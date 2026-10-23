---
name: ad-non-resident-income-tax
description: >
  Assess Andorran-source income of non-residents under IRNR: distinguish a
  permanent establishment from separate income payments, classify services,
  royalties and rent, test statutory exemptions and treaty relief, calculate
  ordinary withholding and identify quarterly reporting obligations. Use for
  payments to overseas suppliers and non-resident landlords. Property sales,
  treaty-specific rates and full PE computations require separate work.
jurisdiction: AD
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
---

# Andorra non-resident income tax v0.1

## Who this applies to

IRNR applies to non-resident individuals and entities receiving income treated as arising in Andorra. Establish residence first under the referenced individual or corporate residence rules; a foreign address alone does not determine the answer. Treaties that form part of Andorran law can override domestic treatment. [Law 94/2010, Articles 1, 3–4][law]

This draft uses the legal portal's current consolidated law and regulation. Both are expressly labelled consolidations without official legal status. The law's status sheet identifies the fifth consolidation with effect from 17 April 2025 and warns that entry into force and tax application dates can differ. Retain the applicable period and check the underlying enactments for a disputed or transitional case. [Status sheet][status]

### Source and permanent-establishment checks

Income from activities in Andorra, assets there or rights exercisable or usable there is within the source rules. For payments by Andorran companies or resident businesspeople, the exception for services or rights contracted, performed **and** used outside Andorra requires all three elements. An overseas supplier performing remotely is not automatically outside IRNR. International merchandise purchases and associated mediation commissions/accessory costs have a separate source exclusion. [Articles 9, 14(6)–(7)][law]

A continuous or habitual fixed business location can constitute a permanent establishment (PE). Article 11 includes branches, offices and other listed sites, construction/installation/assembly exceeding twelve months, and habitual exercise of contracting powers by a dependent agent. Review the listed storage, purchasing and preparatory/auxiliary exceptions and the independent-agent rule against the facts. Common ownership alone does not create a PE. Rental income from immovable property is expressly treated separately under the non-PE chapter. [Article 11][law]

A PE is taxed on attributable income wherever obtained, rather than separately on each receipt. It requires separate accounts, registration and ordinarily an Andorran-resident representative. Appointment must be communicated within one month; ministry-required appointments have their own one-month notification rule. The detailed PE base, credits and advance payments need the corporate-tax rules as well as IRNR. [Articles 6, 10, 16–24][law]

## Rates, bands and thresholds

These are domestic rules for non-PE income before any applicable treaty relief.

| Item | Rule | Source |
|---|---|---|
| Ordinary taxable income, including taxable service fees | 10% | [Article 29(a)][law] |
| Royalties within the statutory definition | 5% | [Articles 14(2), 29(c)][law] |
| Reinsurance premiums | 1.5% | [Articles 25(3), 29(b)][law] |
| Immovable-property rental income | Base reduced by 20%, then ordinary 10% rate | [Articles 25(2), 29(a)][law] |
| Dividends, interest and other Article 13 movable-capital income | Exempt under Article 15(b), subject to correct classification | [Articles 13, 15(b)][law] |

The royalty definition includes specified intellectual-property rights, software rights, know-how, equipment use and image rights. Determine what is licensed rather than relying on an invoice label. Property-sale gains have separate base, holding-period rates and buyer withholding rules: the rental calculation above must not be used for a sale. [Articles 14(2), 28 bis, 29(d)–(f), 35(5)][law]

## The base

Without a PE, calculate tax separately for each taxable accrual; do not offset one income stream against another. The ordinary base is the full accrued income, with the specific property-income reduction and capital-gain rules kept separate. This is not a general profit-after-expenses calculation. Related-party transactions are referred to the corporate-tax related-party rules. [Articles 16, 25–28][law]

For each payment record the recipient, residence evidence, contract, service/use locations, accrual/payment dates, income category, gross amount, exemption or treaty basis, tax calculation and certificate. A statutory exemption does not imply every reporting obligation disappears: Articles 33 and 35 specify particular exemptions from declarations. [Articles 33–35][law]

## Deadlines and filing

Ordinary income accrues when due or, if earlier, when collected. Capital gains accrue on the disposal or other relevant alteration. [Article 32][law]

A non-PE taxpayer's ordinary declaration/payment falls during the month after each calendar quarter: April, July, October and January. Invoices or equivalent documents and the income schedule accompany it. The regulation removes the taxpayer's declaration obligation when the withholding party has declared and paid in accordance with the rules; keep evidence of that performance. [Regulation, Article 22][reg]

