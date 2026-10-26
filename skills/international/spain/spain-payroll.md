---
name: spain-payroll
description: Use this Guide to calculate ordinary common-territory Spanish employee payroll for 2026. It computes annual IRPF withholding inputs, the withholding-specific employment reduction, national personal and family minima, the reference scale, quota limits, rate truncation and mid-year recalculation. It reconciles taxable cash and in-kind pay with separate employee and employer social contributions, extra-pay proration, overtime and solidarity through the companion contribution Guide. Trigger phrases include nómina, bruto a neto, retención IRPF, Modelo 145, paga extraordinaria, regularización del tipo, payroll cost, Modelo 111 and Modelo 190. Obtain the contract, collective agreement, contribution classification, annual pay forecast, declared family circumstances and prior pay and withholding records. Foral, non-resident and elected impatriate payroll require their own applicable tax route.
version: 1.1
jurisdiction: ES
tax_year: 2026
last_updated: 2026-10-26
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain: employee payroll and withholding v1.1

Turn contractual pay into a payslip, contribution settlement and withholding working paper for 2026. This revision is sourced from the law; independent whole-pack review is pending and no accountant has signed it off. The payroll withholding calculation is separate from the worker's annual state-plus-regional IRPF return.

## Who this applies to

Use this Guide for ordinary employees whose employment income is subject to the **common-territory IRPF withholding rules**. Establish the applicable collective agreement, contract, actual contribution regime and tax administration first. An administrator's remuneration for holding office can use a fixed tax-withholding rate while their social-security classification follows different facts; do not force it into the ordinary employee calculation ([RIRPF art. 80](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a80); [LGSS arts. 136/305](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a305)).

Foral withholding, non-resident IRNR, the elected impatriate regime, sea/household/agricultural systems and specialist contract contribution methods require their own applicable rules. Spanish social contributions remain state-wide; use [es-social-contributions](es-social-contributions.md) for the contribution computation and RETA classification. Use [es-modelo-111](es-modelo-111.md) for aggregating and remitting withholding, and [es-income-tax](es-income-tax.md) for annual IRPF. That annual Guide now includes ordinary employees; payroll withholding does not settle their annual liability.

Before payroll, obtain the worker's declared circumstances under [RIRPF art. 88](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a88), normally Modelo 145, and employer/worker affiliation records. Do not invent family circumstances from a bank payment. If the worker does not communicate a circumstance, apply the regulation's declared/default position rather than assume a favourable allowance.

## Rates, bands and thresholds

### No-withholding limits and fixed/minimum rates

These are **2026 annual pay limits**, not annual return-filing limits. Apply [RIRPF art. 81](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a81) to the remuneration defined by art. 83.2.

| Declared family situation | No descendants | One | Two or more | Source |
|---|---:|---:|---:|---|
| 1: qualifying unmarried/widowed/divorced/separated single-parent family | Not applicable | 17,644 | 18,694 | [Art. 81.1, including single-parent entitlement test](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a81) |
| 2: married, not legally separated; spouse's non-exempt annual income ≤1,500 | 17,197 | 18,130 | 19,262 | [Art. 81.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a81) |
| 3: other situations, including undeclared situation | 15,876 | 16,342 | 16,867 | [Art. 81.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a81) |

Increase the relevant limit by **600** for qualifying Social Security/Clases Pasivas pensions and **1,200** for unemployment benefits. The exclusion does **not** override fixed rates or statutory minimum rates ([art. 81.2–3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a81)).

