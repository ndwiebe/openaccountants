"""Exercise the contributor gate's actual Bash and jq with synthetic API pages."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import yaml


@unittest.skipUnless(shutil.which("bash") and shutil.which("jq"), "requires bash and jq")
class ContributorStatusWorkflowTests(unittest.TestCase):
    def run_step(self, step_id, pages, api_failure=False, changed_files=3000):
        workflow = Path(__file__).resolve().parents[1] / ".github/workflows/contributor-status.yml"
        steps = yaml.safe_load(workflow.read_text(encoding="utf-8"))["jobs"]["contributor-status"]["steps"]
        script = steps[step_id]["run"]
        stubs = r'''
        curl() { cat "$API_PAGES"; }
        gh() {
          [ "$API_FAILURE" = "0" ] || return 1
          if [ "$2" = "-X" ]; then
            printf 'MUTATION=%s %s\n' "$3" "$4"
            return
          fi
          while [ "$#" -gt 0 ]; do
            if [ "$1" = "--jq" ]; then
              jq -r "$2" "$API_PAGES"
              return
            fi
            shift
          done
          return 2
        }
        '''
        if os.name == "nt":
            stubs = 'jq() { command jq --binary "$@"; }\n' + stubs
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fixture = root / "pages.json"
            fixture.write_text("\n".join(json.dumps(page) for page in pages), encoding="utf-8")
            output = root / "output"
            env = {**os.environ, "REPO": "example/skills", "PR_NUMBER": "1", "PR_LOGIN": "example",
                   "API_PAGES": fixture.as_posix(), "API_FAILURE": "1" if api_failure else "0",
                   "PR_CHANGED_FILES": str(changed_files),
                   "GITHUB_OUTPUT": output.as_posix(), "RUNNER_TEMP": root.as_posix(),
                   "MARKER": "<!-- contributor-status -->", "STATUS": "unknown",
                   "LOOKUP_FAILED": "false", "TOUCHES_SKILLS": "false"}
            result = subprocess.run([shutil.which("bash"), "--noprofile", "--norc"],
                                    input=stubs + script, env=env, text=True, capture_output=True)
            return result, output.read_text(encoding="utf-8") if output.exists() else ""

    def test_skills_path_on_first_page_of_large_pr_is_not_lost(self):
        files = [{"filename": "skills/example.md"}] + [
            {"filename": f"docs/{i:04d}-{'x' * 180}.md"} for i in range(2999)
        ]
        result, output = self.run_step(0, [files[i:i + 100] for i in range(0, len(files), 100)])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("touches_skills=true", output)

    def test_code_only_pr_is_not_treated_as_skills(self):
        result, output = self.run_step(0, [[{"filename": "scripts/example.py"}]])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("touches_skills=false", output)

    def test_skill_renamed_out_of_source_tree_still_requires_accountant(self):
        result, output = self.run_step(0, [[{
            "filename": "docs/example.md", "previous_filename": "skills/example.md", "status": "renamed"
        }]])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("touches_skills=true", output)

    def test_pr_beyond_api_file_limit_fails_closed(self):
        result, output = self.run_step(0, [[{"filename": "docs/example.md"}]], changed_files=3001)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(output, "")

    def test_file_api_failure_does_not_report_code_only(self):
        result, output = self.run_step(0, [], api_failure=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(output, "")

    def test_human_marker_does_not_hide_bot_comment(self):
        comments = [
            {"id": 10, "user": {"login": "contributor"}, "body": "<!-- contributor-status -->"},
            {"id": 20, "user": {"login": "github-actions[bot]"}, "body": "<!-- contributor-status -->"},
        ]
        result, _ = self.run_step(3, [comments])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("updated comment 20", result.stdout)
        self.assertNotIn("updated comment 10", result.stdout)

    def test_profile_text_cannot_inject_verified_status(self):
        result, output = self.run_step(1, [{
            "status": "unknown", "name": "Example\nstatus=verified",
            "jurisdiction": "DE\r\nstatus=verified", "credential": "Example\nstatus=verified"
        }])
        self.assertEqual(result.returncode, 0, result.stderr)
        status_lines = [line for line in output.splitlines() if line.startswith("status=")]
        self.assertEqual(status_lines, ["status=unknown"])

    def test_human_marker_alone_causes_new_bot_comment(self):
        result, _ = self.run_step(3, [[
            {"id": 10, "user": {"login": "contributor"}, "body": "<!-- contributor-status -->"}
        ]])
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("created comment", result.stdout)
        self.assertNotIn("updated comment", result.stdout)


if __name__ == "__main__":
    unittest.main()