The withholding party generally declares and pays during the month after the quarter. Article 24(1) also permits amounts relating to income accrued in the quarter's final month to be declared in the following quarter's settlement period. Do not treat that limited provision as an automatic extension for every payment. Employment income subject to the specified CASS rules instead has monthly reporting/payment between days 1 and 15 of the following month. [Regulation, Article 24][reg]

Retain the withholding records and issue the certificate. The regulation requires communicating the quarter's withholding to the taxpayer during the first 30 calendar days of April, July, October and January. Identify the current approved form before filing; this draft does not certify a live form number or electronic submission. Property sales follow their separate settlement timetable. [Law, Article 35][law]; [Regulation, Articles 22–29][reg]

## Penalties and interest

This draft does not quote a monetary penalty or interest rate: current application of the general tax-procedure legislation and the IRNR enforcement provisions needs a separate review. A payer's duty to remit is distinct from withholding from the recipient, and statutory payer/representative liability must be considered. Retain evidence of actual payment, not only an invoice showing tax deducted. [Articles 5, 35(2), 37–40][law]

## Cross-border points

Before applying treaty relief, verify that the treaty is in force and applicable to the period, the recipient qualifies, the income article and PE position, and the required residence/relief evidence. No treaty-specific rate is supplied here. Article 35 excludes withholding for qualifying domestic or treaty-exempt income; Article 36 permits reclaiming excessive withholding, including amounts above a treaty limit. Do not equate a domestic exemption with a treaty claim. [Articles 3, 35–36][law]

Ordinary non-resident employees, frontier/seasonal-worker elections, PE deductions and cessation, property transfers and related-party documentation require separate work. The presence of this Guide does not complete the cross-border domain.

## Worked examples that recompute

### 1. Separate taxable service and royalty payments

Assume no PE, no treaty relief, a EUR 12,000 taxable service fee and a separate EUR 8,000 royalty meeting Article 14(2). The contracts state gross amounts. Tax is EUR 1,200 and EUR 400 respectively. Combined remittance is EUR 1,600, with EUR 18,400 paid to recipients. Classification and source are assumptions to verify, not conclusions produced by the calculation.

```oa-check
name: Andorra separate service and royalty withholding
inputs:
  service: 12000
  royalty: 8000
  service_rate: 0.10
  royalty_rate: 0.05
steps:
  service_tax: service * service_rate
  royalty_tax: royalty * royalty_rate
  tax_total: service_tax + royalty_tax
  net_total: service + royalty - tax_total
expected:
  service_tax: 1200
  royalty_tax: 400
  tax_total: 1600
  net_total: 18400
```

### 2. Non-resident landlord's ordinary rent

Assume EUR 15,000 of Andorran immovable-property rent, no treaty override, no sale and no other special treatment. Article 25(2)'s reduction is EUR 3,000; the base is EUR 12,000 and tax EUR 1,200. Actual expenses are not additionally deducted in this example.

```oa-check
name: Andorra non-resident rental income base
inputs:
  gross_rent: 15000
  base_reduction_rate: 0.20
  tax_rate: 0.10
steps:
  reduction: gross_rent * base_reduction_rate
  taxable_base: gross_rent - reduction
  tax: taxable_base * tax_rate
expected:
  reduction: 3000
  taxable_base: 12000
  tax: 1200
```

## Ask the client first

- Who receives the payment, and what establishes their tax residence?
- Where was the service contracted, performed and used?
- What premises, agents, contracting powers or project duration exist in Andorra?
- Is the payment a service, licensed right, dividend, interest, rent or disposal proceeds?
- Is the contract gross or net of tax, and when did the amount become due or get paid?
- What treaty and exemption evidence exists, and who has actually declared and remitted?

## Sources and review limits

Read 23 October 2026. Source-cited draft; independent source review and professional attestation remain outstanding. Full treaty, property-sale, PE and enforcement coverage is not claimed.

- [Law 94/2010, current portal consolidation][law].
- [Law version and amendment status][status].
- [IRNR regulation approved 29 December 2023, current portal consolidation][reg], including listed amendments through Decree 412/2025.

[law]: https://www.portaljuridicandorra.ad/L2010094
[status]: https://www.portaljuridicandorra.ad/L2010094_F
[reg]: https://portaljuridicandorra.ad/R20231229B
