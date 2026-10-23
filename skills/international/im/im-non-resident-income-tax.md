---
name: im-non-resident-income-tax
description: >
  Prepare Isle of Man non-resident individual income-tax workpapers for
  2026/27: distinguish taxable and exempt source income, apply the published
  rate, reconcile payer deductions, and identify returns and pension-relief
  applications. Residence, treaty entitlement and full statutory review remain open.
jurisdiction: IM
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
---

# Isle of Man non-resident individual income tax v0.1

## Who this applies to

This draft addresses individuals already established to be non-resident who receive Isle of Man income, and the people making taxable payments to them. It does not determine residence, company taxation, permanent establishments or National Insurance. The period is **6 April 2026 to 5 April 2027**, not calendar 2026. [Government rates table][rates]

The government identifies rents and occupational/private pensions as examples of continuing taxable Manx-source income after departure. It identifies Manx bank/building-society interest, dividends and the Manx State Pension as non-taxable to non-residents. Classify the actual income before applying the rate; do not treat every payment from a Manx account as taxable, or every payment called interest as exempt. [Leaving the Island][leaving]

This is a source-cited draft using tax-authority guidance read on 23 October 2026. Several pages were available through the search index but rejected direct browser retrieval. Statutory cross-checks, complete income-category exceptions, treaty entitlement and independent review remain outstanding.

## Rates, bands and thresholds

| Item | 2026/27 rule |
|---|---|
| Published non-resident individual income-tax rate | 21% |
| Non-resident personal allowance | GBP 0 |
| Tax year | 6 April to 5 April |

[Government rates table][rates]. The historical table also gives 21% for 2025/26. Do not reuse the former 20% rate or apply resident allowances and the resident standard-rate band to a full-year non-resident calculation. The 2026 budget confirms the 21% rate for taxable income of non-resident individuals and non-corporate entities. [Budget 2026][budget]

## The base and the recipient's return

Separate taxable source income, exempt income, any treaty-relieved income and payer deductions. Establish allowable expenses and taxable profit before calculating final liability; tax withheld from a gross payment does not by itself establish the final taxable base.

The government's non-resident guidance says returns are issued on 6 April for the year ended the previous day and are due by the following **6 October**. It states a GBP 100 penalty for missing that deadline. For 2026/27, that means a return issued on 6 April 2027 and due on 6 October 2027 under the published rule. Further penalties, payment deadlines and individual notices require separate checking. [Receiving Manx-source income][receiving]

That page warns that its linked 2006 practice note contains historical rates and allowances. Use the relevant year's rates table. It also states that non-resident couples cannot elect joint taxation; each accounts for their own income. Part-year arrival/departure cases require separate apportionment and residence work, rather than this full-year illustration. [Receiving Manx-source income][receiving]

## Payer deductions and records

The tax authority's payment guidance describes deduction at the prescribed higher rate and these documents. Apply it to a payment established to be within the deduction obligation; the listed income exemptions and any authorised relief still matter. [Making payments][payments]

| Document | Purpose |
|---|---|
| N15 | Authority's instruction to deduct from future payments |
| N13 | Recipient certificate recording gross payment, deduction and net payment |
| N20 | Estate agent registration of a new non-resident landlord's property |
| N35 | Remittance card sent with tax within 14 days of making the payment |
| N37 | Year-end payer return recording payments |
| R221 | Application for treaty relief or repayment on qualifying Manx pension income |

[Making payments][payments]. Reconcile certificates and remittances to the payer ledger and the recipient's return. A deduction notice or treaty-relief application must be examined for its actual recipient, payment and effective period. No electronic submission route or holiday extension has been verified here.

## Employment performed on and off the Island

Government employer guidance directs use of code **HR** for a non-resident employee with no personal allowance. For duties wholly outside the Island, it requires prior Income Tax Division clearance before omitting deductions. For duties partly performed on the Island, it directs HR deductions on the whole remuneration. Do not unilaterally prorate payroll withholding using a day-count spreadsheet; resolve any relief through the applicable clearance or assessment procedure. [Non-resident employees][employment]

