---
name: es-social-contributions
description: Use this Guide to calculate Spanish social-security contributions for ordinary self-employed RETA workers and employers in the Régimen General in 2026. It covers annual computable income, the calendar-day monthly average, contribution bands, chosen and final bases, generic deductions, company and family floors, coverage rates, starting-fee conditions, bonuses, annual regularisation and pluriactividad refunds. For payroll it covers assessable cash and in-kind remuneration, extra-pay proration, overtime, contribution groups, employer and employee shares, occupational tariffs, the maximum base, MEI and solidarity. Trigger phrases include cuota de autónomos, RETA, cotización, TGSS, regularización, tarifa plana, Seguridad Social, RLC and payroll contributions. Obtain the actual registration, base, coverage and assessment records before calculating.
version: 2.1
jurisdiction: ES
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spanish social contributions: RETA and employer payroll v2.1

Compute 2026 contributions from the worker's status, assessable income, contribution base and coverage. This revision is sourced from the law; independent whole-pack review is pending and no accountant has signed it off. Amounts below are euros.

## Who this applies to

This Guide covers ordinary self-employed workers in RETA and employers/employees in the Régimen General. Determine the correct inclusion under [LGSS arts. 136 and 305](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a305) before calculating: a shareholder/director is not automatically an ordinary employee. Identify an individual business, a working shareholder/director within art. 305.2.b/e, or a collaborating relative within letter k. Their income definitions, generic deduction and minimum-base rules differ.

Social security is state-wide, including the foral territories. Use the relevant tax administration's income information for RETA regularisation; a different income-tax administration does not exclude the worker from these contribution rules ([LGSS art. 308](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308)). First establish the applicable state for an international worker under the cross-border section.

Income tax, payroll withholding and quarterly tax instalments are separate computations in [es-income-tax](es-income-tax.md), [spain-payroll](spain-payroll.md) and [es-estimated-tax](es-estimated-tax.md). Sea workers, household workers, agriculture, artists, training contracts and other special systems require their own applicable base rules; do not apply the ordinary full-time table to them. The ordinary rates and bases below apply from **1 January 2026** under [Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296).

## Rates, bands and thresholds

### RETA income bands and chosen monthly bases

Every row below is for **2026** under [order art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10). Income is the statutory monthly average calculated in the next section, not turnover or the bank debit. The reduced table ends **below** 1,166.70; that exact amount starts general band 1.

