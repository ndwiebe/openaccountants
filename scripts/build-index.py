#!/usr/bin/env python3
"""
Build index.json — a machine-readable inventory of every Guide in the repo.

Walks skills/**/*.md and packages/us-federal/*.md (the hand-authored federal
set), skips READMEs and files without frontmatter, and writes index.json at
the repo root:

{
  "generated_at": "<UTC ISO>",
  "counts": { "guides": N, "jurisdictions": N, "accountant_reviewed": N },
  "guides": [ { "slug", "path", "name", "jurisdiction", "category", "tier",
                "verified_by", "reviewed_by", "tax_year", "last_updated" }, ... ]
}

Dependency-free (stdlib only). Frontmatter is parsed with a simple ---block
line scanner; malformed YAML is tolerated by regex-extracting the known keys.

Usage:
    python3 scripts/build-index.py            # write index.json and restamp the llms.txt counts
    python3 scripts/build-index.py --out PATH # write elsewhere (used by CI)
"""

import json
import os
import re
import sys
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Directories walked for guide files.
GUIDE_TREES = [
    "skills",
    os.path.join("packages", "us-federal"),
]

# Frontmatter keys parsed for index rows and the review-count predicate.
KNOWN_KEYS = [
    "name",
    "jurisdiction",
    "category",
    "tier",
    "verified_by",
    "reviewed_by",
    "review_status",
    "authored_by",
    "tax_year",
    "last_updated",
]

# `key: value` at column 0. Tolerates malformed YAML elsewhere in the block.
KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):[ \t]*(.*)$")

# Jurisdiction values that look like codes get uppercased (MT, US, US-CA, CA-ON).
CODE_RE = re.compile(r"^[A-Za-z]{2,3}(-[A-Za-z0-9]{1,4})*$")


def extract_frontmatter(text):
    """Return the raw frontmatter block (str) or None if the file has none."""
    if not text.startswith("---"):
        return None
    first_nl = text.find("\n")
    if first_nl == -1 or text[:first_nl].strip() != "---":
        return None
    end = re.search(r"^(---|\.\.\.)\s*$", text[first_nl + 1:], re.MULTILINE)
    if not end:
        return None
    return text[first_nl + 1: first_nl + 1 + end.start()]


def clean_value(raw):
    """Normalize a scalar frontmatter value; None for empty/block scalars."""
    value = raw.strip()
    if value in ("", ">", "|", ">-", "|-", ">+", "|+"):
        return None
    # Strip a trailing YAML comment only when the value is unquoted.
    if value[0] in "\"'":
        quote = value[0]
        if len(value) >= 2 and value.rstrip().endswith(quote):
            value = value.strip()[1:-1].strip()
    else:
        value = re.sub(r"\s+#.*$", "", value).strip()
    if value == "" or value.lower() in ("null", "~"):
        return None
    return value


def parse_known_keys(block):
    """Regex-extract KNOWN_KEYS from a frontmatter block, malformed or not."""
    fields = {key: None for key in KNOWN_KEYS}
    for line in block.splitlines():
        match = KEY_RE.match(line)
        if not match:
            continue
        key = match.group(1)
        if key not in fields or fields[key] is not None:
            continue
        raw = match.group(2)
        fields[key] = clean_value(raw)
        # The stdlib scanner cannot qualify block-scalar provenance. Preserve
        # its explicit presence so it cannot masquerade as absent legacy data.
        if key in ("authored_by", "review_status") and raw.lstrip().startswith((">", "|")):
            fields[key] = raw.strip()
    return fields


def guide_files():
    """Yield repo-relative paths of candidate guide files, sorted."""
    paths = []
    for tree in GUIDE_TREES:
        base = os.path.join(REPO_ROOT, tree)
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames.sort()
            for filename in sorted(filenames):
                if not filename.endswith(".md"):
                    continue
                if filename.lower().startswith("readme"):
                    continue
                full = os.path.join(dirpath, filename)
                paths.append(os.path.relpath(full, REPO_ROOT).replace(os.sep, "/"))
    return sorted(set(paths))


