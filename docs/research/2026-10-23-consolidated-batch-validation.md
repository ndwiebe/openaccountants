# Consolidated batch validation after main reconciliation

23 October 2026. PR #514 remains the single draft batch. Compared with refreshed main `2df160e1` and merged it in commit `e0d73ab6`. OWNERS was the only merge conflict: preserved main's roles and catalogue plus all 55 Europe assignments (Claude 22, ChatGPT 33), and updated the handover to include Kosovo cross-border and Isle of Man work.

Before reconciliation, comparing the stale branch directly against current main reported 49 sync errors, including absent newer Guides and older metadata. These were branch divergence, not a reason to overwrite newer country work. After reconciliation, the Australia, Italy, Portugal, Sweden and UK source directories have no differences from main.

Validation on the reconciled tree:

- Changed-Guide validation: 74 Guides checked, passed. Existing warning remains for Gibraltar global minimum tax with tax_year 2024. That pack remains parked; this check does not certify its figures.
- Example checker: 232 files examined, 155 executable blocks, zero failures or missing blocks reported by the selected mode. It does not establish legal eligibility or comprehensive examples for every Guide.
- Strict sync-integrity audit against current main: 83 source files, zero errors/warnings/notices.
- Repository unit tests: 128 passed using Python 3.12.14 and pinned PyYAML 6.0.3.
- Diff whitespace check passed.

Local test setup findings: the default Python 3.9 produced 19 errors because Path.write_text lacks the newline argument. Bundled Python 3.12 initially lacked PyYAML, then seven temporary-repository tests failed because macOS temporary-path aliases differed from resolved paths. Installed the pinned dependency in /tmp/oa-validation-python312 and used TMPDIR=/private/tmp; all 128 tests then passed without modifying tests or implementation. The separate MCP dependency/test suite was not run locally in this pass; it remains a CI gate.

These checks establish structural, arithmetic and merge compatibility only. Independent legal/source review and professional attestation remain separate outstanding gates. No readiness-for-merge or comprehensive-country claim is made.