| Table/band | Monthly computable income | Minimum base | Maximum base | Official source |
|---|---:|---:|---:|---|
| Reduced 1 | ≤670 | 653.59 | 718.94 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Reduced 2 | >670 to 900 | 718.95 | 900.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Reduced 3 | >900 and <1,166.70 | 849.67 | 1,166.70 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 1 | ≥1,166.70 to 1,300 | 950.98 | 1,300.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 2 | >1,300 to 1,500 | 960.78 | 1,500.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 3 | >1,500 to 1,700 | 960.78 | 1,700.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 4 | >1,700 to 1,850 | 1,143.79 | 1,850.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 5 | >1,850 to 2,030 | 1,209.15 | 2,030.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 6 | >2,030 to 2,330 | 1,274.51 | 2,330.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 7 | >2,330 to 2,760 | 1,356.21 | 2,760.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 8 | >2,760 to 3,190 | 1,437.91 | 3,190.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 9 | >3,190 to 3,620 | 1,519.61 | 3,620.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 10 | >3,620 to 4,050 | 1,601.31 | 4,050.00 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 11 | >4,050 to 6,000 | 1,732.03 | 5,101.20 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| General 12 | >6,000 | 1,928.10 | 5,101.20 | [Art. 18.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |

| RETA item | Amount/rule | Year | Official source |
|---|---|---|---|
| Common contingencies (CC) | 28.30% | 2026 | [Order art. 18.2.a](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Occupational contingencies | 1.30%, comprising IT 0.66% and permanent incapacity/death/survivors 0.64% | 2026 | [Art. 18.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Cessation and training | 0.90% and 0.10%; SETA cessation uses 2.20% | 2026 | [Art. 37.5–6](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-9) |
| MEI | 0.90% of CC base, worker pays | 2026 | [Art. 18.2.c](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| IT covered in another regime, no voluntary RETA IT election | Reduce the CC quota by 0.055 × that quota | 2026 | [Art. 18.2.a](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| No occupational cover in an eligible exception | Additional 0.10% on chosen base | 2026 | [Art. 18.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Generic income deduction | 7%; 3% for art. 305.2.b/e after 90 days in those categories | Current | [LGSS art. 308.1.c.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308) |
| Company/family floor | Final base at least group 7 minimum 1,424.40 once the 90-day test applies; 2025 provisional base can continue during 2026 | 2026 | [LGSS art. 308.1.a.4](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308), [order art. 18.4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |
| Pluriactividad | Refund 50% of total CC above 17,323.68; capped at 50% of RETA CC paid | 2026 | [Order art. 18.8](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) |

For ordinary full RETA coverage with the same base for every line, the **derived sum** is `28.30 + 1.30 + 0.90 + 0.10 + 0.90 = 31.50%`. This is arithmetic from the statutory components, before an applicable exception or bonus. The [TGSS summary](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) prints 31.40% while listing those same components. Follow the order. Keep separate component amounts and reconcile rounding with the TGSS assessment.

### Régimen General, ordinary full-time employment

| Contribution group | Minimum CC base | Maximum CC base | Year and source |
|---|---:|---:|---|
| 1, engineers/graduates and senior management | 1,989.30/month | 5,101.20/month | [2026 order art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3) |
| 2, technical engineers/qualified assistants | 1,649.70/month | 5,101.20/month | [2026 art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3) |
| 3, administrative/workshop heads | 1,435.20/month | 5,101.20/month | [2026 art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3) |
| 4–7 | 1,424.40/month | 5,101.20/month | [2026 art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3) |
| 8–11, daily-paid categories | 47.48/day | 170.04/day | [2026 art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3) |
| Accident/occupational base | Floor 1,424.40/month; ceiling 5,101.20/month | Apply applicable daily/partial-period rules | [2026 art. 2](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a2) |

| Contribution | Employer | Employee | Year and source |
|---|---:|---:|---|
| CC | 23.60% | 4.70% | [2026 art. 4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a4) |
| MEI, CC base | 0.75% | 0.15% | [2026 art. 16](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-8) |
| Unemployment, indefinite and listed equivalent contracts | 5.50% | 1.55% | [2026 art. 33.2.a.1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-5) |
| Unemployment, other fixed-term contracts | 6.70% | 1.60% | [2026 art. 33.2.a.2](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-5) |
| FOGASA | 0.20% | 0 | [2026 art. 33.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-5) |
| Training | 0.60% | 0.10% | [2026 art. 33.2.c](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-5) |
| AT/EP | Applicable activity/occupation tariff | 0 | [LGSS DA 61](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#da-37) |
| Additional overtime, force majeure | 12% of overtime pay | 2% | [2026 order art. 5](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a5) |
| Additional other overtime | 23.60% of overtime pay | 4.70% | [2026 art. 5](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a5) |

The lower unemployment rate also applies to the listed training/professional-practice, relief, substitution and surviving interinidad contracts, and any contract with a worker whose recognised disability is at least 33%. A conversion to indefinite uses the lower rate from conversion. The contribution base for unemployment, FOGASA and training is the **AT/EP base** ([art. 33](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-5)). Do not apply an ordinary percentage to a training contract where the order requires its special quota method.

| Slice of assessable monthly remuneration above ceiling | Employer | Employee | Year and source |
|---|---:|---:|---|
| Above 5,101.20 up to 5,611.32 | 0.96% | 0.19% | [2026 solidarity, order art. 17](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-9) |
| Above 5,611.32 up to 7,651.80 | 1.04% | 0.21% | [2026 art. 17](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-9) |
| Above 7,651.80 | 1.22% | 0.24% | [2026 art. 17](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-9) |

### Earlier-year regularisation

Use the year being regularised. Do not apply 2026 rates to a 2025 base difference.

| Item | 2025 figure | Official source |
|---|---|---|
| Maximum base | 4,909.50/month | [Orden PJC/178/2025, arts. 2/18](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780) |
| MEI | 0.80%; employer 0.67%, employee 0.13% | [2025 art. 16](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780) |
| Pluriactividad threshold | 16,672.66 | [2025 art. 18.8](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780) |
| Special company/family and no-income-return minimum | 1,000 under the temporary 2023–2025 rule | [RDL 13/2022 DT 7](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482) |

## The base

### RETA income and choice

1. **Build annual computable income across activities** under [LGSS art. 308.1.c.1](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308). Direct assessment uses IRPF net income plus the proprietor's social-security and alternative-mutual contributions deducted in reaching it. Modules use rendimiento neto previo, except agriculture/forestry/livestock use rendimiento neto previo minorado. Attributed income uses the specific direct/modules attribution rule in that article; do not add back a cost twice.
2. **Include the statutory shareholder income.** For art. 305.2.b, add gross cash/in-kind equity income from entities in which the worker has at least 33% at corporate-tax accrual, or at least 25% as administrator, plus work income from those entities. Include the article's work/capital income for cooperative working members and art. 305.2.c/d/e partners or co-owners. Do not substitute only dividends or only accounting profit.
3. **Deduct generic expenses:** multiply qualifying aggregate income by 93%, or 97% where the 3%/90-day company category applies ([art. 308.1.c.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308)).
4. **Use days, not a presumed number of months.** Let `D` be calendar days of registration subject to regularisation after statutory exclusions. `monthly_income = annual_computable_income_after_generic_deduction / D × 30`. Use actual registration and benefit records to establish D. Do not assume annual/12, or divide by the number of bank debits ([RD 2064/1995 arts. 44.2.a and 46.2.1–2](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a44)).
5. Select the band and a provisional base within its limits, with the company/family floor when applicable. Apply every covered contribution component, then a legally applicable bonus. Keep MEI separate: it is not reduced by ordinary contribution bonuses ([LGSS art. 127 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a1-5)).

**Provisional high bases and special periods.** [Order art. 18.5](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10) permits the specified unchanged pre-2023 high base, or a lower base, during 2026 despite income implying a lower band. The separate regularisation election in [RD 2064 art. 46.2.6](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a46) can preserve eligible provisional bases up to the 31 December 2022 base by renouncing refund by the last day of the month after notification. Distinguish these rules; do not assume every base change destroys that separate election.

Late registration and office registration have the exact nonregularisable periods and general-band-1 minimum in [RD 2064 art. 44.3.c/d](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a44), with a possible higher inspection base. Failure to file IRPF, or a direct-assessment return declaring no relevant income, uses the group 7 minimum under art. 44.3.e. Exclude the statutory reduced-fee periods and benefit-related bases/periods from regularisation as directed in art. 46.1–2. Do not treat every sickness day as an independently regularisable month.

### Annual regularisation

Follow [RD 2064 art. 46.2](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a46):

- Calculate D and monthly income as above. Calculate `average_provisional_base = (sum of provisional monthly bases − bases attributable to excluded days) / D × 30`, using proportionate exclusions from the TGSS record.
- If this average is within the applicable minimum/maximum, provisional bases become final. If below, the final base is the band minimum; if above, it is the maximum, subject to the historical-base election.
- For an adjustment, retain the **signed difference for each month** between final and provisional base. Prorate band limits for partial registration months. Apply that month's rates, benefits and other contribution data, then net the differences. Do not calculate every full-year case as twelve identical debits or discard negative monthly differences.
- A net amount due is payable by the last day of the month following notice, without surcharge/interest if paid by then. A refund is automatic, without interest, before 30 April of the year following the tax administration's income communication. Existing unpaid provisional debts and their surcharges/interest are not erased ([LGSS art. 308.1.c.4](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308)).

For **pluriactividad**, include employer **and** employee CC from employment plus RETA CC. `refund = min(0.50 × max(total_CC − 17,323.68, 0), 0.50 × RETA_CC_paid)`. TGSS pays within four months after regularisation, subject to the statutory data/special-case exceptions ([LGSS art. 313](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a313); [order art. 18.8](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10)). This is not a refund of every type of contribution.

### Reduced starting fee and family/territorial bonuses

[Ley 20/2007 art. 38 ter](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a3-5) allows the starting reduction for first registration or no RETA registration in the preceding two years; use three years if the previous registration enjoyed it. Request it at registration. It runs from the effective registration date through the next twelve complete calendar months, with no cessation/training contribution during it. A further twelve complete months requires expected annual computable income **below** annual SMI, an application before that period starts, and the condition in each year if it spans two. The first period is not regularised; the extension is tested under art. 38 ter.6. Disability ≥33%, gender-violence and terrorism cases use 24 and 36 complete months instead. The article excludes joining relatives through the second degree and the specified religious members, but expressly includes qualifying company/cooperative members.

The current statutory monetary authority for a **new 2026** reduced fee remains unconfirmed in this pass. [RDL 13/2022 DT 5](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482) fixes the stated amounts for 2023–2025 and refers later years to annual budgets. The [TGSS guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) advertises 80 plus MEI, but its displayed total does not reconcile with its stated base/rate. Use the individual's TGSS award and assessment to document the amount; do not certify a general 2026 amount from this discrepancy. This precise gap does not prevent an ordinary full-rate computation.

The [family-collaborator bonus, art. 35](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a35), covers the listed spouse/partner/relatives through second degree who collaborate in the business and were not registered in the preceding five years. It is 50% for eighteen months and 25% for the following six, applied to CC on **general-band-1 minimum**, rather than the whole chosen-base quota. A qualifying unmarried partner requires the article's five-year continuous cohabitation and registry/public-document evidence. Apply the separate final-base floor when relevant.

For **Ceuta/Melilla**, verify residence, activity and the applicable sector list. [Ley 20/2007 art. 36](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409#a36), amended by [RDL 22/2026 art. 36/DF 3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-18429), changes the CC bonus from 50% to **75% for quotas accrued from 1 October 2026**. The revised list is agriculture/fishing/aquaculture; industry except energy/water; commerce; tourism; hospitality and other services with the specified fixed-wing air/financial-insurance/real-estate exclusions. Use the earlier wording, including its building-construction exclusion, for earlier quotas. Do not reduce other contingencies by this CC-only bonus.

### Employer payroll calculation

Build assessable remuneration under [LGSS art. 147](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a147). Include cash/in-kind pay and remuneration due even if not yet paid, with only the statutory exclusions and limits. Add the prorated annual extra/irregular pay: annual estimate/12 for monthly remuneration, or /365 × days for daily remuneration ([order art. 1](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1)). Expenses are not excluded merely because the payroll labels them allowances; apply the actual art. 147.2 conditions.

Maintain separate **CC** and **AT/EP** bases. Overtime is excluded from CC but included for occupational protection; its additional contribution is calculated separately without reducing the AT/EP base. Apply the group minimum and ceiling to CC, and the occupational floor/ceiling to AT/EP. Compute CC/MEI on CC; unemployment/FOGASA/training and the employer's AT/EP tariff on AT/EP. Deduct only the employee shares from pay; the employer pays both shares to TGSS ([LGSS art. 147.2.e](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a147); [order arts. 1–5/16/33](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296)).

Obtain actual **CNAE-2025 and occupation** for the tariff in [LGSS DA 61](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#da-37). Table II's office rate of 1.50% (IT 0.80%, IMS 0.70%) requires exclusive office work in office premises without exposure to the enterprise's activity risks. A job title alone is insufficient. Do not substitute one assumed office rate for every business. Part-time workers, multiple employment, sickness and other suspensions need the corresponding special base rules in the order before finalising payroll.

For solidarity, use assessable remuneration under [LGSS art. 19 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a1-4), rather than cash paid. For a full monthly period, calculate the three slices as `s1 = min(max(R − 5,101.20, 0), 510.12)`, `s2 = min(max(R − 5,611.32, 0), 2,040.48)`, `s3 = max(R − 7,651.80, 0)`. Multiply each by the employer/employee rates above. Daily workers use maximum daily base × contribution days; monthly partial periods use the proportional monthly maximum ([order art. 17.2](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-9)). Solidarity is additional to capped ordinary contributions and does not apply to RETA.

### Benefit and bank-record boundaries

For ordinary RETA temporary incapacity, [LGSS art. 321](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a321) starts common-contingency entitlement on day 4, and occupational entitlement on the day after leave begins. The [Social Security benefit page](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/10952/28362/28365) sets the ordinary 60% days 4–20/75% from day 21 common-contingency rates and 75% occupational rate. Eligibility and regulatory-base calculation require the actual coverage and contribution record; do not promise a benefit from the bank debit. After sixty days of temporary incapacity with benefit entitlement, the mutua or SEPE pays the contribution quotas under [order art. 37.4](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-9).

For cessation, [LGSS arts. 338–339](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a338) use the prior twelve continuous months' base average, ordinarily 70%, or 50% for the specified partial cases. Test legal cessation, at least twelve qualifying months within the prior twenty-four, the 4–24-month duration scale and eighteen-month interval after prior recognition. Art. 339.3–4 applies dependent-child/IPREM limits and exceptions; a voluntary closure alone does not establish legal cessation. The current monetary IPREM and a particular claimant's entitlement are not computed here.

Treat a TGSS debit as an identification clue. Obtain the base report, assessment and award before calling it RETA, employer RLC, reduced fee, regularisation or pluriactividad refund. Keep principal, interest, surcharge and refund nature separate. For direct-assessment IRPF, the [AEAT contribution-booking guidance](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/7-cumplimentacion-irpf/7_4-rendimientos-actividades-economicas/7_4_2-regimen-estimacion-directa/7_4_2_3-gastos-fiscalmente-deducibles/cotizaciones-reta.html) puts a regularisation in the year settled; do not amend the original year solely for that adjustment. Its 2025 box numbers are not assumed to be the approved 2026 return boxes.

## Deadlines and filing

| Action | Rule | Official source |
|---|---|---|
| RETA payment | Within the same month; use the assessed collection document/direct-debit arrangement | [RD 1415/2004 art. 56.1.b](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836#a56) |
| Employer payment | During the month following accrual | [RD 1415 art. 56.1](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836#a56) |
| RETA electronic dealings | Use authorised RED or the applicable electronic-office service | [Orden ESS/484/2013 art. 2.2.b](https://www.boe.es/buscar/act.php?id=BOE-A-2013-3362#a2) |
| Employers' RED obligation | Régimen General regardless of headcount; household and bullfighting exceptions in art. 2.3 | [Order ESS/484 art. 2](https://www.boe.es/buscar/act.php?id=BOE-A-2013-3362#a2) |
| Base change requested Jan–Feb / Mar–Apr / May–Jun | Effective 1 March / 1 May / 1 July | [RD 2064 art. 45](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a45) |
| Base change requested Jul–Aug / Sep–Oct / Nov–Dec | Effective 1 September / 1 November / 1 January next year | [RD 2064 art. 45](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a45) |
| Regularisation due/refund | Due by month-end after notice; refund before 30 April after income-communication year | [RD 2064 art. 46.2.5](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a46) |

Reconcile payroll workers/days/bases with the TGSS settlement and its payment receipt. Do not substitute a bank debit for a filed contribution record or apply the special artist quarterly option to every autónomo. For a regularisation notice, retain the tax-income communication, excluded-day schedule, provisional/final base schedule and due-date evidence.

## Penalties and interest

Contribution surcharges depend on compliance with the art. 29 data/settlement duties, as well as payment timing. They are separate from an administrative infringement fine.

| Late-payment situation | Surcharge | Official source |
|---|---:|---|
| Art. 29 duties met; paid in first calendar month after payment deadline | 10% | [LGSS art. 30.1.a.1](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) |
| Same duties met; paid from second subsequent month | 20% | [Art. 30.1.a.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) |
| Duties not met; paid before end of demand/assessment payment period | 20% | [Art. 30.1.b.1](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) |
| Duties not met; paid from end of that period | 35% | [Art. 30.1.b.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) |
| Non-contribution public-law Social Security debt | 20% | [Art. 30.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) |

[LGSS art. 31](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a31) makes interest exigible after fifteen days from the enforcement notice/deduction-procedure communication, and in the specified suspended-appeal case. Principal accrues from its original payment deadline; surcharge interest accrues from exigibility. The rate is the legal-money rate during each accrual period **increased by 25%**, unless the budget sets another rate. Use a verified monetary rate for the actual interval; do not confuse a 25% relative increase with 25 percentage points. A RETA regularisation paid within its special notice deadline has no such surcharge/interest.

## Cross-border points

Establish applicable social-security legislation before charging Spanish contributions. [Regulation 883/2004 arts. 11–13](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02004R0883-20190731) provides one applicable Member State, ordinary work-state rules, qualifying temporary-posting exceptions and multi-state-work rules. In particular, simultaneous employment in one Member State and self-employment in another follows the employment-state rule under art. 13.3. Do not treat a foreign client, foreign bank account or tax treaty as proof of social-security exemption.

Obtain the applicable-legislation determination and its evidence before computing an international worker's quotas. The detailed A1 application, non-EU agreements and special telework exceptions are outside this ordinary Spanish computation. Once Spanish legislation applies, use the relevant Spanish regime and income scope; ordinary international clients do not by themselves justify refusing a domestic RETA computation. Foral IRPF information remains relevant to the statewide regularisation under [LGSS art. 308](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a308).

## Two worked examples that recompute

### 1. Individual autónomo: statutory day average and a chosen base

Hypothetical 2026 records establish **180 calendar days subject to regularisation**, direct-assessment activity net income 10,000 after deducting own RETA of 1,200, ordinary individual status, full coverage and no bonus. Add back 1,200 and deduct 7%: 10,416. The statutory monthly income is `10,416 / 180 × 30 = 1,736`, in general band 4. A chosen base of 1,200 lies between 1,143.79 and 1,850. For one complete month on that base, CC is 339.60, occupational 15.60, cessation 10.80, training 1.20 and MEI 10.80, total **378.00**. The regularisation comparison still uses the actual provisional-base schedule; the example does not infer it from the income day count ([RD 2064 arts. 44/46](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579#a46); [order arts. 18/37](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a1-10)).

```oa-check
name: RETA 2026 day average and full-coverage month
inputs:
  net_irpf: 10000
  own_contributions_deducted: 1200
  regularisable_days: 180
  chosen_base: 1200
steps:
  computable_income: (net_irpf + own_contributions_deducted) * 0.93
  monthly_income: computable_income / regularisable_days * 30
  minimum_margin: chosen_base - 1143.79
  maximum_margin: 1850 - chosen_base
  cc: chosen_base * 0.283
  occupational: chosen_base * 0.013
  cessation: chosen_base * 0.009
  training: chosen_base * 0.001
  mei: chosen_base * 0.009
  contribution: cc + occupational + cessation + training + mei
expected:
  computable_income: 10416
  monthly_income: 1736
  minimum_margin: 56.21
  maximum_margin: 650
  cc: 339.60
  occupational: 15.60
  cessation: 10.80
  training: 1.20
  mei: 10.80
  contribution: 378
```

### 2. Employer: capped ordinary bases and two solidarity slices

An ordinary monthly group-1 employee has **6,000 of assessable remuneration for October 2026**, already including extra-pay proration, no overtime, an indefinite contract and no contribution relief. The verified work facts meet table II(a)'s exclusive-office conditions, giving the statutory 1.50% AT/EP tariff. Both ordinary bases are capped at 5,101.20. Solidarity uses 510.12 in the first slice and 388.68 in the second. On the separately rounded component working paper, employer contributions are **1,648.98**, employee deductions **333.37**; employer cost is **7,648.98** before other costs. Cash after employee social contributions is 5,666.63 **before IRPF withholding**, which must be computed separately. Reconcile component rounding with the final TGSS settlement ([order arts. 3/4/16/17/33](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296); [LGSS DA 61 table II(a)](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#da-37)).

```oa-check
name: October 2026 payroll cap and employer-employee solidarity
inputs:
  remuneration: 6000
  cap: 5101.20
steps:
  base: min(remuneration, cap)
  slice_one: min(max(remuneration - cap, 0), 510.12)
  slice_two: min(max(remuneration - 5611.32, 0), 2040.48)
  slice_three: max(remuneration - 7651.80, 0)
  employer_cc: round(base * 0.236, 2)
  employer_unemployment: round(base * 0.055, 2)
  employer_fogasa: round(base * 0.002, 2)
  employer_training: round(base * 0.006, 2)
  employer_mei: round(base * 0.0075, 2)
  employer_occupational: round(base * 0.015, 2)
  employer_solidarity: round(slice_one * 0.0096, 2) + round(slice_two * 0.0104, 2) + round(slice_three * 0.0122, 2)
  employee_cc: round(base * 0.047, 2)
  employee_unemployment: round(base * 0.0155, 2)
  employee_training: round(base * 0.001, 2)
  employee_mei: round(base * 0.0015, 2)
  employee_solidarity: round(slice_one * 0.0019, 2) + round(slice_two * 0.0021, 2) + round(slice_three * 0.0024, 2)
  employer_total: employer_cc + employer_unemployment + employer_fogasa + employer_training + employer_mei + employer_occupational + employer_solidarity
  employee_total: employee_cc + employee_unemployment + employee_training + employee_mei + employee_solidarity
  employer_cost: remuneration + employer_total
  before_irpf_cash: remuneration - employee_total
expected:
  base: 5101.20
  slice_one: 510.12
  slice_two: 388.68
  slice_three: 0
  employer_solidarity: 8.94
  employee_solidarity: 1.79
  employer_total: 1648.98
  employee_total: 333.37
  employer_cost: 7648.98
  before_irpf_cash: 5666.63
```

## Ask the client first

1. Which regime, employment/shareholding/director/family status, registration dates, contribution days, benefits and applicable-state determination are documented?
2. What activity income, own contributions, company work/capital income and tax-administration records establish the RETA annual numerator?
3. Which provisional bases, actual coverage, reduced-fee/bonus awards and regularisation notices apply to each period?
4. For payroll, what remuneration, in-kind items, annual extra pay, overtime, group, contract, working time, CNAE and actual occupation establish each base and rate?
5. What employment and RETA CC payments support a pluriactividad refund, including the employer share?
6. What filed settlement, demand/enforcement dates and bank receipts distinguish principal, adjustments, surcharge and interest?

## Sources

| Official source | Scope read | Read on |
|---|---|---|
| [Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296) | 2026 employee/RETA bases, component rates, solidarity, pluriactividad and long-IT contribution payer, arts. 1–5, 16–18, 33/37 | 2026-10-26 |
| [LGSS, RDL 8/2015](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724) | Regime inclusion, assessable pay, MEI, solidarity, income definition, regularisation, surcharge/interest, office tariff and benefit boundaries | 2026-10-26 |
| [RD 2064/1995](https://www.boe.es/buscar/act.php?id=BOE-A-1996-1579) | Arts. 44–46, calendar-day denominator, average provisional base, signed monthly adjustments, exclusions and historical-base election | 2026-10-26 |
| [Ley 20/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-13409), [RDL 13/2022](https://www.boe.es/buscar/act.php?id=BOE-A-2022-12482), [RDL 22/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-18429) | Starting-fee eligibility/periods, family bonus, transitional amounts and Ceuta/Melilla effective date | 2026-10-26 |
| [RD 1415/2004](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836), [Orden ESS/484/2013](https://www.boe.es/buscar/act.php?id=BOE-A-2013-3362) | Payment periods and mandatory electronic dealings | 2026-10-26 |
| [Orden PJC/178/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-3780) | Earlier-year contribution ceiling, MEI and pluriactividad threshold | 2026-10-26 |
| [TGSS autonomous-worker guide](https://portal.seg-social.gob.es/wps/portal/importass/importass/Colectivos/trabajo%2Bautonomo/guia) | Administrative explanation; combined-rate and reduced-fee total discrepancies identified, not substituted for the order | 2026-10-26 |
| [Social Security, temporary incapacity](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/PrestacionesPensionesTrabajadores/10952/28362/28365), [AEAT RETA-booking guidance](https://sede.agenciatributaria.gob.es/Sede/ayuda/manuales-videos-folletos/manuales-ayuda-presentacion/irpf-2025/7-cumplimentacion-irpf/7_4-rendimientos-actividades-economicas/7_4_2-regimen-estimacion-directa/7_4_2_3-gastos-fiscalmente-deducibles/cotizaciones-reta.html) | Ordinary benefit percentage boundaries and year of booking a settled regularisation | 2026-10-26 |
| [Regulation 883/2004, arts. 11–13](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:02004R0883-20190731) | Applicable-state gateway; read in a normal browser after automated access was blocked | 2026-10-26 |

**Not yet confirmed:** the current statutory monetary authority and reconciled assessment of the new-2026 starting fee; the exact equality-at-SMI treatment of the extension where art. 38 ter's wording and RD 2064 art. 44.3.f use differing boundaries; current monetary IPREM for a cessation-benefit cap; the monetary interest rate for a particular accrual interval. Detailed special-system/part-time/suspension contribution calculations, non-EU coordination and individual benefit awards are outside this ordinary full-time/RETA computation. Independent whole-pack review remains outstanding.

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