def is_reviewed(guide):
    """Match the MCP legacy tier classifier, rejecting explicit contradictions.

    Missing status/author fields remain supported for legacy records; they do
    not establish that the reviewer is a distinct, current professional.
    """
    if str(guide.get("tier") or "").strip() != "1":
        return False
    raw_status = guide.get("review_status")
    status = "" if raw_status is None else str(raw_status).strip().casefold()
    if status not in ("", "current"):
        return False
    markers = {"pending", "pending_review", "none", "no", "false", "-", "n/a", "tbd"}
    for key in ("reviewed_by", "verified_by"):
        reviewer = str(guide.get(key) or "").strip()
        if reviewer and reviewer.casefold() not in markers:
            author = str(guide.get("authored_by") or "").strip()
            return not author.startswith((">", "|")) and (not author or author.casefold() != reviewer.casefold())
    return False


def build_index():
    guides = []
    reviewed_count = 0
    for rel_path in guide_files():
        with open(os.path.join(REPO_ROOT, rel_path), encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        block = extract_frontmatter(text)
        if block is None:
            continue  # not a guide (no frontmatter)
        fields = parse_known_keys(block)
        reviewed_count += is_reviewed(fields)

        jurisdiction = fields["jurisdiction"]
        if jurisdiction and CODE_RE.match(jurisdiction):
            jurisdiction = jurisdiction.upper()

        tier = fields["tier"]
        if isinstance(tier, str) and tier.isdigit():
            tier = int(tier)

        guides.append({
            "slug": os.path.splitext(os.path.basename(rel_path))[0],
            "path": rel_path,
            "name": fields["name"],
            "jurisdiction": jurisdiction,
            "category": fields["category"],
            "tier": tier,
            "verified_by": fields["verified_by"],
            "reviewed_by": fields["reviewed_by"],
            "tax_year": fields["tax_year"],
            "last_updated": fields["last_updated"],
        })

    guides.sort(key=lambda g: g["path"])

    jurisdictions = {g["jurisdiction"] for g in guides if g["jurisdiction"]}
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "counts": {
            "guides": len(guides),
            "jurisdictions": len(jurisdictions),
            "accountant_reviewed": reviewed_count,
        },
        "guides": guides,
    }


# The counts sentence in llms.txt. A default build restamps it from the same
# counts that go into index.json, so the two never disagree; llms-full.txt
# embeds llms.txt and picks the figures up on its next build.
LLMS_COUNTS_RE = re.compile(
    # "Guides" until 16 Oct 2026, "AI skills" after: match both so the first build
    # after the rename restamps instead of warning.
    r"[\d,]+ (?:Guides|AI skills) across [\d,]+ jurisdictions in this repository, "
    r"[\d,]+ of them (?P<label>accountant-reviewed|checked by a named accountant other than the author)"
)


def stamp_llms_counts(counts, path=None):
    """Rewrite the counts sentence in llms.txt; return True when it changed."""
    path = path or os.path.join(REPO_ROOT, "llms.txt")
    # newline="" keeps the file's own line endings on both read and write.
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    stamped, n = LLMS_COUNTS_RE.subn(
        lambda match: f"{counts['guides']:,} AI skills across {counts['jurisdictions']:,} "
        f"jurisdictions in this repository, {counts['accountant_reviewed']:,} "
        f"of them {match.group('label')}",
        text,
    )
    if n != 1:
        # A missing or duplicated sentence is a docs defect, not a reason to
        # fail the build that the nightly export depends on.
        print(f"warning: llms.txt counts sentence found {n} times, expected 1; not restamped", file=sys.stderr)
        return False
    if stamped == text:
        return False
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(stamped)
    return True


def main():
    out_path = os.path.join(REPO_ROOT, "index.json")
    custom_out = "--out" in sys.argv
    if custom_out:
        out_path = sys.argv[sys.argv.index("--out") + 1]
    index = build_index()
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(index, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    counts = index["counts"]
    # --out is CI's freshness check; it must not touch tracked files.
    if not custom_out and stamp_llms_counts(counts):
        print("llms.txt counts restamped")
    print(f"index written to {out_path}")
    print(f"  guides: {counts['guides']}")
    print(f"  jurisdictions: {counts['jurisdictions']}")
    print(f"  accountant_reviewed: {counts['accountant_reviewed']}")


if __name__ == "__main__":
    main()
