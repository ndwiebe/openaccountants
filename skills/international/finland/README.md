---
jurisdiction: FI
version: 0.8
last_updated: 2026-10-23
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: fi-income-tax
  IT-CORP: fi-corporate-income-tax
  XB: fi-individual-cross-border-residence
  PR: fi-employer-payroll
  VAT: finland-vat-return
  SC: fi-yel-social
  TP: fi-transfer-pricing
partial:
  IT-IND: "2026 state/capital scales, ordinary business split, YEL deduction routes and filing sanctions prepared; complete legal chain, deductions/credits, local taxes, income categories and independent review open."
  IT-CORP: "2026 rate, book-to-tax bridge, losses, filing and outbound-payment screening prepared; statutes, exemptions, finance, groups, specialist international cases and independent review open."
  VAT: "Existing return Guide now has executable rate/mixed-use/sanction controls; full statutory, specialist scope and independent review open."
  SC: "YEL contribution/reduction/review controls and selected legal exceptions checked; wider employee/social coverage, annual decrees and independent review open."
  PR: "Reporting/health contribution, tax-card and statutory cash-cap preparation; insurance/benefit exceptions, remaining law and independent review open."
  TP: "Documentation/control/method-selection principles and selected penalty provisions checked; benchmark/transaction application, specialist scope and independent review open."
  XB: "Individual residence core checked to selected statutes; income categories, treaties, companies, PE and independent review open."
---

# Finland tax pack

Accountable owner: Michael. Active writer: ChatGPT support chat under [OWNERS.md](../../../OWNERS.md), [issue #392](https://github.com/openaccountants/openaccountants/issues/392), local branch `codex/finland-country-completion`, consolidated draft [PR #514](https://github.com/openaccountants/openaccountants/pull/514). Michael directed the move from Iceland on 23 October 2026. Existing Guides and research are preserved; all domains remain partial.

The [individual-tax Guide](fi-income-tax.md) now separates the 2026 state scale from total tax, records ordinary sole-trader allocation and removes the contradictory personal-only YEL deduction prohibition. The [corporate Guide](fi-corporate-income-tax.md) now distinguishes the current rate/loss rules from future proposals, with a book-to-tax bridge and loss/payment controls. Existing source work is retained in the topic research records and Git history.

The [transfer-pricing documentation Guide](fi-transfer-pricing.md) addresses a scoped documentation gap. Prepayments, VAT, YEL, payroll, cross-border and property still need full scope and legal review. The formation draft now uses current PRH setup routes/fees, statutory board and registration rules and the precise two-period audit-omission test. Its wider entity, accounting and specialist-law scope remains open. Guide presence and passing checks do not establish comprehensive coverage or professional review.

The [country-by-country reporting draft](fi-country-by-country-reporting.md) distinguishes notification and full-report preparation. The selected statutory notification/report deadlines, secondary/surrogate conditions and penalty provisions are now source-checked; current exchange conditions, case-specific eligibility and independent review remain open.

The [employer-payroll draft](fi-employer-payroll.md) adds reporting and employer health-contribution preparation. It does not complete employee withholding or employer insurance coverage.

The [individual residence draft](fi-individual-cross-border-residence.md) adds arrival/departure and treaty-screening work. It does not establish comprehensive cross-border coverage.

The [property-transfer tax draft](fi-property-transfer-tax.md) adds acquisition-tax preparation for real estate and housing-company shares. Annual property taxation, rental income, gains and full statutory/exception review remain open.

## Evidence and next action

The local 23 October country batch has 33 passing executable controls across eleven source Guides, including the older YEL, VAT and prepayment Guides and a second CbCR threshold-boundary control. All 98 unique non-CTA source URLs have HTTP 200 evidence without redirects, including seven newly checked formation sources. The full local batch passes 129 repository unit tests. These checks do not establish legal accuracy or independent review. Source reachability is recorded separately from legal-content verification in `docs/research/2026-10-23-finland-source-reachability.json`; a successful HTTP response does not prove the rule is correct or current.

Next: finish statutory/source-content reconciliation across the existing pack, obtain one independent full-pack review, fix its findings and publish one reviewed country content batch. A named Finnish accountant review is still required separately. Keep this issue open and the consolidated PR in draft while these gates remain open.

Selected provisions of ten tax, pension, company and audit statutes have been read directly from official Finlex content, including the YEL review-consent and disability exceptions and the 2026 contingent-consideration transition. This is scoped legal reconciliation, not an audit of every statute or exception. Retrieval scope/hashes are in `docs/research/2026-10-23-finland-direct-statute-retrieval.json`.
