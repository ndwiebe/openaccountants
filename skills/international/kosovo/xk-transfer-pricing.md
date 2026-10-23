---
name: xk-transfer-pricing
description: >
  Prepare Kosovo controlled-transaction pricing workpapers: identify related
  parties, select a supported market-value method, distinguish documentation
  from annual cross-border notification and assess corresponding-adjustment
  requests. Use for intercompany goods, services and financing. Detailed
  instruction reconciliation, current submission procedures and independent
  review remain outstanding.
jurisdiction: XK
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.2
---

# Kosovo transfer pricing v0.2

## Who this applies to

A corporate taxpayer participating in controlled transactions must determine taxable profit using the open-market principle. Article 3(1.18) defines related persons through multiple relationships: officers/directors, business partners, employment, ownership/control of at least 50% of shares or votes, direct or indirect control, common control, specified family relationships and membership of the same multinational group. The percentage test is one route, not a universal exclusion for holdings below 50%. [Law 06/L-105, Articles 3 and 28][law]

This source-cited draft uses the official English statute and the tax authority's notice for 2025 transactions filed in 2026. Administrative Instruction 02/2017 predates that statute and refers to its predecessor. The authority still cites it in the 2026 filing notice, but a complete article-by-article reconciliation and amendment audit remain open. Do not apply an older instruction provision over inconsistent later law.

## Rates, bands and thresholds

| Test | Rule | Source |
|---|---|---|
| Share/voting relationship route | 50% or more; other relationship routes also apply | [Article 3(1.18)][law] |
| Market-pricing obligation | Corporate taxpayers participating in controlled transactions | [Article 28(1)][law] |
| Documentation | All taxpayers with controlled transactions must prepare it; submit on TAK request | [Article 28(5)][law] |
| Annual cross-border controlled-transaction notification | The current notice addresses related parties in different tax jurisdictions whose reporting-period total exceeds EUR 300,000 | [TAK notice][notice] |

The notification threshold is not a tax rate, pricing safe harbour or blanket documentation exemption. Exactly EUR 300,000 does not exceed the threshold stated in that notice; verify aggregation and transaction classification before using the boundary. Specific-jurisdiction rules, valuation of loan balances and any simplified documentation treatment require the instruction/form review still outstanding.

## The base

Article 28 allows taxable profit to include profit that would have arisen between independent enterprises but did not arise because of the controlled terms. Reconcile the supported value to the booked transaction and resulting profit adjustment. Preserve contracts, invoices, transaction dates, counterparty identity/residence and the relationship evidence. [Article 28(1)–(2)][law]

The statute lists comparable uncontrolled price, resale price and cost-plus methods, and permits transactional net margin and profit split in the specified circumstances. Its selection criteria address method strengths/weaknesses, transaction nature and functions/assets/risks, reliable information and comparability including reliable adjustments. Explain the selected method and rejected alternatives against those criteria; a group policy or invoice label is not the analysis. [Article 28(3)–(4)][law]

A practical workpaper should connect the transaction description, functional analysis, comparable evidence, adjustments, selected result and ledger reconciliation. These are preparation steps supporting the statutory requirements, not a claim that this draft supplies a complete local-file checklist or a prescribed markup. The instruction-based checklist below develops documentation content; amendment reconciliation and adjustment-range rules remain open before an audit response.

### Documentation file under Instruction 02/2017

Article 29(6) identifies the following components. Tie each to the taxpayer and actual controlled transactions rather than providing an unadapted group report:

- Business history, market trends and business-unit/department structure.
- Group members, legal forms, ownership percentages, operating structure and each relevant member's role.
- Controlled transactions, comparability factors and relevant pricing policies.
- Selection of the most appropriate method and financial indicator where needed.
- Comparable search, reasons for rejecting potential internal comparables, comparability analysis and explanations of adjustments.
- Economic analysis and supporting work, applicable foreign advance-pricing or similar arrangements, and the conclusion on market compliance including adjustments.
- Other information materially relevant to compliance.

[Instruction, Article 29(6)][instruction]. Preparing the file does not prevent TAK from adjusting a transaction whose terms are not at market value. Incomplete, inaccurate or non-objective material does not satisfy the documentation requirement. [Article 29(5), (12)][instruction]

Article 29(3) of the retrieved instruction requires availability within **30 days after receipt of TAK's request**. Record the actual receipt and requested scope, and check the applicable current procedure before calculating the response date. The instruction's penalty cross-reference is to the older Law 03/L-222; this draft does not import that historical penalty as current law. [Article 29(3)–(4)][instruction]

Where business operating conditions remain unchanged, the instruction distinguishes a database/comparable search refreshed every **three years** from comparable financial-indicator information refreshed **annually**. Do not treat an old search as permission to leave annual financial information unchanged, or continue it after material changes without reassessment. [Article 29(8)–(10)][instruction]

The instruction calls for an official Kosovo language and allows English in special cases, electronically or physically. Confirm acceptance for the actual request rather than assume any English-only group file will be accepted. [Article 29(11)][instruction]

