---
name: fi-employer-payroll
description: >
  Prepare Finnish employer payroll reporting for 2026: distinguish earnings
  payment reports, the employer's separate report and tax payment; calculate
  the employer health-insurance contribution for eligible wages. Pension,
  unemployment, accident coverage and full withholding review remain open.
jurisdiction: FI
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
---

# Finland employer payroll reporting v0.1

## Who this applies to

This draft addresses the ordinary business-employer electronic reporting cycle. Household, paper-filing, non-cash-only, international and other exceptional cases require separate rules. It does not replace the worker-status, tax-card, wage-base or insurance assessment before payroll.

Reporting deadlines are linked to when the worker can use the payment, rather than when the work was performed. A different employer tax period does not extend the earnings-report deadline. [Incomes Register deadlines][deadlines]

## Rates, bands and thresholds

Vero publishes a **1.91% employer health-insurance contribution for 2026**, compared with 1.87% for 2025. Its guidance covers employees aged 16–67 who are insured in Finland under the relevant health-insurance rules. Determine the applicable wage base and coverage before multiplying. [Social insurance contributions][insurance]

The employer contribution can apply even when withholding is zero or remuneration consists of benefits. The employee's insured-person health contribution is included in the withholding rate; do not deduct it again as a separate item. Vero distinguishes trade income from wages for this contribution. [Social insurance contributions][insurance]

The same official page lists pension, unemployment, occupational accident/disease and group life contributions separately. Their inclusion depends on the applicable coverage and other conditions. This Guide supplies no universal all-in employer percentage. [Social insurance contributions][insurance]

## Reports and deadlines

| Obligation | Ordinary electronic-reporting rule |
|---|---|
| Earnings payment report | Within five calendar days following payment availability |
| Employer's separate report | By the fifth of the following calendar month |
| Registered regular employer with no wages | Monthly separate report with the appropriate no-wages information |
| Casual business employer | Separate report for the relevant wage-payment months |

[Incomes Register deadlines][deadlines]. Weekends and holidays count within the five-day period; when the final reporting day falls on a weekend or holiday, the guidance permits the following business day. Verify the particular calendar and exception before fixing the due date.

The separate report carries the employer health contribution and relevant adjustments; it does not replace each worker's earnings details. Preserve both submission confirmations and reconcile their periods to payroll. [Employer reporting guidance][reporting]

## Payment is a separate step

For an ordinary monthly tax period, Vero's instructions direct payment of withholding and employer health contributions to the Tax Administration by the twelfth of the following month. Longer authorised tax periods affect payment timing; determine the employer's actual period rather than assuming one. Filing the earnings report is not itself evidence of payment. [Reporting/payment guidance][reporting]

Confirm the applicable business-day treatment, tax references and MyTax balance before delivery. Other insurers' contribution invoices have separate payment routes. This draft has not tested a live payroll submission, account or bank payment.

## Preparation workpaper

Use this practical checklist alongside the verified payroll rules for the actual employee:

1. Establish worker classification, residence, insurance status and payment date.
2. Reconcile cash wages, benefits, expenses and the bases used for each deduction/contribution.
3. Apply the valid withholding instruction and separately supported employee deductions.
4. Prepare each worker's earnings report and the employer's monthly separate report.
5. Reconcile submissions, payslips, net cash, tax liabilities and insurer invoices.
6. Retain acceptance confirmations, payment evidence and correction records.

This checklist is preparation practice, not a complete statutory payroll specification. Wage and benefit valuation, tax cards, pensions, unemployment coverage, collective agreements and termination payments still need substantive checks.

## Worked example

Assume EUR 20,000 is the correctly established eligible employer-health contribution base for 2026, with no adjustments. At 1.91%, the contribution is EUR 382. The example excludes other employer costs and does not determine whether a worker is insured.

```oa-check
name: Finland 2026 employer health contribution
inputs:
  eligible_contribution_base: 20000
  employer_health_rate: 0.0191
steps:
  employer_health_contribution: eligible_contribution_base * employer_health_rate
expected:
  employer_health_contribution: 382
```

## Ask the client first

- Who is paid, for what work, where, and on which payment dates?
- What are the worker's insurance status and valid withholding instructions?
- Which amounts are wages, benefits, expenses or trade income?
- Is the employer registered as regular, and what is its payment tax period?
- Which reports, corrections, insurer invoices and payments already exist?

## Sources and review limits

Official text retrieved through the search index on 23 October 2026:

- [Vero social insurance contributions][insurance], 2026 table and scope.
- [Incomes Register deadlines][deadlines].
- [Vero wage reporting and employer contributions][reporting].

Not yet confirmed: complete current statutory chain, employee withholding and benefit valuation, pension/unemployment/accident and group-life conditions and rates, cross-border insurance, exceptional reporting, sanctions and live correction/payment procedures. Independent review and professional attestation remain outstanding. Payroll and social-contribution coverage remain partial.

[insurance]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/being-an-employer/social-insurance-contributions/
[deadlines]: https://www.vero.fi/en/incomes-register/companies-and-organisations/deadlines-for-reporting/
[reporting]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/being-an-employer/how-to-report-wages-and-employers-contributions/
