---
name: north-macedonia-social-contributions
description: "Use this skill for North Macedonia mandatory insurance contributions for calendar year 2026. Trigger on social security, pension insurance, health contributions, MPIN, minimum contribution base, maximum contribution base, self-employed insurance or director contributions. It separates ordinary employees, uninsured directors, self-employed business people, professional service providers and individual farmers; identifies who bears and remits each contribution; and gives the January-to-June and July-to-December wage-period rates. It covers contribution floors and ceilings, employer extended-service contributions, monthly reporting and payment, record reconciliation and international insurance routing. Salary PIT is calculated in the payroll guide. This source-cited draft is for reviewable calculations and awaits licensed professional sign-off."
jurisdiction: MK
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 0.2
---

# North Macedonia mandatory social contributions v0.2

**Tax year: 2026. Source-cited draft, tier 2.** Amounts are MKD unless stated otherwise. Professional review remains outstanding.

## Who this applies to

[Contributions Law arts. 7, 10-13][social] define each insured group and the person responsible for calculation/remittance. Ordinary employees bear the employee contributions and the employer calculates, withholds and remits them. A self-employed person calculates/pays their own contributions; UJP calculates for a taxpayer on assessed lump-sum income, who still pays. Uninsured executive directors/board members/managers fall into the separate arts. 7(1)(1-a), 10(1)(1-a) class if not already insured by employment/self-employment. Do not apply employee rates to every payment called a fee.

Individual farmers and registered market-stall traders have their own base; the pension/health funds and Chamber have the calculation responsibilities specified in art. 13. Employer-funded extended-service pension contributions are separate from deductions from employee gross salary (art. 7(3)).

## Rates, bands and thresholds

| Item | Amount | Period | Official provision |
|---|---|---|---|
| Pension/disability | 18.8% | Wages January-June 2026 | [UJP dated rate table][rates], Contributions Law prior art. 25 |
| Pension/disability | 19.9% | Wages July-December 2026 | [Contributions Law art. 25(1)(1)][social]; [UJP amendment notice][july] |
| Ordinary health | 7.5% | All 2026 | [Art. 25(1)(3)][social]; [dated rate table][rates] |
| Additional injury/occupational-disease health | 0.5% for art. 11 insured groups | All 2026 | [Arts. 11, 25(1)(7)][social] |
| Unemployment | 1.2% / 0.1% for art. 12 groups | January-June / July-December wages 2026 | [Art. 25(1)(8)][social]; [dated rate table][rates] |
| Derived ordinary employee total | 28% in both periods | 2026 | Sum of applicable [art. 25][social] / [dated rates][rates] |
| Derived ordinary self-employed total | 26.8% / 27.9% | January-June / July-December 2026 | [Arts. 7(1)(5), 10(1)(3), 11-12, 25][social]; [dated rates][rates] |
| Derived uninsured director total | 26.3% / 27.4% | January-June / July-December 2026 | [Arts. 7(1)(1-a), 10(1)(1-a), 11-12, 25][social]; [dated rates][rates] |
| January-published average gross wage reference | 69,141 | January-December 2026 calculations | [UJP 22 January announcement][bases] |
| General minimum monthly base | 34,570, UJP published amount | 2026 | [Art. 15(1)][social]; [UJP announcement][bases] |
| Professional/intellectual self-employed minimum | 69,141, one reference wage | 2026 | [Art. 15(2)][social]; [reference wage][bases] |
| Employee/director maximum monthly base | 1,106,256, 16 reference wages | 2026 | [Art. 16(1)-(2),(5)-(6)][social]; [UJP announcement][bases] |
| Self-employed maximum monthly base | 829,692, 12 reference wages | 2026 | [Art. 16(3),(5)-(6)][social]; [UJP announcement][bases] |
| Individual farmer/covered market trader base | 20% of January-published average, arithmetic 13,828.20 before operational rounding | 2026 | [Art. 14(1)(12), art. 15 exception][social]; [reference wage][bases] |

The **wage month**, not the day a bank transfer happens, determines the July split: art. 25 expressly starts with the July wage and ends with the December wage. Use the published 34,570 floor; do not silently replace it with a different rounding of half the reference wage. These parameters are not a statutory minimum-wage amount.

## The base

**Employees:** art. 14 includes salary, statutory employment additions and performance pay. Compute each fund on the appropriate base, subject to arts. 15-16. For ordinary full-month employee salary, `base = min(max(contributory gross, 34570), 1106256)`. Aggregate salary components paid by the same remitter for the same month before applying the cap; the employee cap is expressly per remitter. A cap limits contributions, not salary PIT. The general floor exceptions are specifically art. 14(1)(3),(5)-(13); art. 14(1)(2) part-time salary is not in that list. Do not prorate the floor simply because contractual hours are reduced. For fewer employee hours, [UJP calculation guidance step 2][hours] prorates gross pay and the personal reduction by worked hours. Its step 4 supplies a specific mixed work/sickness top-up: effective-work gross = monthly gross / full month hours × effective hours; effective-hours minimum = published minimum / full month hours × effective hours; top-up base = max(0, effective-hours minimum - effective-work gross), with each applicable fund charged on that top-up. Keep sickness pay and the legally responsible payer separate. This specified formula does not establish arbitrary calendar-day or all-category proration; other partial-month/part-time contribution-floor cases remain unconfirmed.

