---
name: fi-transfer-pricing
description: >
  Screen Finnish transfer-pricing documentation obligations, prepare
  cross-border related-party evidence, distinguish Form 78 from the full
  documentation, and track authority requests. Detailed statutory, method,
  reporting and independent review remain outstanding.
jurisdiction: FI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.2
---

# Finland transfer-pricing documentation v0.2

## Who this applies to

The Finnish Tax Administration's guidance addresses foreign related-party transactions of Finnish taxpayers and dealings between a foreign enterprise and its Finnish PE. The pricing principle also applies to small enterprises outside the full documentation obligation. [Obligation guidance][obligation]

This draft uses official administrative guidance read on 23 October 2026. The obligation page says it will be updated and displays a 2022 update date. Current statutory reconciliation and independent review remain open; the intended tax year does not certify an amendment audit.

## Rates, bands and thresholds

The detailed guidance defines the SME exclusion using all three requirements: fewer than 250 employees; turnover at most EUR 50 million **or** balance sheet at most EUR 43 million; and compliance with the Commission recommendation's SME criteria. Group and linked/partner-enterprise relationships matter. A small Finnish subsidiary cannot determine its status using its standalone figures alone. [Detailed guidance, section 4.3][detailed]

The detailed guidance and Form 78 instructions use turnover **exceeding** EUR 50 million and balance sheet **exceeding** EUR 43 million for that financial-size route. A separate FAQ uses “or more”. Preserve exact-boundary cases for statutory reconciliation rather than silently adopting the FAQ wording. Employee count, EU SME status, group relationships and changes across years still require their own checks. [Detailed guidance][detailed]; [Form 78][form]; [FAQ][faq]

## Requests and filing

The obligation guidance states: annual documentation; Finnish, Swedish or English; submission within 60 days of request, with a six-month post-year-end restriction on when that year's documentation can first be requested; supplementary information within 90 days. Extensions can be requested. It describes a two-consecutive-year size transition and a maximum EUR 25,000 documentation sanction. Verify the statutory conditions before a deadline or penalty conclusion. [Obligation guidance][obligation]

Form 78 is separate from the documentation. Its instructions say documentation is provided on request rather than attached to the return. Where no foreign related-party transactions occurred during the year, those instructions say Form 78 is unnecessary. Check the taxpayer's facts and the applicable return instructions before filing. [Form 78][form]

### EUR 500,000 simplification is assessed by counterparty

Detailed guidance section 4.4 describes reduced documentation where annual controlled dealings with a particular associated enterprise have an arm's-length value no greater than EUR 500,000. Aggregate that counterparty's dealings; do not test each invoice separately. Its examples include service income plus loan interest, and separately a newly drawn loan principal. Repayment of that principal is not counted as another borrowing. [Detailed guidance, section 4.4][detailed]

The simplification can remove the Master File requirement when no counterparty exceeds the threshold. For qualifying below-threshold dealings, it removes specified Local File functional/comparability/method content, while other taxpayer information remains required. It does not exempt the pricing from the arm's-length principle. Keep loan movements and valuation evidence for the applicability check. [Section 4.4][detailed]

## Preparation workpaper

Use this as an evidence checklist, not a claim that it reproduces every statutory local-file requirement:

- Identify the taxpayer, PE, related parties, residences and period.
- Record group structure and reconcile the size/SME calculation to the underlying accounts.
- List each transaction, agreement, booked amount and relevant currency.
- Describe actual conduct, functions, assets and risks; preserve evidence supporting the chosen pricing analysis.
- Connect the analysis and any adjustment to the accounts, tax computation and Form 78.
- Keep the authority's request, receipt date, requested scope, response calendar and delivery acknowledgement together.

A documentation exemption does not establish an acceptable price. Nor does an authority request establish the correct margin: the transaction evidence still needs substantive analysis. No markup, interest rate or method priority is supplied by this checklist.

## Worked example

Assume a supported independent-party price of EUR 120 per unit for 2,000 units sold at EUR 105. The assumed revenue difference is EUR 30,000. The comparable price and all legal conditions are assumptions; this block tests arithmetic only and does not select a tax rate.

```oa-check
name: Finland assumed controlled sale price reconciliation
inputs:
  units: 2000
  booked_unit_price: 105
  supported_unit_price: 120
steps:
  booked_revenue: units * booked_unit_price
  supported_revenue: units * supported_unit_price
  assumed_adjustment: supported_revenue - booked_revenue
expected:
  booked_revenue: 210000
  supported_revenue: 240000
  assumed_adjustment: 30000
```

### 2. Counterparty aggregation

Assume EUR 350,000 services and EUR 180,000 interest with one associated enterprise, both at established arm's-length values. EUR 530,000 exceeds the simplification threshold by EUR 30,000. The example assumes no disputed classification or double counting.

```oa-check
name: Finland documentation counterparty aggregation
inputs:
  service_value: 350000
  interest_value: 180000
  simplification_limit: 500000
steps:
  counterparty_total: service_value + interest_value
  excess_over_limit: counterparty_total - simplification_limit
expected:
  counterparty_total: 530000
  excess_over_limit: 30000
```

## Ask the client first

- Which foreign parties and PE dealings exist, and what establishes the relationships?
- What are the group size figures, ownership links and prior-year changes?
- What transactions and pricing evidence reconcile to the accounts?
- Has an authority requested documents or supplements, and when was it received?
- What return and Form 78 submissions already exist?

## Sources and review limits

Read 23 October 2026. The obligation page was opened directly; detailed guidance, Form 78 and FAQ passages were retrieved from indexed official text.

- [Documentation obligation][obligation], referring to Assessment Procedure Act sections 14a and 14c.
- [Detailed documentation guidance][detailed], SME definition and related calculations.
- [Form 78 instructions][form]; [documentation FAQ][faq].

Not yet confirmed: current consolidated statute and amendments, related-party definition, full master/local-file content, full simplification eligibility and current statutory reconciliation, valuation methods and transaction-specific treatment, CbCR, dispute/APA procedures, current penalties and live filing. Professional attestation and independent review remain outstanding. TP and the country pack remain partial.

[obligation]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/transfer-pricing-documentation/obligation-to-compile-a-transfer-pricing-documentation/
[detailed]: https://www.vero.fi/en/detailed-guidance/guidance/47978/transfer-pricing-documentation/
[form]: https://www.vero.fi/en/About-us/contact-us/forms/filling-instructions/78-explanation-of-transfer-prices-how-to-fill-out-the-form/
[faq]: https://www.vero.fi/en/businesses-and-corporations/business-operations/foreign-business-in-finland/supporting-high-growth-companies-with-international-tax-questions/faq---transfer-pricing/faq/when-does-a-company-need-to-maintain-and-submit-transfer-pricing-documentation-in-finland/