Article 29(8)'s below-EUR-300,000 documentation wording requires reconciliation with the newer law's general preparation duty. No blanket exemption is asserted here, and the notification threshold must not be used to erase the pricing evidence. This checklist is sourced to the retrieved instruction; a complete current amendment/procedure audit remains outstanding.

## Deadlines and filing

Prepare the documentation under Article 28(5); submit it when TAK requests it. Do not confuse a completed annual notification with a completed documentation file. [Article 28(5)][law]

TAK's notice expressly sets **31 March 2026** for notification of **tax-year 2025** qualifying controlled transactions. It describes the notification as an information statement and cites Instruction 02/2017. That is a confirmed historical filing date, not confirmation of a newly issued 2026-year filing notice. The 2026 reporting deadline, current submission route and actual approved form must be verified before filing. [TAK notice][notice]

Retain the reconciliation of annual transaction totals, the submitted statement, acknowledgement and any documentation request and response. No filing or current electronic-form validation was performed for this draft.

## Penalties and interest

Unsupported pricing exposes taxable profit to adjustment under Article 28. This draft does not quote a current penalty or interest rate. The instruction-based response period above still needs checking against current tax-administration legislation and the applicable request. The notification's information-statement classification must be considered when reviewing enforcement rules. [Article 28][law]; [TAK notice][notice]

## Cross-border points

Where another country's adjustment taxes profit already taxed in Kosovo, Article 28(6) provides for TAK to examine the adjustment's compliance with open-market value on the Kosovo taxpayer's request where the other country has a double-taxation agreement with Kosovo. Relief is not automatic merely because the foreign assessment exists. Obtain the assessment, affected transaction/year, evidence of double taxation, applicable agreement and pricing analysis. Treaty-specific procedures and time limits remain unverified. [Article 28(6)][law]

Keep source withholding, permanent establishments and foreign-tax credits separate from transaction pricing. See the [corporate-tax draft](xk-corporate-income-tax.md) for its stated boundaries; neither Guide completes the cross-border domain.

## Worked examples that recompute

### 1. Comparable-price reconciliation

Assume 1,000 identical units sold to a related party for EUR 80 each. A reliable independent comparison, already adjusted for all relevant differences, supports EUR 95. Supported revenue is EUR 95,000 versus EUR 80,000 booked, a EUR 15,000 increase. The comparison is a fact assumption requiring evidence, not a price established by this Guide.

```oa-check
name: Kosovo controlled goods price reconciliation
inputs:
  units: 1000
  booked_unit_price: 80
  supported_unit_price: 95
steps:
  booked_revenue: units * booked_unit_price
  supported_revenue: units * supported_unit_price
  revenue_adjustment: supported_revenue - booked_revenue
expected:
  booked_revenue: 80000
  supported_revenue: 95000
  revenue_adjustment: 15000
```

### 2. Notification total versus documentation duty

Assume two qualifying cross-border controlled-transaction categories in tax year 2025: goods EUR 210,000 and services EUR 100,000, with no double counting, loans or disputed classification. Total EUR 310,000 exceeds the notice's threshold by EUR 10,000, so the stated 2025 notification applies. A below-threshold total would not remove Article 28(5)'s documentation obligation.

```oa-check
name: Kosovo controlled transaction notification aggregation
inputs:
  goods: 210000
  services: 100000
  notification_threshold: 300000
steps:
  transaction_total: goods + services
  excess_over_threshold: transaction_total - notification_threshold
expected:
  transaction_total: 310000
  excess_over_threshold: 10000
```

## Ask the client first

- Which parties are related under each ownership, control, management or family test?
- What transactions and balances exist, with which jurisdictions, and how do they reconcile to the accounts?
- What functions, assets and risks support the selected pricing method and comparables?
- Has TAK requested documentation, and what precisely does the request require?
- Was the annual notification submitted, and is the acknowledgement available?
- Is there a foreign adjustment, double taxation or treaty procedure involved?

## Sources and review limits

Read 23 October 2026. Independent source review and professional attestation remain outstanding. The full instruction/amendment chain, specified-jurisdiction and simplified-documentation rules, current enforcement, electronic form and treaty procedures remain open. This is not comprehensive TP or country coverage.

- [Law 06/L-105, official English PDF][law], Articles 3(1.18), 28.
- [TAK notification notice for tax year 2025][notice], identified in the current search index; direct browser retrieval returned HTTP 502.
- [Instruction 02/2017, Gazette text][instruction], retrieved as the implementation source requiring further detailed reconciliation.

[law]: https://www.atk-ks.org/wp-content/uploads/2019/09/LAW_NO.06_L-105.pdf
[notice]: https://www.atk-ks.org/njoftim-per-tatimpagues-raporto-transaksionet-e-kontrolluara-2/
[instruction]: https://gzk.rks-gov.net/ActDocumentDetail.aspx?ActID=14937