| Item | 2026 rule | Source |
|---|---|---|
| Contract/relationship shorter than a year; specified performing-arts special relationship | At least 2% | [RIRPF art. 86.2](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a86) |
| Other dependent special employment relationships | At least 15%; statutory prisoner/disability exceptions | [Art. 86.2](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a86) |
| Qualifying Ceuta/Melilla income | Ordinary/fixed rates reduced by 60%; relevant minimum floors 0.8% and 6% | [Arts. 80.2/86.2](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a80) |
| Directors/board office | 35%; 19% if payer's net turnover in last completed tax period before payment <100,000, annualised if period short | [Art. 80.1.3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a80) |
| Teaching courses/conferences and listed literary/artistic/scientific employment income | 15%; qualifying authors have a separate 7% test and written communication | [Art. 80.1.4](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a80) |
| Arrears attributable to prior years | 15%, unless another fixed art. 80.1.3/4 rate applies | [Art. 80.1.5](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a80) |
| Ordinary quota limit where annual remuneration ≤35,200 | 43% of positive excess over applicable art. 81 limit | [Art. 85.3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a85) |
| Transitional financed main-home deduction | Reduce rate by two percentage points if annual remuneration <33,007.20 and notified qualifying entitlement; not below zero or applicable floor | [Art. 86](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a86) |
| Regularised rate maximum | 47%; 19% where all employment income meets the specified Ceuta/Melilla condition | [Art. 87.5](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a87) |

### Withholding scale

Define `T(x)` by the following **2026 withholding reference scale**. It is applied to the withholding base and separately to the personal/family minimum. It does not replace the state and regional scales on the annual return.

| Base slice | Marginal rate | Quota at lower boundary | Source |
|---|---:|---:|---|
| 0–12,450 | 19% | 0 | [RIRPF art. 85.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a85) |
| >12,450–20,200 | 24% | 2,365.50 | [Art. 85.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a85) |
| >20,200–35,200 | 30% | 4,225.50 | [Art. 85.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a85) |
| >35,200–60,000 | 37% | 8,725.50 | [Art. 85.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a85) |
| >60,000–300,000 | 45% | 17,901.50 | [Art. 85.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a85) |
| >300,000 | 47% | 125,901.50 | [Art. 85.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a85) |

### Deductions and personal/family minimum

| Item | Amount/condition used for withholding in 2026 | Source |
|---|---|---|
| Other employment expenses | 2,000; qualifying geographical mobility adds 2,000; active disability adds 3,500 or 7,750 under the statutory degree/assistance conditions | [LIRPF art. 19.2.f](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a19), [RIRPF art. 83.3.c](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a83) |
| Employment reduction, R ≤14,852 | 7,302, capped at R | [RIRPF art. 83.3.d](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a83) |
| 14,852 <R ≤17,673.52 | 7,302 −1.75 ×(R −14,852) | [Art. 83.3.d](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a83) |
| 17,673.52 <R <19,747.50 | 2,364.34 −1.14 ×(R −17,673.52) | [Art. 83.3.d](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a83) |
| R ≥19,747.50 | No art. 83.3.d reduction | [Art. 83.3.d](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a83) |
| Taxpayer minimum | 5,550; add 1,150 if over 65 and another 1,400 if over 75 | [LIRPF art. 57](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a57) |
| Descendants, first/second/third/fourth and later | 2,400 /2,700 /4,000 /4,500; under-three supplement 2,800 | [Art. 58](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a58) |
| Ascendant | 1,150 if over 65 or disabled; further 1,400 if over 75 | [Art. 59](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a59) |
| Disability minimum for worker/qualifying relative | 3,000 at ≥33%, 9,000 at ≥65%; assistance supplement 3,000 under the statutory conditions | [Art. 60](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a60) |
| Qualifying relative's own annual income ceiling | 8,000, excluding exempt income; other age/cohabitation conditions apply | [Arts. 58–61](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a58) |

`R` for this reduction is remuneration after the **art. 83.3.a irregular-income reductions and art. 83.3.b employee contributions**, before the 2,000/other-expense item. Do not import the annual return's other-income condition into this withholding reduction. For withholding, [RIRPF art. 84](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a84) ignores LIRPF art. 61.2's relative-return condition and counts descendants by **half**, unless the worker alone has the whole entitlement. Establish the actual entitlement and applicable division for ascendants/disability as well.

### Pay floors and contribution inputs

