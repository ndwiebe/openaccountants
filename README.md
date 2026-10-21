# OpenAccountants

**Free AI skills (tax rules your AI follows) your AI can cite, with sources and a published attribution state.**

The platform uses three attribution states: built by the OpenAccountants team, Accountant-authored or Checked by a named second accountant. Legacy source files may lack these fields; missing provenance is unavailable, not evidence of team authorship or an independent check. Read the frontmatter before relying on a skill. Skill content is source-available under the terms in [LICENSING.md](LICENSING.md).

## Need someone to do the accounting?

OpenAccountants also helps business owners get bookkeeping and tax work done through partner accountants. Tell us what you need, including work across countries. We confirm whether we can take it on, who will do the work and the price before you commit.

**[Book a free 30-minute call](https://www.openaccountants.com/tax-help?source=github_readme#book)** · [Explore our accounting services](https://www.openaccountants.com/tax-help?source=github_readme)

The skills and AI connection remain free.

[![License: AGPL-3.0](https://img.shields.io/badge/license-AGPL--3.0-047857)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/openaccountants-mcp?label=openaccountants-mcp&color=047857)](https://pypi.org/project/openaccountants-mcp/)
[![GitHub stars](https://img.shields.io/github/stars/openaccountants/openaccountants?style=social)](https://github.com/openaccountants/openaccountants/stargazers)

<!-- oa-stats:start -->
**1,903 AI skills** across **231 jurisdictions** · **33 accountant-reviewed** · **38 named accountants** · **20,782 questions answered** through connected AIs

<sub>Live from openaccountants.com — updated 2026-10-21 by the nightly sync.</sub>
<!-- oa-stats:end -->

---

## Try it in 60 seconds

Add the hosted connector to Claude, ChatGPT, Cursor, Windsurf or any MCP client:

```
https://www.openaccountants.com/api/mcp
```

Guided setup: **[openaccountants.com/connect](https://www.openaccountants.com/connect)**

Listed on [Smithery](https://smithery.ai/server/info-ood9/openaccountants) and the [MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.openaccountants/openaccountants).

Then ask a question your AI would otherwise guess at:

> *"What's the combined sales tax rate in Manatee County, Florida for 2026?"*

Without OpenAccountants, models answer from training data. With it, the answer can cite the fetched skill and its recorded provenance. Check the review status and authorship before claiming that a named accountant independently checked the current version.

```
You:    "I'm moving to Malta and selling my company next year. What tax do I face?"
          ↓  loads moving-to-malta-tax-residence, selling-a-company-in-malta
AI:     Residence and domicile · Remittance basis on foreign income
        Gain on the share sale · Participation exemption check
        ─────────────────────────────────────────
        Authored by Michael Cutajar CPA, ACCA (Malta)
```

<details>
<summary><strong>Prefer self-hosting or manual files?</strong></summary>

- **pip MCP server:** `pip install openaccountants-mcp` (mirrors this repo's `packages/`)
- **Manual:** download your jurisdiction's folder from [`packages/`](packages/) and upload the files to your AI. Start with your country's main package; `index.json` is the machine-readable inventory.

</details>

---

## Three states, greppable honesty

These are the platform's attribution states. Source files exported under older conventions may not yet identify one:

| State | Meaning | Grep for |
|---|---|---|
| **Built by Michael Cutajar and the OpenAccountants team** | Written by the team from primary sources, every figure cited. No named accountant stands behind it | `trust_label: Built by` |
| **Accountant-authored** | A named accountant, approved on openaccountants.com, wrote it. Not yet independently checked | `authored_by:` with a person's name and `trust_label: Accountant-authored` |
| **Checked by <name>** | An accountant other than the author checked the complete skill. Their name is in `reviewed_by:` and on [the public roster](VERIFIERS.md) | `reviewed_by:` with `review_status: current` |

`tier` is the legacy machine field. The scripts and self-hosted MCP retain tier 1 records with a named reviewer when author or review-status fields are absent. They reject explicit non-current reviews and identical author/reviewer names. A legacy tier alone does not prove a distinct accountant checked the current version; confirm that evidence on the platform. Tier 2 does not establish an independent check.

⚠️ **General reference, not advice.** skills may be incomplete, outdated, or wrong for your facts. Have a qualified professional review outputs before filing, payment, or action.

---

## Are you an accountant?

Your name on the tax knowledge AI actually uses, with attribution built in:

1. **Open a pull request** with a skill for the work you know cold: see [CONTRIBUTING.md](CONTRIBUTING.md). Your AI can write the file from our template in 15 minutes ([docs/CONTRIBUTE-PROMPT.md](docs/CONTRIBUTE-PROMPT.md)). Once merged it is live on openaccountants.com and in every connected AI, credited to you as Accountant-authored.
2. **Check a skill:** open a pull request against any skill in your jurisdiction that someone else wrote; once merged, the skill reads "Checked by" with your name.
3. **Set your GitHub username** in [your profile](https://www.openaccountants.com/profile). The `contributor-status` check uses it to recognise you as a verified accountant. Your changes arrive as your own pull requests; the platform export carries team edits and metadata.

The current roster: **[VERIFIERS.md](VERIFIERS.md)** (generated nightly from the platform).

---

## How it stays accurate

A tax library is only as good as its worst stale number, so machines re-check this one
every night:

- **The maths check** re-reads every guide and flags sums that do not add up, tax bands
  with gaps, totals that do not total, and years that disagree.
- **The source watch** visits the official pages the figures came from and raises a hand
  when a page changes.
- **The refresh engine** re-derives the stalest guides from official sources on a fixed
  monthly budget, refusing to publish any figure without a link.
- **The nightly exam** tests whether AIs actually said what the guides say that day, or
  improvised. Improvisation gets caught, counted and fixed at the source.

The sync runs both ways: the nightly export carries team edits and platform metadata only,
and merged PRs here flow into what every AI serves, credited to you. Accountants' changes
arrive as their own pull requests. A guide with an accountant's byline never changes without
that accountant's one-click approval.

The whole story, in plain words: [openaccountants.com/how-it-works](https://www.openaccountants.com/how-it-works)

---

## Contributing

Edit **`skills/**` only** — everything else regenerates automatically:

- `packages/`, `index.json`, `llms-full.txt` — generated nightly; never edit in a PR
- Merged source PRs are credited to you and must be confirmed as ingested before the next platform export
- Skill PRs are merged only from verified accountants; the `contributor-status` check tells you where you stand
- Full guide: [CONTRIBUTING.md](CONTRIBUTING.md) · Layout: [docs/REPO-LAYOUT.md](docs/REPO-LAYOUT.md)

---

## For developers

| What | Where |
|---|---|
| Skill source (per jurisdiction) | [`skills/`](skills/) |
| Per-country bundles (generated) | [`packages/`](packages/) |
| Machine-readable inventory | [`index.json`](index.json) |
| LLM entry point | [`llms.txt`](llms.txt) |
| Python MCP server | [`mcp/`](mcp/) · [PyPI](https://pypi.org/project/openaccountants-mcp/) |
| Repo architecture + sync | [`docs/REPO-LAYOUT.md`](docs/REPO-LAYOUT.md) · [`docs/WEBSITE-SYNC.md`](docs/WEBSITE-SYNC.md) |

API and platform integrations: [openaccountants.com/for-developers](https://www.openaccountants.com/for-developers)

---

## Related open-source projects

Independent, open-source review aids and calculation tools that complement the OpenAccountants guide library:

- **[payday-super-checker](https://github.com/ryanduguid/australian-accounting/tree/main/packages/payday-super-checker)** (MIT) — Verifies superannuation contributions against Australian Payday Super deadlines (in force since 1 July 2026) and estimates SG charge exposure on late payments, with all workings and statutory assumptions disclosed.
- **[div7a-loan-review](https://github.com/ryanduguid/australian-accounting/tree/main/packages/div7a-loan-review)** (MIT) — Reviews Division 7A loan terms and minimum yearly repayments against the ATO benchmark interest rate, with fabricated inputs and explicit refusal boundaries.
- **[xero-trial-balance-export](https://github.com/ryanduguid/accounting-review-pipeline/tree/main/packages/xero-trial-balance-export)** (MIT) — Exports a Xero trial balance to CSV only when month-movement and YTD column pairs both balance exactly.
- **[ato-benchmark-compare](https://github.com/ryanduguid/australian-accounting/tree/main/packages/ato-benchmark-compare)** (MIT) — Evaluates business P&L statements locally against the Australian Taxation Office (ATO) small business performance benchmarks, surfacing variance flags and ratio analyses.

*(External tools provide computational review assistance and do not constitute tax or legal advice.)*

---

## License

- **Code** (mcp/, scripts/, tools/): [AGPL-3.0](LICENSE)
- **skill content**: OpenAccountants Guide License v1.0 — see [LICENSING.md](LICENSING.md); commercial options in [COMMERCIAL-LICENSING.md](COMMERCIAL-LICENSING.md)

**Contact:** info@openaccountants.com · [Security policy](SECURITY.md) · [Cite this repo](CITATION.cff)
