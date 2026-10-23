---
name: no-transfer-pricing
description: >
  Screen Norwegian controlled-transaction reporting and transfer-pricing
  documentation, distinguish size exemptions and prepare method-selection
  evidence. Current statutory scope, special exceptions and independent
  review remain outstanding.
jurisdiction: "NO"
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
---

# Norway transfer-pricing preparation v0.1

## Who this applies to

Use this draft for corporate controlled transactions and balances involving Norway, including foreign-enterprise screening. Confirm the statutory related-party definition and PE scope before applying the tests below. A foreign address or a small standalone Norwegian entity does not resolve the compliance position.

The foreign-company guidance describes reporting where combined fair-value controlled transactions reach **NOK 10 million**, or combined receivables, debts and guarantees reach **NOK 25 million at period end**. Equality meets either stated threshold. [Foreign-company guidance][screen]

## Documentation size test

The same guidance describes an exemption for entities that, together with associates, have fewer than 250 employees and either sales no greater than NOK 400 million or balance sheet no greater than NOK 350 million. It excludes dealings with entities in jurisdictions from which Norway cannot demand tax information. [Foreign-company guidance][screen]

This exemption is distinct from the transaction/balance reporting thresholds. Its complete scope, including petroleum-tax and other special cases, requires current statutory reconciliation. Do not infer that an exemption from this documentation obligation establishes acceptable pricing, removes other information duties or exempts the tax return.

The size tests involve associates; do not compare only the Norwegian entity's accounts. Preserve the ownership structure and the figures used for each condition. No universal ownership percentage or small-transaction safe harbour is established by this draft.

## Requests and retention

The current Tax Administration handbook reproduces section 8-11(2): documentation must support evaluation against independent-party conditions, be supplied within **45 days of request**, and be retained for **at least ten years after the tax period ends**. [Current handbook][handbook]

Its regulatory discussion requires information and analysis proportionate to transaction value, complexity and the authority's evaluation needs. A prescribed sequence of headings is not required; extensive files need a summary. A general group document must still support the actual transaction. [Current handbook][handbook]

Calendar the actual request, preserve receipt/submission evidence and reconcile the requested material to the relevant period. This draft has not verified extensions, current language requirements, penalties or live submission channels.

## Pricing workpaper and method

The authority's method guidance starts with the delineated transaction, functions/assets/risks and available comparables. It lists CUP, resale price, cost plus, TNMM and profit split. It distinguishes unilateral tested-party methods from profit split, which examines both parties. The choice depends on the evidence; the list does not prescribe a margin. [Method guidance][method]

Other methods require a verifiable process/result and an explanation of why the standard methods are unsuitable. A range does not automatically justify selecting its median: the quality of comparability and the circumstances matter. [Method guidance][method]

As a practical preparation framework:

- Identify parties, relationships, residences, periods and transaction categories.
- Reconcile contracts, invoices and year-end balances to the accounts, including guarantees.
- Describe actual conduct and functions, assets and risks.
- Record comparable searches, adjustments, method choice and rejected alternatives.
- Connect the supported result to the booked amount and tax computation.
- Keep reporting, documentation, requests and foreign adjustments in one reconciliation.

This checklist does not claim to reproduce every statutory documentation item. Financing, services, intangibles, restructurings and PE attribution require transaction-specific work.

## Worked example

Assume two qualifying controlled-transaction categories have established fair values of NOK 6 million and NOK 4 million. Their NOK 10 million total meets the reporting screen. This assumes classification and aggregation are correct; it does not establish documentation liability or a tax adjustment.

```oa-check
name: Norway assumed controlled transaction reporting boundary
inputs:
  goods_fair_value: 6000000
  services_fair_value: 4000000
  reporting_threshold: 10000000
steps:
  combined_fair_value: goods_fair_value + services_fair_value
  excess_over_threshold: combined_fair_value - reporting_threshold
expected:
  combined_fair_value: 10000000
  excess_over_threshold: 0
```

## Ask the client first

- What relationships, residences, transactions and PE dealings exist?
- Which balances, guarantees and fair values reconcile to the accounts?
- What associate-level employee, sales and asset figures support the size screen?
- Which jurisdictions and special tax regimes affect the exemption?
- What pricing evidence, requests, filings and foreign adjustments exist?

## Sources and review limits

Read 23 October 2026 through indexed official text:

- [Foreign-company reporting/documentation guidance][screen].
- [Current handbook, section 8-11(2)][handbook].
- [Method-selection guidance][method], published 28 October 2025.

Not yet confirmed: complete current statute and regulations, related-party/PE definition, reporting form and deadline, petroleum and other exemption exceptions, language, full documentation contents, sanctions, CbCR, treaty relief and live filing. Independent review and professional attestation remain outstanding. Norway's TP and country coverage remain partial. Retired guidance and historical handbook editions must not substitute for current law.

[screen]: https://www.skatteetaten.no/en/business-and-organisation/foreign/tax-returns-and-tax-assessment-notices/transfer-pricing/
[handbook]: https://www.skatteetaten.no/en/rettskilder/type/handboker/skatteforvaltningshandboken/gjeldende/kapittel-8-opplysningsplikt-for-skattepliktige-trekkpliktige-mv/ID-8-11.001/ID-8-11.009/
[method]: https://www.skatteetaten.no/en/business-and-organisation/tax-for-businesses/tax-return/deductions/foreign-large-companies-and-groups/transfer-pricing/specific-transfer-pricing-topics/how-to-conduct-a-comparability-analysis/comparability-and-pricing/select-method/
