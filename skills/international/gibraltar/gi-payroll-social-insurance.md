---
name: gi-payroll-social-insurance
description: >
  Prepare ordinary monthly payroll controls using the social-insurance schedule effective 1 July 2026. Special contribution classes, partial periods, employment-law entitlements and cross-border coverage require their own determination. This source-cited draft supports preparation of reviewable working papers using the stated periods, evidence requirements and computation examples. Retain source evidence and effective dates; unresolved points and professional review remain explicit. Use the linked official materials when checking a case, and obtain a qualified local review before filing or making a payment. Read the explicit exclusions before applying its calculations to different facts.
jurisdiction: GI
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.2
verified_by: pending
sources:
  - url: "https://www.gibraltar.gov.gi/income-tax-office/employers-and-trusts/employers"
    title: "Income Tax Office: employer registration and obligations"
    as_of: "2026-10-22"
  - url: "https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Employers/P8%20SUBMISSION%20GUIDE%202025-2026.pdf"
    title: "Electronic P8 submission guidance 2025/2026"
    as_of: "2026-10-22"
  - url: "https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Self-Employed/Social%20Insurance%20Contributions%20Class%202026-2027x.pdf"
    title: "Social Insurance Contributions Class 2026/2027"
    as_of: "2026-10-22"
---

# Gibraltar payroll and social insurance v0.2

> **Source-cited draft.** Professional review is pending. Figures are limited to the periods and assumptions below. This Guide prepares working papers; it is not authority to file or pay.

## Scope

Prepare ordinary monthly payroll controls using the social-insurance schedule effective 1 July 2026. Special contribution classes, partial periods, employment-law entitlements and cross-border coverage require their own determination.

Sources were accessed on 22 October 2026. A dated rate table controls its stated period; an undated guidance page does not prove that all later amendments have been incorporated.

## Registration and reporting

Register each employee and obtain the ITO code. Remit deducted tax and social insurance by the 15th of each month. Annual P8, P10/P10A and P12 reporting is due by 31 July. Give a leaver P7A and an annual P7 certificate. Retain submission and payment receipts. [ITO employers, obligations section](https://www.gibraltar.gov.gi/income-tax-office/employers-and-trusts/employers).

### Registration and leaver evidence

For company PAYE registration, the ITO requests employment-registration and incorporation certificates, a request addressed to the Commissioner and the PAYE commencement date. Employee registration needs the employment contract and identification; an employer requesting the employee's tax code also needs the employee's signed authority. Keep employer and employee registration evidence separately. For leavers, send P7A part 1 to the ITO and give parts 2 and 3 to the employee. [ITO employer questions and answers](https://www.gibraltar.gov.gi/income-tax-office/employers-and-trusts/employers).

### Annual P8: period and reconciliation controls

The **2025/26** P8 guidance covers 1 July 2025–30 June 2026; the employer page gives 31 July 2026 as its deadline. Do not label it the 2026/27 return. [ITO](https://www.gibraltar.gov.gi/income-tax-office/employers-and-trusts/employers).

Match employee identity and contribution class to P3. Exclude unpaid weeks and start a new entry when the contribution class changes. Keep the company's numeric taxpayer reference distinct from its PAYE employer reference. An active PAYE employer paying no salary still submits a nil P8. [2025/26 P8 guidance, pages 7–11 and 17](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Employers/P8%20SUBMISSION%20GUIDE%202025-2026.pdf).

Reconcile tax deducted and both SI components to actual remittances, not amounts merely accrued. The form separately captures tax and SI already paid. Example: assumed annual deductions of £4,800 PAYE and £2,000 employee SI, plus £2,800 employer SI, compared with payments of £4,500 PAYE and £4,600 SI, leave **£300 PAYE and £200 SI** outstanding. The totals are illustrative, not annual contribution caps. [P8 guidance, pages 13–14](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Employers/P8%20SUBMISSION%20GUIDE%202025-2026.pdf).

The completed declaration generates an XML file for submission through tax.egov.gi. Saving the workbook alone does not submit the return. Retain the submitted file and receipt. [P8 guidance, page 16](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Employers/P8%20SUBMISSION%20GUIDE%202025-2026.pdf). Screenshots contain older year labels; use the explicit 2025/26 period and verify the selected filing year before submission.

## Monthly ordinary contribution table

For the ordinary earnings-related class, the published schedule effective **1 July 2026** gives:

| Contributor | Rate | Monthly minimum | Monthly maximum |
|---|---:|---:|---:|
| Employee | 10% | £62.11 | £176.76 |
| Employer | 18% | £138.55 | £243.65 |
| Self-employed, separate SE class | 20% | £131.95 | £232.05 |

[ITO 2026/27 contribution-class schedule](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Self-Employed/Social%20Insurance%20Contributions%20Class%202026-2027x.pdf). The schedule contains separate pensioner, married-woman, trainee and exemption classes. Do not assign them from age or job title without confirming the issued class and eligibility.

## Computation

1. Confirm class, pay frequency, full/partial period, and earnings base before selecting a schedule.
2. For a confirmed full-month ordinary class, compute employee `min(176.76, max(62.11, earnings × 10%))` and employer `min(243.65, max(138.55, earnings × 18%))`.
3. Use the employee's tax code and correct-year official tax tables for PAYE. Contribution rates are not income-tax rates.
4. Reconcile gross wages, PAYE, employee contributions, other deductions, net wages and employer cost separately.
5. Reconcile payroll totals to remittances and the annual return. Never multiply a rounded monthly cap to substitute for an official annual table.

**Examples:** full-month ordinary gross earnings £3,000 give employee SI **£176.76**, employer SI **£243.65** and gross-plus-employer-SI **£3,243.65**, before other employer costs. At £1,000, the respective amounts are **£100** and **£180**. A person with an exemption code must not be put through this formula.

## Evidence and exclusions

A detached-worker exemption needs the relevant coverage evidence. A pensioner, trainee, second job or self-employed worker needs the appropriate class. Refer to the complete schedule and the ITO's [social-insurance explanation](https://www.gibraltar.gov.gi/income-tax-office/individuals-and-employees/social-insurance).

The annual P8 controls above do not resolve PAYE table selection, cumulative adjustments, corrections after submission or statutory penalties. No live return was submitted or tested. This draft does not calculate minimum wages, leave, redundancy, pension contributions or benefit-in-kind valuation. Preserve those as separate review lines rather than representing gross-plus-SI as total employer cost.

## Self-checks and output

- Retain the relevant source version, the applicable period and the facts establishing scope.
- Reconcile every input to the client's records; keep estimates separate from actual amounts.
- Recompute the example and boundary cases before applying the method.
- Record exclusions and unresolved points explicitly. Do not convert a missing source into an exemption.
- Deliver a calculation, evidence list, filing calendar and reviewer questions. Record the exact revision reviewed.

## Disclaimer

General tax and accounting reference material only. These drafts have not been professionally attested. A qualified professional in the relevant jurisdiction must check the facts, current law, elections and deadlines before anyone files, pays or acts on an output.