| Item | 2026 amount/rule | Official source |
|---|---|---|
| SMI | 1,221/month or 40.70/day; annual compensation/absorption floor 17,094, full legal working time | [RD 126/2026 arts. 1/3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-3815#a1) |
| General contribution ceiling | 5,101.20/month, with group/daily minimums | [Order PJC/297/2026 arts. 2/3](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a2) |
| Employee ordinary CC / lower unemployment / training / MEI | 4.70% /1.55% /0.10% /0.15% on their respective bases | [Order arts. 4/16/33](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296#a3-5) |
| Employer ordinary CC / lower unemployment / FOGASA / training / MEI | 23.60% /5.50% /0.20% /0.60% /0.75%, plus actual AT/EP tariff and any solidarity | [Order arts. 4/16/17/33](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296) |

These SMI amounts apply from 1 January through 31 December 2026 and are prorated for shorter working time. Collective-agreement wages can be higher. The annual figure paid in twelve equal instalments gives a **derived** 1,424.50/month; it is not the published 1,424.40 contribution floor. Do not substitute one for the other. Receiving the SMI does not by itself establish zero withholding: test the actual art. 81 limits and full algorithm, keeping any annual-return credit separate.

## The base

### 1. Establish annual remuneration and taxable payment components

Under [RIRPF art. 83.2](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a83), use cash plus valued in-kind remuneration expected from this payer for the calendar year. Include foreseeable variable pay, normally at least last year's variable amount unless an objectively lower figure is supported. Exclude the specified employer pension contributions and arrears attributable to prior years. In-kind remuneration enters this annual input at its [LIRPF art. 43](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a43) value **without** adding the payment on account. Sporadic daily manual workers have the article's daily-pay ×100 rule. New starters use expected pay for their actual remaining engagement, not an automatically invented full-year salary.

Keep separate salary, exempt reimbursements, social benefits, in-kind value and arrears. Tax exemptions under [LIRPF arts. 7/42](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a7) differ from social-security exclusions. Applying IRPF to every item in total devengado would incorrectly tax exempt items.

### 2. Compute the withholding base mechanically

Follow [RIRPF art. 83.3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a83):

1. Subtract qualifying art. 18/transition irregular-income reductions and the employee contributions in art. 83.3.b. Retain the prior five-year reduction history and declared exceptions where relevant.
2. Calculate R for the employment reduction **before** other employment expenses. Apply the piecewise table above; cap the reduction at R. Other expenses under art. 19.2.f have the separate cap of remuneration less art. 83.3.a/b amounts. Do not deduct union dues, professional-college dues or legal defence as automatic payroll-rate inputs merely because they can affect the annual return.
3. Subtract the capped other expenses and employment reduction. Also subtract 600 for qualifying pension/Clases Pasivas status or more than two qualifying descendants, and 1,200 for unemployment benefits; the art. 83.3.e reductions are compatible.
4. Deduct a notified judicial compensatory pension to the spouse under art. 83.3.f. Floor the resulting withholding base B at zero.
5. Compute personal/family minimum M under the national amounts and withholding-specific entitlement rules. A regional annual-return minimum does not replace this reference minimum ([art. 84](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a84)).

### 3. Calculate the quota and rate

For the ordinary case, `Q = max(T(B) −T(M), 0)`. If judicial child-support annuities A apply **without entitlement to those children's minimum**, and A <B, use `Q = max(T(A) +T(B −A) −T(M +1,980), 0)` instead. When annual remuneration G ≤35,200, limit Q to `0.43 ×max(G −applicable_art81_limit, 0)` ([RIRPF art. 85](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a85)).

Apply the no-withholding exclusion unless a fixed/minimum rate overrides it. For ordinary positive G, calculate `rate = 100 ×Q/G`; if B −M ≤0, the ordinary rate is zero. Apply qualifying territorial reduction and the notified two-point transitional mortgage reduction, without going below zero, then the statutory contract floor. For G=0 there is no ordinary cash withholding to compute; do not divide by zero. Use fixed-rate income's own rule instead of this annual calculation ([arts. 80–86](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a86)).

The official 2026 calculation specification **truncates the percentage to two decimal places**, rather than rounding it up. Its final monetary rounding treats half a cent upwards. Retain precision until the designated rounding/truncation step. AEAT publishes separate specifications for **1 January–9 September** and **from 10 September 2026**; choose the dated version and preserve its input/output record. These implementation details are checked against the [AEAT 2026 specification](https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/Algoritmo%20Retenciones-2026_10sept.pdf), alongside the statutory procedure.

### 4. Recalculate when facts change

[RIRPF art. 87](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a87) covers pay/expense changes, contract continuation or re-engagement in the year, new pension, relevant family/disability/mobility changes, judicial payments, spouse-income change, residence and mortgage changes. Recompute the annual quota using the **new annual forecast**, subtract withholding/payment on account already applied, and divide the remaining quota by the year's **remaining remuneration**, multiplying by 100. If negative, use zero; do not refund earlier withholding through this routine recalculation. Apply applicable floors and the 47%/territorial cap.

If mortgage reduction was used, art. 87.3.b requires the specified counterfactual prior-withholding treatment before the renewed reduction. If IRNR residence changes or territorial treatment changes mid-year, use the article's credit/period allocation rather than treating every earlier payment as taxed under the new status. Art. 87.5 also prevents an increase where only base-minus-minimum decreases and limits the increase attributable to an exclusive increase of that amount. Retain old/new B, M, rate and annual quota to test these constraints.

Apply pay changes from their occurrence; apply employee-notified changes with the article's minimum five-day lead before payroll preparation. The payer can elect the permitted April/July/October regularisation schedule for preceding-quarter changes. A worker can request a higher rate under [art. 88.5](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a88); do not lower the legal calculation merely because the worker prefers it.

### 5. Complete gross-to-net and employer cost

Use [es-social-contributions](es-social-contributions.md) to compute separate CC and AT/EP bases, extra-pay proration, contributions, overtime and solidarity. In the simple indefinite-contract case with the same uncapped base for every employee component, the **derived** employee sum is 6.50%. Exceptions, different bases or solidarity require the individual components. Summing verified components is valid arithmetic; label an aggregate as derived and state its assumptions.

Apply the withholding rate to **taxable cash remuneration** paid, with a separate payment on account for in-kind employment remuneration under [RIRPF art. 102](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a102). In the annual tax certificate, [LIRPF art. 43.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a43) adds employer-borne payment on account to in-kind value unless charged to the worker. Do not add that employer-borne tax to the cash salary or include it twice in the annual rate forecast.

`cash_net = cash_pay + exempt_cash_reimbursements −employee_SS −cash_IRPF −employee_charged_in_kind_payment_on_account −lawful_cash_deductions`. If starting from a total-accrual payslip that includes in-kind value, remove that value once in reaching cash net. `employer_cost = gross_remuneration + employer_SS + employer_borne_payment_on_account + other_actual_employer_costs`, keeping reimbursed disbursements and contributions payable separate in the ledger. Neither formula makes a tax-exempt item automatically exempt from contributions.

### Employment rules feeding payroll

- **Extra pay and wage in kind.** [ET arts. 26/31](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#a31) provide two annual extra payments; the collective agreement sets amount and permits twelve-month proration. For contributions, extra pay is prorated whether or not paid monthly. Pay in kind cannot exceed 30% of salary or reduce the full cash SMI.
- **Working time and overtime.** [ET arts. 34/35](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#a34) set an ordinary average maximum of 40 effective hours/week annually, 12-hour interday rest and the qualified daily/break rules. Overtime pay cannot be below ordinary-hour value; absent agreement use paid rest within four months. The 80-hour annual limit is proportionately reduced for shorter annual working time and excludes the statutory emergency/rest-compensated hours. Use the applicable agreement rather than invent overtime/night premiums.
- **Leave and benefits.** [ET art. 38](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#a38) requires at least 30 calendar days' paid annual leave. Current [art. 48.4–5](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#a48) gives 19 weeks' birth/adoption-related suspension, 32 for the specified sole-parent situation, with its compulsory/deferred portions and special extensions. Obtain the event/award dates and transition rule for a historical event; do not make all weeks employer-paid wages.
- **Ending employment.** The [ET art. 49.2](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#a49) settlement includes outstanding pay, accrued extra pay and unused holiday as applicable. Unused holiday paid on termination has the complementary contribution treatment in [LGSS art. 147.1](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a147). Objective termination and unfair-dismissal formulas are respectively 20 days/year capped at 12 monthly payments and 33 days/year capped at 24, subject to the actual legal route and legacy service transitions ([ET arts. 53/56](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#a53)). Establish legal cause, service dates and the applicable daily salary before calculating; do not equate every settlement with exempt severance. [LIRPF art. 7.e](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a7) sets the tax exemption conditions and 180,000 ceiling.

For part-time, concurrent-employment and suspension periods, apply the dedicated contribution-base methods in [es-social-contributions](es-social-contributions.md#the-base), then use those actual employee contributions in the annual rate forecast. Detailed severance transitions, special contribution systems and individual benefit-award computations require their specific verified facts.

## Deadlines and filing

| Obligation | Timing/record | Source |
|---|---|---|
| Pay and payslip | Contractual/agreed date; ordinary periodic remuneration interval no longer than a month | [ET art. 29](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#a29) |
| Payslip model | Monthly receipt with accruals, deductions, contribution bases and employer contribution detail; approved model or lawful alternative | [1994 payslip order art. 1/annex](https://www.boe.es/buscar/act.php?id=BOE-A-1995-912#a1) |
| Payslip archive | Minimum five years with contribution records | [Payslip order art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-1995-912#a3) |
| Social contributions | Employer contribution period paid in following month; reconcile RED settlement/RLC/RNT | [RD 1415 art. 56](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836#a56) |
| Modelo 111 | First twenty calendar days of April/July/October/January for previous quarter, or monthly where statutory conditions apply | [RIRPF art. 108.1](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a108) |
| Modelo 190 and certificates | Annual electronic-summary January window under applicable form rules; certificate before IRPF return period opens | [Art. 108.2–3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a108) |

Monthly 111 filing does not follow headcount: art. 108 refers to the RIVA art. 71.3.1/2 circumstances and the specified public-administration budget test. Use the actual filing obligation and official calendar/direct-debit cut-off in [es-modelo-111](es-modelo-111.md). Paid income that legally produces zero withholding can require a negative return; a period with no subject payments does not require an empty negative 111. Reconcile paid/accrued payroll timing with withholding's payment trigger rather than copy the contribution month without checking.

## Penalties and interest

For TGSS, use the [LGSS arts. 30–31](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#a30) 10%/20%/35% payment-timing/data-duty rules and interest computation in [es-social-contributions](es-social-contributions.md). They are not the AEAT rules for Modelo 111.

For an unprompted late tax return with tax due, [LGT art. 27](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27) generally uses 1% plus 1% for each complete month of delay up to twelve months, and 15% after twelve months with the specified subsequent interest; apply its notification, exception and reduction conditions. A failure to remit withholding can instead engage the conduct/amount-based [art. 191](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a191) penalty, not a universal flat 50%. Use the separate collection surcharges under [art. 28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a28) only for the relevant enforcement stage. Documentary/annual-return failures require their own classification.

Late wages have the separate **10% salary-debt interest** rule in [ET art. 29.3](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430#a29). Do not confuse it with the contribution surcharge or tax interest. Keep principal, interest, penalty and surcharge distinct.

## Cross-border points

Determine tax residence, work location, payer status and the applicable withholding administration before selecting IRPF, IRNR or the impatriate route. A foreign employer or bank account does not alone remove Spanish obligations. A residence change can trigger regularisation and credit for the specified IRNR amounts under [RIRPF art. 87.3](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a87). Do not apply the ordinary resident scale to a documented special-regime/non-resident payment.

For qualifying Ceuta/Melilla income use the territorial rules above. [LIRPF DA 57](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#da-8) extends the specified treatment to La Palma for 2026 with its **10 September withholding commencement**, reflected in AEAT's second dated specification. The payer may use the statutory option to implement the recalculation in the first payment from the following month, October 2026. Do not amend January–9 September payroll merely because annual territorial relief covers the year; apply the required prospective recalculation to the remaining payments. A mid-year residence/work-location change requires the art. 87 period computation.

For posted or multi-state workers, determine applicable social-security legislation before Spanish deductions, using the gateway in [es-social-contributions](es-social-contributions.md). A tax treaty is not a contribution exemption. Foral withholding remains outside this common-territory algorithm; preserve common social contributions and select the correct foral tax computation separately.

## Two worked examples that recompute

### 1. Ordinary full-time salary: annual rate and monthly net pay

A hypothetical employee under 65 has declared situation 3, no descendants/disability, no pension/mortgage/territorial adjustment, an indefinite contract and annual taxable pay **30,000 in twelve equal payments**, including prorated extras. Ordinary contribution bases equal monthly pay; verified exclusive-office facts meet the statutory 1.50% AT/EP occupation tariff. Employee contributions are a derived 6.50%, annual **1,950**. R is 28,050, so no employment reduction; subtract 2,000 other expenses to get B=26,050. `T(B)=5,980.50`, `T(5,550)=1,054.50`, Q=4,926. The 43% limit does not bind. Rate **16.42%** gives monthly IRPF 410.50, employee SS 162.50 and cash net **1,927.00**. Employer contributions are 803.75, cost **3,303.75**. Sources: [RIRPF arts. 81–86](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a83), [2026 contribution order](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296), [LGSS DA 61](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724#da-37).

```oa-check
name: Spain 2026 annual withholding rate to monthly net payroll
inputs:
  annual_pay: 30000
  minimum: 5550
steps:
  monthly_pay: annual_pay / 12
  annual_employee_ss: annual_pay * (0.047 + 0.0155 + 0.001 + 0.0015)
  reduction_income: annual_pay - annual_employee_ss
  base: reduction_income - 2000
  base_tax: 4225.50 + (base - 20200) * 0.30
  minimum_tax: minimum * 0.19
  raw_quota: max(base_tax - minimum_tax, 0)
  quota_limit: max(annual_pay - 15876, 0) * 0.43
  quota: min(raw_quota, quota_limit)
  rate: floor(quota / annual_pay * 10000) / 100
  monthly_withholding: monthly_pay * rate / 100
  monthly_employee_ss: annual_employee_ss / 12
  net_pay: monthly_pay - monthly_employee_ss - monthly_withholding
  employer_ss: monthly_pay * (0.236 + 0.055 + 0.002 + 0.006 + 0.0075 + 0.015)
  employer_cost: monthly_pay + employer_ss
expected:
  reduction_income: 28050
  base: 26050
  base_tax: 5980.50
  raw_quota: 4926
  quota: 4926
  rate: 16.42
  monthly_withholding: 410.50
  monthly_employee_ss: 162.50
  net_pay: 1927
  employer_ss: 803.75
  employer_cost: 3303.75
```

### 2. Mid-year pay rise: remaining quota over remaining pay

The same worker has received **15,000** and had **2,463** withheld before a rise. The revised calendar-year total is **36,000**, leaving 21,000 to be paid in six equal months. Revised annual employee SS is 2,340; B=31,660; the ordinary quota is **6,609**. Because annual pay exceeds 35,200, the 43% quota limit does not apply. Remaining quota 4,146 over remaining remuneration 21,000 gives **19.74% after truncation**. With monthly pay 3,500, SS is 227.50, IRPF 690.90 and net **2,581.60**. Projected annual withholding becomes 6,608.40; the 0.60 difference from the untruncated quota comes from the two-decimal rate. Retain the art. 87.5 comparison and do not promise the annual return is settled ([RIRPF art. 87](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a87)).

```oa-check
name: Spain 2026 ordinary pay-rise rate regularisation
inputs:
  revised_annual_pay: 36000
  pay_already_received: 15000
  tax_already_withheld: 2463
steps:
  revised_employee_ss: revised_annual_pay * 0.065
  revised_base: revised_annual_pay - revised_employee_ss - 2000
  revised_quota: 4225.50 + (revised_base - 20200) * 0.30 - 5550 * 0.19
  remaining_pay: revised_annual_pay - pay_already_received
  remaining_quota: revised_quota - tax_already_withheld
  revised_rate: floor(max(remaining_quota, 0) / remaining_pay * 10000) / 100
  monthly_pay: remaining_pay / 6
  monthly_ss: monthly_pay * 0.065
  monthly_tax: monthly_pay * revised_rate / 100
  monthly_net: monthly_pay - monthly_ss - monthly_tax
  projected_annual_withholding: tax_already_withheld + monthly_tax * 6
expected:
  revised_employee_ss: 2340
  revised_base: 31660
  revised_quota: 6609
  remaining_pay: 21000
  remaining_quota: 4146
  revised_rate: 19.74
  monthly_tax: 690.90
  monthly_net: 2581.60
  projected_annual_withholding: 6608.40
```

## Ask the client first

1. What contract, dates, working time, collective agreement and contribution classification govern this worker?
2. What cash/in-kind/variable/extra pay, prior-year arrears and exempt reimbursements are expected for this calendar year?
3. What signed family, disability, mobility, judicial-payment, mortgage and residence declarations support the rate inputs?
4. What contribution group, actual CNAE/occupation, overtime and coverage records establish each employee/employer amount?
5. For a change, what pay and withholding have already occurred, what old B/M/rate applied, and when was the change communicated?
6. What tax administration, 111 filing obligation and accepted payroll/contribution/annual-summary records apply?

## Sources

| Official source | Scope read | Read on |
|---|---|---|
| [RD 439/2007, RIRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | Arts. 80–88, 102/108: ordinary/fixed/minimum rates, base, family rules, quota, recalculation and payment/filing duties | 2026-10-26 |
| [Ley 35/2006, LIRPF](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) | Exemptions, employment expenses, in-kind valuation, national minima, judicial support and dated La Palma provision | 2026-10-26 |
| [AEAT 2026 withholding index](https://sede.agenciatributaria.gob.es/Sede/Retenciones.shtml), [January specification](https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/ALGORITMO_2026.pdf), [10 September specification](https://sede.agenciatributaria.gob.es/static_files/Sede/Programas_ayuda/Retenciones/2026/Algoritmo%20Retenciones-2026_10sept.pdf) | Dated implementation versions and rate truncation/monetary rounding; checked against the statute | 2026-10-26 |
| [Orden PJC/297/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-7296), [LGSS](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11724) | Contribution inputs, capped bases, occupation tariff, employer/worker shares and untaken-holiday contributions | 2026-10-26 |
| [RD 126/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-3815), [Estatuto de los Trabajadores](https://www.boe.es/buscar/act.php?id=BOE-A-2015-11430) | Wage floor, extra pay, in-kind salary ceiling, working time, leave, settlement and wage-debt interest | 2026-10-26 |
| [1994 payslip order](https://www.boe.es/buscar/act.php?id=BOE-A-1995-912), [RD 1415/2004](https://www.boe.es/buscar/act.php?id=BOE-A-2004-11836) | Payslip/model/archive and contribution payment period | 2026-10-26 |
| [Ley 58/2003, LGT](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) | Tax late-return, collection and underpayment classification | 2026-10-26 |

**Not yet confirmed:** complete foral/non-resident/impatriate payroll routes; special-system contribution computations and case-specific suspension exemptions; historical severance/leave transitions for an individual event; the applicable collective agreement and occupational tariff for any actual worker. No live-AEAT-service parity run has yet been performed for these two hypothetical examples. Independent whole-pack review remains outstanding.

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
