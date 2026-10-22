# Goal: the number one tax repository in the world

Set 22 October 2026 by Michael Cutajar, Ryan Duguid and Jeff Watts. Target: **6 November 2026** for the coverage milestone.

## What "number one" means

Every jurisdiction in the catalogue has a **complete, verified pack**, and nobody else has that. Three tests, all three must pass:

1. **Complete.** Every jurisdiction has a skill for each applicable domain in [docs/SKILL-TAXONOMY.md](docs/SKILL-TAXONOMY.md):
      - TAX (VAT/GST, income tax, social contributions)
   - BK bookkeeping
   - EI e-invoicing
   - PR payroll
   - CF company formation
   - FS financial statements
   - TP transfer pricing
   - TO tax optimisation
   plus cross-border for the corridors that matter to it. "Applicable" is decided per jurisdiction and written in the pack's README (a territory with no VAT has no VAT skill, and says so).
2. **Verified.** Every figure in every skill is tied to an official source that resolves, and the pack passes `scripts/` checks and CI. A guide being present is not coverage. Source preparation is not coverage.
3. **Reviewed.** A named accountant has reviewed the pack (`tier: 1` with a reviewer). This is the last step and the slowest; we build and verify first, then bring accountants in per country.

## Where we are (index.json, 22 October 2026)

| Measure | Now |
|---|---|
| Jurisdiction codes with at least one skill | 246 |
| Jurisdictions with 8 or more skills | 75 |
| Jurisdictions with 7 or fewer | 171 |
| Jurisdictions with 3 or fewer | 34 |
| Skills with a named reviewer (`tier: 1`) | 33 |
| Full guided packs (intake + assembly), per the taxonomy | 13 |

So the work is not "add countries". It is "turn 246 thin or partial packs into complete, verified ones", then get them reviewed.

## How work moves

- One issue per jurisdiction, titled `[XX] Complete the pack`, labelled `coverage` and `owner:<name>`, on the milestone **Cover the world**. The issue lists the domains missing.
- The owner (or their agent) drafts, verifies sources, opens a PR per jurisdiction or small batch. Humans merge. Nothing is counted done until the PR is merged and the issue closed.
- A newcomer takes an `owner:open` issue, or asks for one. Issues are the task list for people and for agents.
- Status is read from the milestone, never from memory.

## Owners

See [OWNERS.md](OWNERS.md).
