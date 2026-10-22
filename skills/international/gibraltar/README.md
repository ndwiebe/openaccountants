---
jurisdiction: GI
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  VAT: gi-transaction-tax-transition
  TP: gi-connected-party-pricing-and-interest
  XB: gi-foreign-tax-relief
---

# Gibraltar pack: coverage and remaining work

Owner: Michael, as recorded in [issue #398](https://github.com/openaccountants/openaccountants/issues/398). Work in [consolidated PR #514](https://github.com/openaccountants/openaccountants/pull/514). Reconciled 22 October 2026. This is a work queue, not a certificate of complete coverage. Every Guide remains a source-cited draft; no independent review or professional attestation is recorded here.

The seven tax domains in current GOAL.md remain in scope. No domain has a reviewed, source-backed not-applicable determination. VAT is the programme's consumption-tax category; the mapped goods transaction-tax Guide does not assert Gibraltar has retail VAT. The accounting topics below belong to the second milestone and do not count as missing tax domains. Explicit mappings identify existing drafts; they do not certify their completeness.

| Domain | Existing draft material | Work still required before acceptance |
|---|---|---|
| IT-IND | [Individual tax](gi-individual-income-tax.md) | Statutory ordinary rates, selected allowances, return deadline and penalties now drafted; complete reliefs, payment operations, partial-year cross-reference and special regimes |
| IT-CORP | [Company tax](gi-corporate-tax.md) | Specialised company regimes and minimum taxes; resolve identified calculation and procedural questions |
| XB | [Foreign-tax relief](gi-foreign-tax-relief.md) | Named treaty corridors, residence conflicts, withholding and procedural relief evidence |
| VAT | [Goods transaction-tax transition](gi-transaction-tax-transition.md) | Charging rules, valuation, rate calendar, transitional-stock routes and deductions rules now drafted from enacted sources; still verify commodity classifications, customs procedures, relief extensions, state-aid limits and operational deadlines |
| SC | [Payroll and social insurance](gi-payroll-social-insurance.md) | Special classes, partial periods, self-employed procedure and cross-border coverage evidence |
| BK | [Books and tax records](gi-bookkeeping-and-tax-records.md) | Posting examples and chart of accounts, full reconciliation workflow, electronic-original and sector requirements |
| EI | [Invoices and procurement e-invoicing](gi-einvoice.md) | Covered procurement receipt/processing law and core fields drafted; verify current procurement eligibility, standard/syntax versions, endpoints, general B2B/B2C scope and retention |
| PR | [Payroll and social insurance](gi-payroll-social-insurance.md) | PAYE working examples, benefits in kind, starters/leavers, special cases and employment-cost boundaries |
| CF | [Company formation](gi-company-formation.md) | Beneficial ownership, permissions, alternative entities and unresolved statutory cross-reference |
| FS | [Accounts and reporting](gi-company-accounts-and-reporting.md) | Audit-exemption cross-reference, disclosure schedules, groups and specialised entities |
| TP | [Connected-party pricing and interest](gi-connected-party-pricing-and-interest.md) | Remaining anti-avoidance/interest restrictions, documentation/reporting and cross-border application |
| TO | [Training, planning and start-up reliefs](gi-training-planning-and-startup-reliefs.md), company loss/allowance sections | Remaining reliefs, elections, operational claims and interaction questions; historical relief windows must stay distinct from current eligibility |

Additional required topics are only partly drafted: [foreign-tax relief](gi-foreign-tax-relief.md), [property stamp duty](gi-property-stamp-duty.md), and [enquiries and appeals](gi-income-tax-assessment-appeals.md). Named treaty corridors, withholding, complete property reliefs and procedural submission channels remain open. A domestic foreign-tax-credit example is not a treaty corridor.

## Next work and acceptance evidence

1. Complete transaction-tax operational procedures and remaining incorporated treaty conditions; the charging, valuation and baseline rate-date gaps have source-backed draft treatment. Complete the invoicing operational and wider-scope research and payroll procedures.
2. Close material source/interpretation questions recorded in each Guide and the dated Gibraltar files in [research](../../../docs/research/). The company accounts audit cross-reference and mixed-loss computation require specific conclusions, not generic disclaimers.
3. Complete `sources:` frontmatter for the remaining baseline property Guide; the individual Guide now has statutory source metadata. Body citations alone do not satisfy issue #398's metadata requirement. Recheck resolved sources and recompute examples on the exact reviewed revision.
4. Obtain independent source review and the named accountant review required by GOAL.md. Record identity, date, exact revision and findings; do not promote tiers from automated checks.
5. Run Guide and sync checks plus the owner coverage report. The report reads the source tree in memory and classifies slugs/categories. Explicit mappings now connect the consumption, connected-party and cross-border drafts to the current tax domain names. Zero mechanically missing domains would still not establish legal completeness; the gaps above remain open.
6. Merge only after required checks and reviews, then verify platform ingestion and served content. Keep issue #398 open until the whole acceptance scope is proved.

The baseline issue lists five Guides. This branch contains thirteen Guide files, but neither number is a comprehensive-coverage count. Do not create duplicate Guides merely to satisfy filename matching in the coverage script.
