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
| IT-IND | [Individual tax](gi-individual-income-tax.md) | Statutory ordinary rates, selected allowances, specified approved/imported pension scope and UK scheme-qualification routes, non-resident pensioner relief limit and claim requirements, pre-death income obligations, return deadline and penalties now drafted; complete reliefs, payment operations, partial-year cross-reference and special regimes |
| IT-CORP | [Company tax](gi-corporate-tax.md); [global minimum tax](gi-global-minimum-tax.md) | UK treaty PE/business-profits and cessation stock valuation rules now drafted; domestic minimum-tax framework, ordinary-tax election conditions, filing/payment and selected penalties now drafted; full GloBE calculations, current administrative channels and specialised regimes; resolve identified calculation and procedural questions |
| XB | [Foreign-tax relief](gi-foreign-tax-relief.md), [Spain residence agreement](gi-spain-tax-residence.md), [UK investment-income agreement](gi-uk-investment-income-treaty.md), [UK employment and pensions](gi-uk-employment-pensions-treaty.md) | Spain residence tests drafted; timing conflict, historical corporate exception/list, Spanish definitions and claim channels open; UK investment-income eligibility, ceilings and capital-gain allocation drafted; employment/pension allocation drafted with an explicit HMRC-summary conflict; Gibraltar MAP submission procedure now drafted; company UK-interest evidence route now drafted; exact claim deadlines, other domestic relief procedures and remaining treaty topics open |
| VAT | [Goods transaction-tax transition](gi-transaction-tax-transition.md) | Charging rules, valuation, rate calendar, transitional-stock routes and deductions rules now drafted from enacted sources; still verify commodity classifications, customs procedures, relief extensions, state-aid limits and operational deadlines |
| SC | [Payroll and social insurance](gi-payroll-social-insurance.md) | UK bilateral posting/multiple-activity rules now drafted; special classes, partial periods, self-employed procedure, UK temporary-work certificate routes now drafted; Gibraltar-issued certificates and other cross-border coverage evidence |
| BK | [Books and tax records](gi-bookkeeping-and-tax-records.md) | Posting examples and chart of accounts, full reconciliation workflow, electronic-original and sector requirements |
| EI | [Invoices and procurement e-invoicing](gi-einvoice.md) | Covered procurement receipt/processing law and core fields drafted; verify current procurement eligibility, standard/syntax versions, endpoints, general B2B/B2C scope and retention |
| PR | [Payroll and social insurance](gi-payroll-social-insurance.md) | PAYE working examples, benefits in kind, starters/leavers, special cases and employment-cost boundaries |
| CF | [Company formation](gi-company-formation.md) | Core beneficial-ownership duties and GFSC transition now drafted; full nominee/appointor procedures, access/sanctions, permissions, alternative entities and unresolved statutory cross-reference |
| FS | [Accounts and reporting](gi-company-accounts-and-reporting.md) | Group consolidation duty, size tests and exemption conditions now drafted; audit-exemption cross-reference, complete disclosure schedules, regulated-entity successor provisions and case-specific group evidence remain open |
| TP | [Connected-party pricing and interest](gi-connected-party-pricing-and-interest.md) | Shareholder-loan deemed distributions, later dividend set-off and section 42 clearance/section 43 appeal procedure now drafted; remaining anti-avoidance/interest restrictions, claim mechanics, documentation/reporting and cross-border application |
| TO | [Training, planning and start-up reliefs](gi-training-planning-and-startup-reliefs.md), company loss/allowance sections | Remaining reliefs, elections, operational claims and interaction questions; historical relief windows must stay distinct from current eligibility |

Additional required topics are only partly drafted: [foreign-tax relief](gi-foreign-tax-relief.md), [property stamp duty](gi-property-stamp-duty.md), [residential disposals](gi-residential-property-disposals.md), and [enquiries and appeals](gi-income-tax-assessment-appeals.md). Named treaty corridors, withholding, complete property reliefs and procedural submission channels remain open. Non-resident representative obligations, statutory agency appeals and liquidation tax provision are now drafted, with case-specific scope open; Income Tax Act section 52(2) points to current Companies Act section 305, which concerns merger terms, so the liquidation successor provision/date remains unresolved. Domestic overpayment entitlement and its six-year claim period are now drafted separately from appeals; operational refund channels and interest remain open. A domestic foreign-tax-credit example is not a treaty corridor.

## Next work and acceptance evidence

1. Complete transaction-tax operational procedures and remaining incorporated treaty conditions; the charging, valuation and baseline rate-date gaps have source-backed draft treatment. Complete the invoicing operational and wider-scope research and payroll procedures.
2. Close material source/interpretation questions recorded in each Guide and the dated Gibraltar files in [research](../../../docs/research/). The company accounts audit cross-reference and mixed-loss computation require specific conclusions, not generic disclaimers.
3. All seventeen Gibraltar Guides now have `sources:` frontmatter, including the corporate, individual and property baseline Guides. Verify that every operative claim is covered by the listed source versions. Body citations alone do not satisfy issue #398's metadata requirement. Recheck resolved sources and recompute examples on the exact reviewed revision.
4. Obtain independent source review and the named accountant review required by GOAL.md. Record identity, date, exact revision and findings; do not promote tiers from automated checks.
5. Run Guide and sync checks plus the owner coverage report. The report reads the source tree in memory and classifies slugs/categories. Explicit mappings now connect the consumption, connected-party and cross-border drafts to the current tax domain names. Zero mechanically missing domains would still not establish legal completeness; the gaps above remain open.
6. Merge only after required checks and reviews, then verify platform ingestion and served content. Keep issue #398 open until the whole acceptance scope is proved.

The baseline issue lists five Guides. This branch contains seventeen Guide files, but neither number is a comprehensive-coverage count. Do not create duplicate Guides merely to satisfy filename matching in the coverage script.
