---
jurisdiction: GI
applicable: [TAX-VAT, TAX-IT, TAX-SC, BK, EI, PR, CF, FS, TP, TO]
not_applicable: {}
---

# Gibraltar pack: coverage and remaining work

Owner: Michael, as recorded in [issue #398](https://github.com/openaccountants/openaccountants/issues/398). Work in [consolidated PR #514](https://github.com/openaccountants/openaccountants/pull/514). Reconciled 22 October 2026. This is a work queue, not a certificate of complete coverage. Every Guide remains a source-cited draft; no independent review or professional attestation is recorded here.

All ten programme domains remain in scope. No domain has a reviewed, source-backed not-applicable determination. In particular, retaining EI means its applicability must be investigated, not that an electronic-invoicing mandate has been established. TAX-VAT is the programme's consumption-tax category; retaining it does not assert Gibraltar has a retail VAT. Neither uncertainty is removed from the denominator to improve the report.

| Domain | Existing draft material | Work still required before acceptance |
|---|---|---|
| TAX-IT | [Company tax](gi-corporate-tax.md), [individual tax](gi-individual-income-tax.md) | Individual income/allowance depth; specialised company regimes and minimum taxes; resolve the company Guide's identified calculation and procedural questions |
| TAX-VAT | [Goods transaction-tax transition](gi-transaction-tax-transition.md) | Operative charging law, commencement, valuation, commodity schedules and post-12-October relief position; the draft explicitly blocks operational reliance |
| TAX-SC | [Payroll and social insurance](gi-payroll-social-insurance.md) | Special classes, partial periods, self-employed procedure and cross-border coverage evidence |
| BK | [Books and tax records](gi-bookkeeping-and-tax-records.md) | Posting examples and chart of accounts, full reconciliation workflow, electronic-original and sector requirements |
| EI | No dedicated draft | Determine legal applicability, invoice fields, electronic format/transmission and retention; obtain positive primary evidence for any not-applicable conclusion |
| PR | [Payroll and social insurance](gi-payroll-social-insurance.md) | PAYE working examples, benefits in kind, starters/leavers, special cases and employment-cost boundaries |
| CF | [Company formation](gi-company-formation.md) | Beneficial ownership, permissions, alternative entities and unresolved statutory cross-reference |
| FS | [Accounts and reporting](gi-company-accounts-and-reporting.md) | Audit-exemption cross-reference, disclosure schedules, groups and specialised entities |
| TP | [Connected-party pricing and interest](gi-connected-party-pricing-and-interest.md) | Remaining anti-avoidance/interest restrictions, documentation/reporting and cross-border application |
| TO | [Training, planning and start-up reliefs](gi-training-planning-and-startup-reliefs.md), company loss/allowance sections | Remaining reliefs, elections, operational claims and interaction questions; historical relief windows must stay distinct from current eligibility |

Additional required topics are only partly drafted: [foreign-tax relief](gi-foreign-tax-relief.md), [property stamp duty](gi-property-stamp-duty.md), and [enquiries and appeals](gi-income-tax-assessment-appeals.md). Named treaty corridors, withholding, complete property reliefs and procedural submission channels remain open. A domestic foreign-tax-credit example is not a treaty corridor.

## Next work and acceptance evidence

1. Resolve the transaction-tax source and commencement gap before expanding its calculations. Complete the missing invoicing applicability research and payroll procedures.
2. Close material source/interpretation questions recorded in each Guide and the dated Gibraltar files in [research](../../../docs/research/). The company accounts audit cross-reference and mixed-loss computation require specific conclusions, not generic disclaimers.
3. Complete `sources:` frontmatter for the older baseline Guides. Body citations alone do not satisfy issue #398's metadata requirement. Recheck resolved sources and recompute examples on the exact reviewed revision.
4. Obtain independent source review and the named accountant review required by GOAL.md. Record identity, date, exact revision and findings; do not promote tiers from automated checks.
5. Run Guide and sync checks plus the owner coverage report. The report classifies indexed slugs/categories and can lag source changes; zero mechanically missing domains would still not establish legal completeness.
6. Merge only after required checks and reviews, then verify platform ingestion and served content. Keep issue #398 open until the whole acceptance scope is proved.

The baseline issue lists five Guides. This branch contains twelve Guide files, but neither number is a comprehensive-coverage count. Do not create duplicate Guides merely to satisfy filename matching in the coverage script.
