---
name: iceland-payroll
description: Use this skill whenever asked about Iceland payroll processing for employed persons. Trigger on phrases like "Iceland payroll", "Icelandic payroll", "staðgreiðsla", "PAYE Iceland", "withholding Iceland", "tryggingagjald", "social security contribution Iceland", "persónuafsláttur", "personal tax credit Iceland", "lífeyrissjóður", "mandatory pension Iceland", "séreignarsparnaður", "supplementary pension", "launagreiðendaskrá", "employer registry Iceland", "RSK 5.02", "launamiði", "skilagreining", "net salary Iceland", "tax withholding Iceland", "employer social cost Iceland", "kjarasamningur", "minimum wage Iceland", "municipal income tax Iceland", "gross to net Iceland", "salary calculation Iceland", or any question about computing employee pay, withholding income tax (state + municipal), or social contributions for Iceland-based employees. This skill covers PAYE (staðgreiðsla) income tax withholding, the personal tax credit, employer social security contribution (tryggingagjald), mandatory occupational pension (employee 4% + employer 11.5%), supplementary private pension, no statutory minimum wage (collective-agreement minimums), and filing obligations to Skatturinn. ALWAYS read this skill before processing any Iceland payroll.
version: 0.3
jurisdiction: IS
tax_year: 2026
last_updated: 2026-10-23
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland payroll: employer method for 2026

Figures are for tax year 2026. [Dated official rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/)

## Who this applies to

Use this method for ordinary Icelandic employed-person payroll in 2026. Establish employer and employee identity, residence and work location, pay date and period, contract and collective agreement, cash wages, benefits, pension arrangements, other deductions, and the employee's tax-credit and bracket instruction. Keep source documents and pay-run approval. Unknown tax residence, posted-worker coverage, contractor status, director fees, equity, benefit valuation or sector-specific charges require the applicable separate rule before calculation. Pay rates, including minimum pay, come from the applicable collective agreement and employment contract; this skill does not set them.