**Self-employed:** art. 14(1)(4) starts from monthly advance net business income, or UJP-assessed lump-sum net income. General business floor is 34,570; professional/intellectual services use at least 69,141; cap is 829,692. Under art. 14(1)(14), first-calendar-year starters have a specific half-reference-wage base; document the start year and resolve its interaction with art. 15(2) before calculating a new professional's base. A higher elected base is permitted on personal request under art. 14(2). Business losses do not remove a contribution floor.

The ordinary self-employed group pays pension, ordinary health and 0.5% additional health because art. 11 explicitly includes art. 10(1)(3). It is not an ordinary art. 12 unemployment-insured group. Thus its derived totals differ from an employee's. A separate continued-insurance status must be tested separately under art. 12(2).

**Uninsured directors/managers:** base is their monetary remuneration (art. 14(1)(1-a)), subject to the general floor and director ceiling. They pay pension and ordinary health; art. 11 does not list the 1-a health group and art. 12 does not list this standalone director group. If the director is an employee, use employee rules for that employment instead. Do not deduct the salary personal allowance from standalone director fees without the PIT basis.

**Individual farmers/covered market traders:** use art. 14(1)(12)'s 20% base, exempt from the general floor. Pension and ordinary health follow their group in arts. 7 and 10; art. 11 does not add the 0.5% employee/self-employed charge to those groups, nor art. 12 ordinary unemployment. Follow the designated fund/Chamber calculation rather than inventing a payroll salary.

**Employer-funded extended-service pension:** for jobs whose 12 worked months count as 18, 17, 16, 15, 14 or 13 insured months, the additional rates are respectively **9.4%, 7.83%, 6.27%, 4.7%, 3.13%, 1.57%** through June, and **9.95%, 8.29%, 6.63%, 4.98%, 3.32%, 1.66%** for July-December ([art. 25(2)][social]; [dated table][rates]). Confirm the legally designated job and duration first. Apply the relevant extra to its applicable contributory base and add it to employer cost, not the ordinary employee deduction. Ordinary employment does not itself trigger this extra.

Sick-pay/maternity replacement payments, domestic pensioners, non-working health-insured people, trainees and the new seasonal-engagement class have separate arts. 7-14 and 25 categories. Do not apply the ordinary employee bundle to them; their specialist computations are outside this guide's ordinary scope. No deduction, business expense or tax-loss offset reduces the insurance base beyond its own statutory definition. Salary PIT is computed after insurance in the payroll guide.

## Deadlines and filing

Establish the appropriate insurance admission/status with the competent employment/insurance body before calculating; retain employment/self-employment registration and any foreign coverage certificate. The [MPIN rulebook arts. 4-7][contrib-rules] requires electronic monthly integrated calculations with insured identifiers, gross pay, bases and separate funds. Funds submit calculations for the groups they administer under rulebook art. 5. Keep a status change/cessation aligned with the insurance register; a final contribution debt survives cessation.

[Contributions Law art. 18][social]: ordinary monthly MPIN by the **10th of the following month**, per insured person. Standalone directors' calculations are submitted **before paying remuneration** under art. 18(3), not automatically the employee monthly timetable. UJP checks/confirms the calculation before bank payment. Correct a rejected/incorrect calculation using the rulebook process; reconcile fund-by-fund and retain acceptance/payment references.

Art. 24: payment on salary/remuneration payment day. Unpaid ordinary wages still produce contribution maturity on the **15th of the following month**; the standalone director exception in art. 24(3) must be kept distinct. People paying for themselves pay by the **15th of the following month**. Under art. 22 employees receive the certified contribution calculation no later than **15 days after payment**, and the annual summary by **15 February next year**. No separate annual contribution settlement replaces these monthly obligations. Obligation during approved employment suspension follows art. 26, with any special-law exception.

## Penalties and interest

[Arts. 28, 28-a and 28-b][social] distinguish failure to issue records, incorrect/late calculation and paying remuneration without timely contributions. Legal-person fine ranges are micro **EUR 300-1,000**, small **600-2,000**, medium **1,800-6,000**, large **3,000-10,000**, in MKD equivalent. Sole trader/self-employed **EUR 100-250** and ordinary physical remitter **EUR 50-250** apply to the specified offences. Art. 28-b has separate responsible-person fines and potential activity/profession restrictions of **3-30 days**. UJP can assess missing contributions officially under art. 23; failing to file does not stop accrual. Art. 23 imports Tax Procedure Law collection; [art. 123][procedure] interest is **0.03% daily** from the day after maturity.

