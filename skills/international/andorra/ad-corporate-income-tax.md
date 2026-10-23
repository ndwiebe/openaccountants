---
name: ad-corporate-income-tax
description: "Source-cited draft: corporate income tax for Andorra (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: AD
tax_year: 2025
last_updated: 2026-10-23
version: 0.2
category: international
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Andorra Corporate Income Tax

## Corporate income tax (Impost sobre Societats)

- **Standard corporate income tax rate** — 10% on taxable profit %  _(Llei 95/2010 IS)_
- **Reduced rate for newly created companies** — Historically 5% on the first EUR 50,000 of taxable base in the first years of activity % (approx — confirm this incentive is still in force for 2025)  _(Llei 95/2010 IS)_
- **Holding-company (ETVPESE) regime** — Qualifying foreign-shareholding income (dividends and capital gains) may be exempt, giving an effective rate near 0% (approx — confirm current qualifying conditions)  _(Llei 95/2010 IS (regim de societats de tinenca de participacions))_
- **Intangible-exploitation / IP regime** — Qualifying income from exploitation of certain intangibles may benefit from a reduced effective rate (around 2%) % (approx — confirm; subject to OECD nexus / substance rules)  _(Llei 95/2010 IS)_
- **Tax base** — Accounting profit per Andorran GAAP (Pla General de Comptabilitat), adjusted for tax-specific items  _(Llei 95/2010 IS)_
- **Corporate residence** — A company is resident if incorporated under Andorran law, has its registered office in Andorra, or has its effective management in Andorra  _(Llei 95/2010 IS)_
- **Withholding tax on dividends to non-residents** — 0% — no withholding tax on dividends paid by Andorran companies to non-residents %  _(Llei 94/2010 IRNR)_
- **Withholding tax on interest to non-residents** — 0% — no withholding tax on interest paid to non-residents %  _(Llei 94/2010 IRNR)_
- **Withholding tax on royalties to non-residents** — 5% (may be reduced under an applicable double tax treaty) % (approx — confirm treaty rates)  _(Llei 94/2010 IRNR)_
- **IS filing window** — The month following the six months after the tax period ends. For a 31 December 2025 year-end, the ordinary window is July 2026. Earlier filing during the first six months is permitted without changing payment/refund deadlines. Confirm the current approved form; no form number is certified here. [Corporate-tax regulation, Article 45](https://www.portaljuridicandorra.ad/R20231229C).
- **Advance payment** — During the ninth month after the period begins, pay 50% of the immediately preceding period's settlement liability. For a calendar-year business this is September. If the previous period was shorter than twelve months, include proportionate liability from preceding periods to complete twelve months. The regulation excludes the first activity year from this advance. [Law 95/2010, Article 45](https://www.portaljuridicandorra.ad/L2010095); [regulation, Article 37](https://www.portaljuridicandorra.ad/R20231229C).

## Filing and payment workpapers

**Scope of this update:** filing and ordinary advance-payment rules were checked on 23 October 2026 against the current legal-portal consolidations. The other legacy 2025 bullets above, including approximate incentives, have not been reverified by this update and must not be used as confirmed current advice. The portal labels its consolidations as without official legal status. This remains a partial source-cited draft, not comprehensive corporate-tax coverage.

Reconcile the settlement liability before advances to the payments actually made. Under Article 46, payments under Articles 45 and 45 bis are credited to determine the balance; an excess is refundable. Property-transfer advances have their own rules, including timing of credit where income is recognised over deferred receipts, and are not computed in the examples below. [Law, Article 46](https://www.portaljuridicandorra.ad/L2010095).

### Example 1: ordinary advance and balance

Assume a full prior year, prior settlement liability EUR 18,000, current settlement liability EUR 22,000 and no property advance or other adjustment. The September advance is EUR 9,000. After it is paid, the annual balance is EUR 13,000. The settlement liabilities are assumed independently verified; the example does not compute incentives or taxable profit.

```oa-check
name: Andorra ordinary advance and annual balance
inputs:
  prior_liability: 18000
  advance_rate: 0.50
  current_liability: 22000
steps:
  advance: prior_liability * advance_rate
  final_balance: current_liability - advance
expected:
  advance: 9000
  final_balance: 13000
```

### Example 2: excess advance

Assume a full prior year with settlement liability EUR 20,000, a EUR 10,000 advance actually paid, current settlement liability EUR 6,000 and no other adjustments. The balance is negative EUR 4,000, producing a EUR 4,000 excess for refund under Article 46. This arithmetic does not establish when the refund will be received.

```oa-check
name: Andorra advance excess reconciliation
inputs:
  prior_liability: 20000
  advance_rate: 0.50
  current_liability: 6000
steps:
  paid_advance: prior_liability * advance_rate
  final_balance: current_liability - paid_advance
  excess: paid_advance - current_liability
expected:
  paid_advance: 10000
  final_balance: -4000
  excess: 4000
```

Ask for the declared accounting period, activity start date, prior-period lengths and settlement liabilities, payment receipts, and any property-transfer advances before applying this timetable. Current electronic forms, general penalties, special regimes, the full tax-base calculation and professional review remain outstanding.

## Sources

Filing/payment provisions read 23 October 2026:

- [Law 95/2010, Articles 45–46](https://www.portaljuridicandorra.ad/L2010095).
- [Corporate-tax regulation, Articles 37 and 45](https://www.portaljuridicandorra.ad/R20231229C).

These citations substantiate the updated filing/payment sections, not every legacy incentive claim above.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