This is an employer withholding instruction, not a conclusion that every payment is ultimately taxable in full regardless of a treaty. Final relief, residence, workdays, employer identity and treaty conditions remain case-specific checks.

## Treaty and pension relief

R221 is the authority's route described for residents of a treaty jurisdiction whose agreement provides relevant pension relief. A foreign address alone is insufficient. Verify the actual agreement, income article, residence evidence and relief decision before treating a pension as exempt. [Making payments][payments]

For the UK corridor, HMRC lists the 2018 agreement as in force and the previous 1955 arrangement as terminated. Its collection includes later exchange-of-letters and memorandum material. This draft does not provide a treaty-rate table or conclude that a particular pension qualifies; use the applicable current text and related instruments. [HMRC treaty collection][uk]

## Worked examples

### 1. Full-year non-resident taxable income

Assume GBP 18,000 is the correctly determined taxable income after category, expense and treaty review, the individual is non-resident throughout 2026/27, and there is no other relief. At 21%, liability before credits is GBP 3,780. This is not a calculation of allowable rental expenses from gross rent.

```oa-check
name: Isle of Man 2026 non-resident taxable income
inputs:
  established_taxable_income: 18000
  applicable_rate: 0.21
steps:
  liability_before_credits: established_taxable_income * applicable_rate
expected:
  liability_before_credits: 3780
```

### 2. Payer deduction and cash reconciliation

Assume an N15-covered GBP 2,000 payment to a non-resident individual in 2026/27, subject to the published 21% rate, with no authorised exemption or net-of-tax promise. Deduct GBP 420 and pay GBP 1,580 to the recipient. Record both on the certificate and track remittance separately. This cash split does not settle the recipient's annual liability.

```oa-check
name: Isle of Man non-resident payer cash split
inputs:
  gross_payment: 2000
  deduction_rate: 0.21
steps:
  withheld_tax: gross_payment * deduction_rate
  recipient_cash: gross_payment - withheld_tax
  reconciled_payment: withheld_tax + recipient_cash
expected:
  withheld_tax: 420
  recipient_cash: 1580
  reconciled_payment: 2000
```

## Ask the client first

- What establishes non-residence, and on what dates did residence change?
- Which income categories, gross amounts, expenses and ownership shares are involved?
- What N15 instructions, certificates, remittance records and returns exist?
- Where were employment duties performed, and is written clearance available?
- What treaty residence and pension-relief evidence supports the claimed treatment?

## Sources and review limits

Read 23 October 2026. The rates, budget, receiving-income, departure and employment guidance were retrieved in indexed official-source text; attempted direct opens of several returned rejection/cache errors. The payer guidance opened successfully. No independent review, professional attestation or full statutory verification is claimed.

- [Current and historical rates][rates]; [Budget 2026][budget].
- [Receiving Manx-source income][receiving]; [Leaving the Island][leaving].
- [Making payments to non-residents][payments]; [Non-resident employees][employment].
- [HMRC Isle of Man treaty collection][uk].

Not yet confirmed: residence tests, statutory amendment chain, detailed deductions, additional sanctions and payment deadlines, live forms, treaty-by-treaty entitlement, company/PE rules, foreign-tax credits and wider reporting. Cross-border country coverage remains partial. Existing corporate withholding summaries must not be used to infer individual treatment.

[rates]: https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/rates-and-allowances?iomg-device=Mobile
[budget]: https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/budget/
[receiving]: https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/non-residents/receiving-isle-of-man-source-income/
[leaving]: https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/residents/leaving-the-island?iomg-device=Mobile
[payments]: https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/non-residents/making-payments-to-non-residents?iomg-device=Mobile
[employment]: https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/employers/further-information-for-employers/non-resident-employees/?iomg-device=Mobile
[uk]: https://www.gov.uk/government/publications/isle-of-man-tax-treaties