## Cross-border points

Contributions residence is not decided by the PIT 183-day test. Arts. 7, 10 and 12 define foreign-worker, foreign-employer and outbound-worker cover subject to ratified social-insurance agreements. Outbound assignments use the specific wage-history/reference rules in art. 14(1)(5)-(6). Check the actual agreement and competent body's certificate before removing local insurance. A tax treaty is not itself a social-insurance certificate, and EU coordination is not assumed.

## Two worked examples that recompute

**Simple: existing nonprofessional self-employed business, June 2026.** Assessed monthly business-income base 50,000 is between the floor and self-employed cap. Pension 9,400, health 3,750 and additional health 250 total 13,400. There is no ordinary unemployment contribution for this group (arts. 7, 10-12, 14-16; dated rates).

```oa-check
name: MK June 2026 self-employed fund split
inputs:
  declared_base: 50000
steps:
  - base: min(max(declared_base, 34570), 829692)
  - pension: base * 0.188
  - health: base * 0.075
  - injury_health: base * 0.005
  - total: pension + health + injury_health
expected:
  base: 50000
  pension: 9400
  health: 3750
  injury_health: 250
  total: 13400
```

**Edge: established professional with income below the special floor, July 2026.** Monthly advance income 40,000 is raised to 69,141 by art. 15(2). Pension at 19.9%, health at 7.5% and additional health at 0.5% total 19,290.35 when each is shown to two decimals. This is an analytical control; reconcile to UJP's accepted MPIN denomination/rounding before payment. It is not an employee's 28% bundle.

```oa-check
name: MK July 2026 professional minimum base
inputs:
  declared_base: 40000
steps:
  - base: min(max(declared_base, 69141), 829692)
  - pension: round(base * 0.199, 2)
  - health: round(base * 0.075, 2)
  - injury_health: round(base * 0.005, 2)
  - total: pension + health + injury_health
expected:
  base: 69141
  pension: 13759.06
  health: 5185.58
  injury_health: 345.71
  total: 19290.35
```

## Ask the client first

- What is each person's actual insured status, including employment, other cover and standalone directorship?
- Which wage month, start/stop dates, hours and paid/unpaid absences does the payment cover?
- Is self-employment professional, first-calendar-year or lump-sum assessed, and what base was accepted?
- Are there multiple remitters, bonuses or prior corrections for the month?
- Is the job designated for extended-service insurance, or is foreign coverage documented?

## Sources

| Official source | URL | Read on |
|---|---|---|
| UJP, gross salary calculation guidance, steps 2-4 | https://www.ujp.gov.mk/file/pravni_lica/category/643?print=1 | 2026-10-24 |
| Mandatory Social Insurance Contributions Law, through Gazette 148/2026 | https://www.ujp.gov.mk/files/attachment/0000/1616/Precisten_tekst_na_ZPZSO_07_2026______________.pdf | 2026-10-24 |
| UJP, dated contribution-rate tables | https://www.ujp.gov.mk/en/vodic/category/641?print=1 | 2026-10-24 |
| UJP, 22 January 2026 contribution-base announcement | https://www.ujp.gov.mk/mk/javnost/soopstenija/pogledni/1187 | 2026-10-24 |
| UJP, 13 July 2026 contributions amendment notice | https://ujp.gov.mk/en/javnost/soopstenija/pogledni/1266?print=1 | 2026-10-24 |
| Contribution calculation/payment rulebook, MPIN structure | https://www.ujp.gov.mk/files/attachment/0000/0198/Pravilnik_za_nacinot_na_presmetka_i_uplata_na_pridonesite_od_zadolzitelno_socijalno_osiguruvanje_od_09.12.2008_godina.pdf | 2026-10-24 |
| Tax Procedure Law, through Gazette 3/2025 | https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf | 2026-10-24 |

[hours]: https://www.ujp.gov.mk/file/pravni_lica/category/643?print=1
[social]: https://www.ujp.gov.mk/files/attachment/0000/1616/Precisten_tekst_na_ZPZSO_07_2026______________.pdf
[rates]: https://www.ujp.gov.mk/en/vodic/category/641?print=1
[bases]: https://www.ujp.gov.mk/mk/javnost/soopstenija/pogledni/1187
[july]: https://ujp.gov.mk/en/javnost/soopstenija/pogledni/1266?print=1
[contrib-rules]: https://www.ujp.gov.mk/files/attachment/0000/0198/Pravilnik_za_nacinot_na_presmetka_i_uplata_na_pridonesite_od_zadolzitelno_socijalno_osiguruvanje_od_09.12.2008_godina.pdf
[procedure]: https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf

Not yet confirmed: Interaction of the first-calendar-year half-reference base with the professional-services minimum; contribution-floor/ceiling treatment of ordinary part-time and partial-month cases beyond the confirmed UJP mixed work/sickness formula; operational fund rounding for those cases. Do not extrapolate an arbitrary calendar-day rule.

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
