---
name: ye-individual-income-tax-and-payroll
description: >
  Yemen source-cited individual income-tax and payroll draft based on selected provisions of Law 17/2010. Covers residence, annual resident bands, non-resident employment rate, income exclusions, employer withholding and employee obligations. Later amendments and administration-specific application remain unresolved, including the Sana'a-issued 2020 small-business employee exemption. Two annual computations do not establish a validated monthly payroll engine.
jurisdiction: YE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://agoyemen.net/lib_details.php?id=198"
    title: "Public Prosecution: Law 17/2010, articles 3, 40, 48–50, 62–63 and 98–102"
    as_of: "2026-10-22"
  - url: "https://tax.gov.ye/8-2021/"
    title: "Tax and Customs Authority: Sana'a-issued Law 8/2020, article 160(c)"
    as_of: "2026-10-22"
---

# Yemen: individual income tax and payroll withholding

## Scope and residence

This is a translation of selected provisions of the 2010 law, not a certified current nationwide schedule. Establish the administering office, business/work location, period and applicable amendments first. Current territorial application and the complete amendment chain remain unresolved. [Law 17/2010](https://agoyemen.net/lib_details.php?id=198).

Article 3 treats a natural person as resident if they have a permanent residence in Yemen; or, without such a permanent residence, spend at least **183 days**, continuously or intermittently, in a twelve-month period ending in the tax year; or are a Yemeni working abroad receiving employment income from Yemen. Do not substitute a calendar-year-only day count or assume nationality alone determines residence. Treaty residence, day-count detail and administrative evidence remain separate work. [Article 3](https://agoyemen.net/lib_details.php?id=198).

## Employment income and exclusions

Article 48 includes cash/in-kind employment benefits regardless of label or written contract, including Yemen-source payments for work inside or outside Yemen and foreign-source payments for work performed in Yemen. Directors' remuneration falls within the specified categories. This does not mean every foreign transfer is employment income. [Article 48](https://agoyemen.net/lib_details.php?id=198).

Article 49 excludes amounts prescribed for pension contributions under the applicable laws and regulations and job-related expense allowances within the implementing regulation's limits and criteria. A payroll label such as “travel allowance” is not sufficient evidence. Article 50 includes specific exemptions for pensions/end-of-service entitlements and compensation for work accidents and occupational injuries under the applicable rules; diplomatic and international-organisation cases have their own conditions. Daily-wage income also depends on regulatory criteria. The complete regulations and exemption eligibility have not been verified here. No social-contribution percentage is inferred from these income-tax provisions. [Articles 49–50](https://agoyemen.net/lib_details.php?id=198).

## Annual resident bands and non-resident wages

Article 62 sets the annual resident schedule: **YER120,000 exempt; the next YER120,000 at 10%; the next YER600,000 at 15%; excess above YER840,000 at 20%**. Apply it to the established income within its scope after the relevant exclusions, retaining the exemption band once. Article 63(f) separately sets **20%** on non-resident employment income. Do not give a non-resident the resident exemption by default. [Articles 62–63](https://agoyemen.net/lib_details.php?id=198).

The examples below test annual statutory arithmetic only. Monthly apportionment, service-period attribution, arrears, bonuses, part-year work and multiple employments require the implementing rules; dividing an annual result by twelve is not verified as a complete payroll method.

## Withholding, return and payment

Article 99 requires monthly withholding by the employer when income is paid, with regard to the period to which the income relates based on the month of service. Other income/entitlements are withheld on payment and included in the monthly return. Under article 100 the employer must remit even if it failed to deduct from the employee. [Articles 99–100](https://agoyemen.net/lib_details.php?id=198).

Article 101(a) requires the return and payment within the **first ten days of each month for the preceding month**. Article 101(b) makes an employee working simultaneously for multiple employers personally responsible for tax differences within that same period, without removing each employer's withholding duty. Article 102 puts remittance on the recipient where the employer/payer is non-resident or lacks a centre or establishment in Yemen, under implementing procedures. Remote work does not automatically remove the recipient's obligation. [Articles 101–102](https://agoyemen.net/lib_details.php?id=198).

Article 40's original small-enterprise payroll rule instead uses a quarterly return/payment within the first ten days of the fourth month. Determine classification and amendments before choosing this exception. The Sana'a-issued Law 8/2020 adds article 160(c), including an employee exemption for specified small/micro enterprises. Its full eligibility and administration-specific application must be reconciled before using either the old quarterly rule or the later exemption. This Guide applies neither automatically. [Article 40](https://agoyemen.net/lib_details.php?id=198); [Law 8/2020](https://tax.gov.ye/8-2021/).

## Example 1: resident band boundaries

Assume the resident annual schedule governs, all relevant exclusions have already been determined, and no separate exemption applies. At YER120,000 the annual tax is zero. At YER840,000, tax is YER12,000 plus YER90,000, totalling YER102,000. The top 20% band has not yet started.

```oa-check
name: Yemen annual resident exemption and upper band boundary
inputs:
  exempt_amount: 120000
  first_taxed_band: 120000
  first_rate: 0.10
  second_taxed_band: 600000
  second_rate: 0.15
steps:
  - tax_at_exemption: exempt_amount * 0
  - tax_at_840000: first_taxed_band * first_rate + second_taxed_band * second_rate
expected:
  tax_at_exemption: 0
  tax_at_840000: 102000
```

## Example 2: resident versus non-resident employment income

Assume YER1,200,000 employment income after relevant exclusions, with the respective statutory regimes independently established and no further relief. The resident annual result is YER102,000 plus 20% of YER360,000: YER174,000. At the non-resident 20% employment rate the result is YER240,000. This comparison does not decide a person's residence or prove the current rule in any particular administration.

```oa-check
name: Yemen annual resident and nonresident employment comparison
inputs:
  income: 1200000
  resident_threshold: 840000
  resident_tax_at_threshold: 102000
  top_rate: 0.20
  nonresident_rate: 0.20
steps:
  - resident_tax: resident_tax_at_threshold + (income - resident_threshold) * top_rate
  - nonresident_tax: income * nonresident_rate
expected:
  resident_tax: 174000
  nonresident_tax: 240000
```

## Intake and outstanding work

Obtain residence/home evidence, travel dates, nationality where relevant, work locations, employer residence/establishment, payment and service dates, simultaneous employers, gross cash/in-kind pay, deductions and supporting documents, and employer classification. Still open: current amendments by administration, monthly payroll tables/methods, benefit valuation, regulatory allowance limits, small-enterprise exemption eligibility, social contributions, operational forms/payment channels, reconciliation, corrections and penalties. No comprehensive individual or payroll coverage or professional attestation is claimed.

## Sources

- [Public Prosecution, Law 17/2010](https://agoyemen.net/lib_details.php?id=198), articles cited above, retrieved 22 October 2026. Arabic controls over this translation.
- [Tax and Customs Authority, Law 8/2020](https://tax.gov.ye/8-2021/), retrieved 22 October 2026. Application outside the issuing administration has not been established.

## Disclaimer

Source-cited research draft. Confirm governing law, administration, facts and procedures before running payroll or filing.