The employer must be on the withholding register (launagreiðendaskrá) and have the required electronic identity or withholding web key. Notify the register at least 8 days before the activity starts; an employer that stops paying wages during the year must notify Skatturinn within eight days. [Employer register](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/launagreidendaskra/) [Act 45/1987, art. 19](https://www.althingi.is/lagas/nuna/1987045.html) The electronic service supports returns, detailed wage information, bank payment claims, corrections and statements. [Skatturinn electronic filing](https://www.skatturinn.is/atvinnurekstur/rafraen-skil/stadgreidsla/)

## Rates, bands and thresholds

For monthly taxable income in 2026, apply each rate only to its band:

| Monthly taxable income, ISK | Rate |
| --- | ---: |
| Up to 498,122 | 31.49% |
| Above 498,122 through 1,398,450 | 37.99% |
| Above 1,398,450 | 46.29% |
| Evidence | [Official rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/) |

Each withholding rate is state income tax plus the national average municipal tax of 14.94% (state share 16.55%, 23.05% and 31.35% in the three bands). Withholding uses the same municipal rate everywhere, but each municipality sets its own final rate, so the annual assessment collects or refunds the difference. Do not adjust withholding for the employee's municipality. [Rate make-up](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

For weekly pay, the January 2026 employer notice gives weekly bands: 31.49% on the first 114,636, 37.99% from 114,637 to 321,835 and 46.29% above 321,835. Where weekly wages vary, they may be evened out between weeks within the month so that the month's withholding is right. [Employer notice 1/2026](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

The monthly personal tax credit is ISK 72,492 (ISK 869,898 for the year). The ordinary resident credit applies from the year a person turns 16. Eligible temporary employees taxed under Income Tax Act Article 3(1) also receive credit for their qualifying days in Iceland, starting on arrival rather than the first working day. Turning 16 satisfies the age condition for the whole year; it does not remove residence or stay-based limits. Establish the applicable income category, status and days under the [cross-border Guide](is-cross-border.md) before using a full annual credit. [Posted-worker credit](https://www.skatturinn.is/english/individuals/posted-workers/) [Limited-liability employment credit](https://www.skatturinn.is/english/individuals/limited-tax-liability/) These are withholding figures, not a promise of the employee's final annual tax. [Official rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/) [Personal tax credit](https://www.skatturinn.is/english/individuals/personal-tax-credit/)

For pay periods shorter than a month, the credit per period is: half a month 36,246; for 14 days and one week, the dated 2026 page shows 33,365 and 16,682 while the January 2026 notice shows 33,366 and 16,683 (the same formula rounded differently). For any other period use 869,898 × days in the period ÷ 365. [Period credits](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) [Employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) No pay period may be longer than one month. [Employer register](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/launagreidendaskra/)

Obtain instructions on the bracket, whether credit is used, starting month and supported accumulated credit. Multiple employers must use the employee's allocation; they cannot see each other's credit use. Unused credit can accumulate within the year, but cannot cross into another year. People moving to/from Iceland or temporarily working there need the day-limited entitlement checked; a displayed cumulative balance can overstate their entitlement. Obtain the employee's statement when changing employers. Never turn a credit into extra cash after withholding reaches zero. [Personal tax credit](https://www.skatturinn.is/english/individuals/personal-tax-credit/)

**Spouse's credit.** In 2026 an employee may use up to 100% of a spouse's unused credit, but only for spouses living together, or cohabitants who meet the conditions for joint taxation and file a joint return. The employer may apply it only against the Skatturinn statement of the spouse's used credit on which the spouse's name appears. [Spouse credit, 2026](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) [Conditions](https://www.skatturinn.is/einstaklingar/stadgreidsla/personuafslattur/)

If credit is over-used or pay is taxed in too low a band, too little is withheld and the shortfall becomes the employee's debt at assessment. Skatturinn states that over-used credit not corrected during the year is collected with a 2.5% surcharge. When notified, stop or reduce the credit use until it evens out, or move pay into the correct band. [Over-used credit](https://www.skatturinn.is/einstaklingar/stadgreidsla/ofnyttur-personuafslattur/)

The default calculation uses each month's wages separately, including bonuses and overtime. Averaging across months is allowed only where monthly wages normally vary by at least 50%; the employer may then withhold proportionally on total wages from the start of the income year (or of employment) to the end of the current pay period. Do not give every employer the lowest band. For minor payments from someone other than the main employer (for example union payments or board fees), the payer may withhold at the middle band rate, but only if the payment is no more than 650,000 per month. [Withholding method](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

### Children's wages

Children born in 2011 or later (who do not reach 16 in 2026) pay 6% (4% state, 2% municipal) with no personal credit, only on income above the child allowance of 300,000 for the year. On the return, enter their total wages without deductions. Children aged 15 and younger do not pay into a pension fund. The English key-rates page still says "born 2010 or later"; the dated Icelandic 2026 pages say 2011, which matches the full-year credit for those turning 16 in 2026. [Child rate 2026](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) [Employer notice](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

## The base

1. Establish wage components, pension arrangements and the employee instruction.
2. Separate withholding-exempt payments from taxable pay, then calculate taxable income, withholding and cash net separately.
3. Add employer pension and payroll tax, then file, pay and reconcile.

### Taxable pay

Withholding applies to all pay for work plus vehicle allowances, benefits, relocation and travel money, per diems and other work-related payments, except payments that Regulation 591/1987 lists as outside withholding. Two common exemptions have conditions:

- **Vehicle allowance** is outside withholding only if it reimburses specific driving done for the employer, the rate is at or below Skatturinn's valuation limit, and the employee keeps a regular log of each trip (date, distance, purpose, rate paid, employee name and ID, vehicle registration). Driving between home and the usual workplace always counts as the employee's own. If any condition fails, the payment is taxable pay.
- **Per diems and travel money** are outside withholding only for travel for the employer, within the amounts Skatturinn's valuation allows, with records of the trip purpose, days, amounts and employee. Any excess above those limits is taxable pay.

Uniforms the employee is expected to wear at work are not withholding pay. Even when a vehicle allowance is outside withholding, it still enters the payroll-tax base (see below). [Withholding base and exemptions](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) [Payroll-tax base](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/)

### Pension and gross-to-net calculation

By law the minimum pension contribution is at least 15.5% of the contribution base, and workers are covered from age 16 to 70. The split between employee and employer follows the collective agreement for the trade (or special law), and fund membership must be stated in the written employment contract. A transitional rule lets 12% be used instead of 15.5% where the current collective agreement still uses 12%, until a new agreement takes effect. [Act 129/1997, art. 1-2](https://www.althingi.is/lagas/nuna/1997129.html)

The current employer instructions use 4% employee pension and an adjustable 11.5% employer default (together 15.5%). They exclude ages 15 and younger and 70 or older. Confirm actual contributions, fund, collective agreement, base, remittance schedule and supplementary arrangements. [Employer instructions](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) The contribution base is all taxable pay for work, but not benefits in kind (such as clothing, food and housing) or reimbursements of expenses (such as vehicle allowances, per diems and meal money). [Act 129/1997, art. 3](https://www.althingi.is/lagas/nuna/1997129.html)

Employee mandatory contributions can be deducted from income up to 4% of the contribution base. Qualifying additional pension contributions have a separate deduction up to 4%; regular payment and an eligible recipient are conditions. A tax deduction limit does not itself establish a worker's contractual pension entitlement. [Pension deduction conditions](https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi/)

Employer pension contributions are not taxable to the employee, except that they become taxable income if the employer's contributions exceed 12% of the contribution base plus 2,000,000 a year. Contributions agreed in a collective agreement or fixed by law are never taxable. [Act 90/2003, art. 28, item 5](https://www.althingi.is/lagas/nuna/2003090.html)

Keep cash and noncash components distinct:

```text
withholding base = taxable cash remuneration + taxable noncash benefits
                   − eligible employee pension deduction − other supported deductions
income tax withheld = maximum of zero and
                      (progressive band tax − authorised available credit)
bank net pay = cash remuneration + supported cash reimbursements
               − employee pension withheld − income tax withheld
               − other authorised cash deductions
```

A noncash benefit can increase taxable income without adding money to the bank payment. Confirm valuation and pension treatment separately. Do not deduct employer pension or employer payroll tax from employee pay. These formulas are accounting controls; a benefit or reimbursement must have its own legal classification before use.

### Employer pension and payroll tax

Calculate employer pension separately from the employee deduction. General 2026 payroll tax (`tryggingagjald`) is 6.35%, made up of 4.90% general levy, 1.35% employment-insurance levy, 0.05% wage-guarantee fund fee and 0.05% market fee. For wages of seamen on fishing vessels add 0.65%, giving 7.00%. Its base includes taxable benefits (food, housing, clothing, car use) at their tax valuation, all vehicle allowances, taxable per diems and share-option gains in the year of exercise, as well as wages. Do not reduce this employer base by the employee's pension deduction. Payments that are not taxable to the employee, such as qualifying commuting payments, are outside the base. [Payroll tax](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald) [Seamen rate](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

Special cases, each needing evidence before use:

- **Posted EEA workers with an A1 certificate:** for citizens of an EEA state hired to work in Iceland for one year or less, the employer does not pay the full rate if it holds the worker's A1 certificate showing cover under the home country's social security. Skatturinn lists 0.293% for 2024 and 2025 and has not published a 2026 figure on that page; confirm the 2026 rate with Skatturinn before use. These wages are reported separately and excluded from the general base. [A1 rule](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald)
- **Financial undertakings** (financial firms, securities firms and insurers) also pay financial activities tax of 5.5% on all wages, monthly with withholding. [Financial activities tax](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

Employer pension contributions also enter the payroll-tax base. The wage-return guidance expressly includes the general employer pension contribution among reportable payroll-tax amounts. Use that base rule with the dated current-year rate; the annual-return page's assessment-year label is not a new wage-year rate. [Payroll-tax base reporting](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/)

```text
employer payroll tax = confirmed total payroll-tax base × applicable employer rate
ordinary cash-wage employer cost = cash wages + employer pension + payroll tax
                                  + other applicable employer obligations
```

For benefits, separately reconcile actual employer benefit cost and the tax valuation; they need not be equal. The ordinary cost formula above assumes no benefits or additional employer charges.

## Deadlines and filing

Pension contributions have a separate payment cycle: due on the tenth of the following month, final due date the last day of that month, subject to the applicable fund rules and agreement. Remit to the fund/provider rather than treating them as part of the tax-authority payment. [Act 129/1997, art. 7](https://www.althingi.is/lagas/nuna/1997129.html)

Use the employer service: `Vefskil → Staðgreiðsla → Skila skýrslu`, or supported payroll software. Withholding and payroll tax fall due on the 1st of the month after the wage month, and the return and payment must reach Skatturinn by the 15th (the final due date). Example: January wages are due by 15 February. If the 15th falls on a weekend or public holiday, it moves to the next working day. Confirm the tax calendar and the generated payment claim. Registered legal entities submit a nil return even when no wages were paid; if payroll pauses, still file, or Skatturinn estimates the amount due. [Filing and corrections](https://www.skatturinn.is/einstaklingar/sjalfsafgreidsla/stadgreidsla-af-launum/) [Dated reporting rule](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) [Due dates](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/launagreidendaskra/)

**Small-payroll exception.** If wages (and any calculated remuneration) average less than 42,000 a month, the employer may file and pay for the first time on the due date of the month in which the year's total reaches 504,000, and on every due date after that. If the year's total does not reach 504,000, it may file and pay once for the year, as if it were the December return. [Payment periods](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald)

For levy outside withholding, current Act 113/1990 Article 12 sets 1 June for individuals and 1 November for legal entities, with final due dates one month later. Published guidance conflicts: the general levy page says 1 July, while the collections page says 1 June for individuals and 1 October for companies. Use the statute as the legal reference, retain the conflict and resolve the actual assessment/payment claim with Skatturinn before payment. Ordinary taxable benefits remain in monthly reporting. [Act 113/1990, arts. 12 and 16](https://www.althingi.is/lagas/nuna/1990113.html), [general guidance](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald), [collections guidance](https://www.skatturinn.is/innheimta/skattar-og-gjold/allir-skattar-og-gjold/)

### Map the calculation to the return

The official employer instructions map the monthly return as follows:

| Field | Enter or check |
| --- | --- |
| Kennitala | Employee identifier. |
| Laun og hlunnindi | Wages, car benefits, taxable vehicle allowance and taxable daily allowances. |
| Lífeyrissjóður | Paid deductible employee pension, including eligible supplementary savings. |
| Persónuafsláttur / Persónuafsláttur maka | Authorised credit; spouse credit entered separately. |
| Þrepaskipti / Þar af í þrepi 2 | Allocate taxable income between applicable bands. |
| Mótframlag | Actual employer pension; correct the default when needed. |
| Tryggingagjald / Reikna | Calculate employer payroll tax and reconcile the displayed amount. |
| Source | [Official return instructions](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) |

Do not submit the prose calculation as a return. Match each employee row, totals and the payment claim; save the accepted submission and payment evidence.

For an incorrect submitted return, Skatturinn instructs employers to submit the correct return first and then reverse the wrong return using `Vefskil → Staðgreiðsla → Bakfæra skýrslu`; correction login requires the withholding web key. Preserve both references and acknowledgements. Reconcile the resulting liability and actual payments; a return correction is not proof of a cash refund or offset. [Correction sequence](https://www.skatturinn.is/einstaklingar/sjalfsafgreidsla/stadgreidsla-af-launum/)

For every run, reconcile wages and benefits, employee deductions, employer pension, tax bases, withholding, payroll tax, the pension-fund payment, bank net pay and ledger. Give the employee the itemised result. At year end reconcile the payroll records to wage statements and employer annual reporting for the actual wage year; use the relevant year's filing instructions before submission. Payroll-tax annual assessment follows the employer wage return. [Annual payroll-tax reporting](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald)

## Penalties and interest

**Late payment and missing returns.** If withholding is not paid on time, a surcharge of 1% of the unpaid amount is added for each day after the final due date, up to a maximum of 10%. If it is not paid within a month from the first due date, penalty interest (dráttarvextir) also runs from that first due date. If no return is filed or it is deficient, Skatturinn estimates the amount due and the same surcharge applies, unless the estimated amount was paid before the final due date. The surcharge can be waived only if Skatturinn accepts valid reasons. **Keep payroll levy separate:** Act 113/1990 Article 10 expressly excludes that daily PAYE surcharge from tryggingagjald. If the levy remains unpaid at its final due date, default interest runs from the first due date. Do not apply the withholding surcharge or its interest trigger to the employer levy. [Act 45/1987, art. 28](https://www.althingi.is/lagas/nuna/1987045.html), [Act 113/1990, arts. 10–11](https://www.althingi.is/lagas/nuna/1990113.html), [collection rules](https://www.skatturinn.is/innheimta/skattar-og-gjold/allir-skattar-og-gjold/)

## Cross-border points

Obtain separate residence and social-security determinations for cross-border workers; the A1 decision does not establish income-tax residence. The A1 limits and unresolved 2026 reduced rate are stated in the base section. Use the [cross-border Guide](is-cross-border.md) for source-payment and residence screening and the [social-contribution Guide](iceland-social-contributions.md) for contribution coverage. Foreign staffing arrangements, nonresidents and treaty relief require the applicable facts and rules before final withholding. [2026 employer guidance](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

## Worked examples that recompute

These hypothetical monthly cases assume an ordinary adult employee, full authorised monthly credit, eligible employee pension at 4%, employer pension at 11.5%, no additional savings, no benefits and no other charges unless expressly stated. Figures use exact arithmetic and show two decimal places with final rounding; actual reporting must follow the service's currency/rounding requirements. They are not authority-approved payroll outputs. [Rates and pension inputs](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) The official case below is the filing reference for identical inputs; the decimal table is secondary arithmetic validation. Do not infer a universal rounding rule from one official example.

### Official monthly example and reconciled payment

For cash wages 600,000, employee pension 24,000, taxable income 576,000, credit 72,492 and employer pension 69,000, the authority displays withholding **113,953** and payroll tax **42,482**. The taxable allocation is 498,122 in the first band and 77,878 in the second. [Official example](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

Using those displayed results, bank pay is **462,047** and employer cost is **711,482**. Reconcile bank pay plus employee pension plus withholding to cash wages; reconcile wages plus employer pension plus payroll tax to cost. These are derived controls for the official example. Actual employer/employee facts and the accepted service output still control filing. [Source illustration](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

### Decimal validation examples

Displayed band subtotals are individually rounded for readability; total tax is calculated from unrounded components, so the displayed subtotals can differ from the rounded total.

| Case | Employee result | Employer result |
| --- | --- | --- |
| A: cash wages 400,000 | Employee pension 16,000; taxable base 384,000; band tax 120,921.60; withholding 48,429.60; bank net 335,570.40. | Employer pension 46,000; payroll-tax base 446,000; payroll tax 28,321; combined cost 474,321. |
| B: cash wages 600,000 | Employee pension 24,000; base 576,000. First-band tax 156,858.62; remaining base 77,878 gives second-band tax 29,585.85. Total band tax 186,444.47; withholding 113,952.47; bank net 462,047.53. | Employer pension 69,000; payroll-tax base 669,000; payroll tax 42,481.50; combined cost 711,481.50. |
| C: cash wages 200,000 | Employee pension 8,000; base 192,000; band tax 60,460.80; withholding zero; bank net 192,000. Unused monthly credit 12,031.20 needs supporting same-year records before later use. | Employer pension 23,000; payroll-tax base 223,000; payroll tax 14,160.50; combined cost 237,160.50. |
| K: cash wages 1,800,000 | Employee pension 72,000; taxable base 1,728,000. First-band tax 156,858.62; second-band tax 342,034.61; third-band excess 329,550 gives tax 152,548.70. Total band tax 651,441.92; withholding 578,949.92; bank net 1,149,050.08. | Employer pension 207,000; payroll-tax base 2,007,000; payroll tax 127,444.50; combined cost 2,134,444.50. |
| Evidence | [Rates](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/) and [pension](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) | [Payroll tax](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald) |
| D: illustrative noncash control only | Cash 400,000, already-established taxable noncash benefit 20,000, documented deductible pension 16,000: base 404,000; band tax 127,219.60; withholding 54,727.60; bank net 329,272.40. | Confirm benefit valuation, pensionability, employer contributions and employer tax base separately; no total-cost conclusion. |

### Rule checks

| Case | Result |
| --- | --- |
| L: child born 2012, total 2026 wages 450,000 from one employer | Taxed only above the 300,000 child allowance: 150,000 × 6% = 9,000; no personal credit; no pension contributions. |
| M: withholding of 1,000,000 paid 4 days after the final due date | Surcharge 1% per day = 40,000; penalty interest applies only if unpaid a month from the first due date. |
| N: same amount paid 12 days late | Surcharge capped at 10% = 100,000; penalty interest from the first due date also applies if unpaid a month from that date. |
| Evidence | [Child rate](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) and [Act 45/1987, art. 28](https://www.althingi.is/lagas/nuna/1987045.html) |

Additional decision checks: exactly at the first band ceiling, no amount enters the next band; above the upper ceiling, only the excess enters the highest band. A second employer without current bracket/credit instructions must obtain them before a final calculation. A prior-year unused credit cannot reduce this year's tax. A spouse's credit is used only for spouses living together or qualifying cohabitants, against the Skatturinn statement. A vehicle allowance without a driving log is taxable pay. An erroneous filed return follows the correct-then-reverse sequence. A registered legal entity with no wages still files the nil return.

### Recomputable arithmetic controls

These blocks implement cases A, C and K, the stated noncash case and the displayed official reference. They check arithmetic only. They do not infer a statutory currency-rounding rule from a decimal illustration.

```oa-check
name: Iceland payroll A, ordinary monthly cash wages 2026
inputs:
  wages: 400000
  credit: 72492
steps:
  - employee_pension: wages * 0.04
  - tax_base: wages - employee_pension
  - withholding: max(0, tax_base * 0.3149 - credit)
  - net_cash: wages - employee_pension - withholding
  - employer_pension: wages * 0.115
  - levy_base: wages + employer_pension
  - payroll_levy: levy_base * 0.0635
  - employer_cost: wages + employer_pension + payroll_levy
expected:
  tax_base: 384000
  withholding: 48429.60
  net_cash: 335570.40
  levy_base: 446000
  payroll_levy: 28321
  employer_cost: 474321
```

```oa-check
name: Iceland payroll C, unused credit cannot make withholding negative
inputs:
  wages: 200000
  credit: 72492
steps:
  - employee_pension: wages * 0.04
  - tax_base: wages - employee_pension
  - band_tax: tax_base * 0.3149
  - withholding: max(0, band_tax - credit)
  - unused_credit: max(0, credit - band_tax)
  - net_cash: wages - employee_pension - withholding
expected:
  tax_base: 192000
  band_tax: 60460.80
  withholding: 0
  unused_credit: 12031.20
  net_cash: 192000
```

```oa-check
name: Iceland payroll K, upper band only on the excess
inputs:
  wages: 1800000
  first_ceiling: 498122
  second_ceiling: 1398450
  credit: 72492
steps:
  - employee_pension: wages * 0.04
  - tax_base: wages - employee_pension
  - band_one: min(tax_base, first_ceiling) * 0.3149
  - band_two: max(0, min(tax_base, second_ceiling) - first_ceiling) * 0.3799
  - band_three: max(0, tax_base - second_ceiling) * 0.4629
  - band_tax: band_one + band_two + band_three
  - withholding: max(0, band_tax - credit)
  - net_cash: wages - employee_pension - withholding
  - employer_pension: wages * 0.115
  - payroll_levy: (wages + employer_pension) * 0.0635
  - employer_cost: wages + employer_pension + payroll_levy
expected:
  tax_base: 1728000
  band_tax: 651441.92
  withholding: 578949.92
  net_cash: 1149050.08
  payroll_levy: 127444.50
  employer_cost: 2134444.50
```

```oa-check
name: Iceland payroll D, a taxable noncash benefit does not add bank cash
inputs:
  cash_wages: 400000
  taxable_benefit: 20000
  documented_pension: 16000
  credit: 72492
steps:
  - tax_base: cash_wages + taxable_benefit - documented_pension
  - withholding: max(0, tax_base * 0.3149 - credit)
  - bank_net: cash_wages - documented_pension - withholding
expected:
  tax_base: 404000
  withholding: 54727.60
  bank_net: 329272.40
```

```oa-check
name: Iceland displayed official monthly example, reconciliation only
inputs:
  wages: 600000
  employee_pension: 24000
  displayed_withholding: 113953
  employer_pension: 69000
  displayed_levy: 42482
steps:
  - bank_net: wages - employee_pension - displayed_withholding
  - cash_reconciliation: bank_net + employee_pension + displayed_withholding
  - employer_cost: wages + employer_pension + displayed_levy
expected:
  bank_net: 462047
  cash_reconciliation: 600000
  employer_cost: 711482
```

For cases M and N the principal below is **PAYE withholding**, not the employer levy, and the block computes only the capped surcharge, excluding any separately due interest:

```oa-check
name: Iceland PAYE late-payment surcharge cap, not tryggingagjald
inputs:
  unpaid_withholding: 1000000
steps:
  - four_days: unpaid_withholding * min(4 * 0.01, 0.10)
  - twelve_days: unpaid_withholding * min(12 * 0.01, 0.10)
expected:
  four_days: 40000
  twelve_days: 100000
```

## Ask the client first

- What are the employee identity, age, residence, work location, wage period and pay date?
- What contract, collective agreement, pension fund and contribution arrangement apply?
- Which cash wages, benefits, reimbursements and other deductions are supported?
- What current bracket, own-credit and spouse-credit instructions and prior usage apply?
- Which prior returns, payment claims, bank payments and pension statements require reconciliation or correction?

## When to refuse or refer

- Return the period, employee scope, evidence gaps, each cash/noncash component, pension fund and bases, employee and employer contributions, band calculation and credit usage, withholding, bank net, employer costs, filing deadline and references, and reconciliation result. Do not label an unresolved input as confirmed. Recheck before the next wage year, when an official rate/rule changes, or when worker status, pension terms, residence or benefit arrangements change.
- Refer for a specific supported method; do not substitute this ordinary calculation: cross-border workers (determine domicile, rolling-period presence and any treaty entitlement under the [cross-border residence method](is-cross-border.md); a short stay alone does not establish limited tax liability), posted workers and A1 cases, workers hired through a foreign staffing agency (the user undertaking can become liable for withholding), seamen, financial undertakings, board fees, disputed worker classification, and self-employed calculated remuneration. [Limited tax liability and staffing agencies](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026)

<!-- openaccountants-cta-block -->

## Talk to an accountant

For advice on your facts, [contact OpenAccountants](https://www.openaccountants.com/contact).

## Sources

The following primary sources were accessed on 23 October 2026. This pass checked the contribution-base and penalty corrections and the example inputs; it does not attest to all remaining scope or operational questions.

| Official source | Read on |
| --- | --- |
| [Withholding Act 45/1987](https://www.althingi.is/lagas/nuna/1987045.html) | 2026-10-23 |
| [Levy Act 113/1990](https://www.althingi.is/lagas/nuna/1990113.html) | 2026-10-23 |
| [Pension Act 129/1997](https://www.althingi.is/lagas/nuna/1997129.html) | 2026-10-23 |
| [Income Tax Act 90/2003](https://www.althingi.is/lagas/nuna/2003090.html) | 2026-10-23 |
| [atvinnurekstur/ad-hefja-rekstur/launagreidendaskra](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/launagreidendaskra/) | 2026-10-23 |
| [atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/launamidar-og-launaframtal/) | 2026-10-23 |
| [atvinnurekstur/rafraen-skil/stadgreidsla](https://www.skatturinn.is/atvinnurekstur/rafraen-skil/stadgreidsla/) | 2026-10-23 |
| [atvinnurekstur/skattar-og-gjold/tryggingagjald](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald) | 2026-10-23 |
| [atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/stadgreidsla/2026) | 2026-10-23 |
| [einstaklingar/sjalfsafgreidsla/stadgreidsla-af-launum](https://www.skatturinn.is/einstaklingar/sjalfsafgreidsla/stadgreidsla-af-launum/) | 2026-10-23 |
| [einstaklingar/stadgreidsla/ofnyttur-personuafslattur](https://www.skatturinn.is/einstaklingar/stadgreidsla/ofnyttur-personuafslattur/) | 2026-10-23 |
| [einstaklingar/stadgreidsla/personuafslattur](https://www.skatturinn.is/einstaklingar/stadgreidsla/personuafslattur/) | 2026-10-23 |
| [einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi](https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi/) | 2026-10-23 |
| [english/individuals/key-rates-and-amounts/2026](https://www.skatturinn.is/english/individuals/key-rates-and-amounts/2026/) | 2026-10-23 |
| [english/individuals/personal-tax-credit](https://www.skatturinn.is/english/individuals/personal-tax-credit/) | 2026-10-23 |
| [innheimta/skattar-og-gjold/allir-skattar-og-gjold](https://www.skatturinn.is/innheimta/skattar-og-gjold/allir-skattar-og-gjold/) | 2026-10-23 |
| [media/2026/rsk_0601_1_2026.is.pdf](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) | 2026-10-23 |
| [Posted-worker personal credit](https://www.skatturinn.is/english/individuals/posted-workers/) | 2026-10-23 |
| [Limited-liability employment credit](https://www.skatturinn.is/english/individuals/limited-tax-liability/) | 2026-10-23 |
