---
name: fo-corporate-income-tax
description: >
  Prepare a 2026 Faroese ordinary corporate income tax computation for P/F and
  Sp/F companies. Check the 18% rate conditions, reconcile accounting profit,
  test carried losses, distinguish group and capital-income regimes, and build
  the filing and payment calendar. Special industries, treaty relief and full
  capital-income calculations remain outside this source-cited draft.
jurisdiction: FO
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
review_status: pending_review
---

# Faroe Islands corporate income tax v0.1

## Who this applies to

This Guide prepares ordinary income-tax working papers for Faroese P/F and Sp/F companies. Faroese registration brings companies with limited-liability participants within Tax Act §1(1)(8); §1(2) also covers relevant foreign-registered entities whose effective management is in the Faroes. Treaty residence requires separate analysis. [Tax Act][tax]

It does not compute capital-income tax, shareholder distributions, petroleum tax, fishing/resource charges, aquaculture surcharges, tonnage taxation, reorganisations or minimum-tax exposure. Identify those activities before using the ordinary calculation. An 18% result here is not necessarily the company's complete tax liability.

**Period:** income year 2026, sources read 23 October 2026. The Tax Act consolidation identifies amendment 53 of 1 June 2026, effective 1 September 2026. Event-specific rules must be matched to the event date.

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Ordinary qualifying company rate | 18% | Assessment Act §5(2) |
| Capital condition in §5(2) | Relevant share/paid-in/guarantee/cooperative capital at least DKK 50,000 for the specified entities | Same |
| Entrepreneur companies | Separately included in §5(2) | Same |
| Residual rate under §5(1) | 49%; do not apply automatically without checking the exceptions in §5(2)–(4) | Same |
| Petroleum-income exception | 27% for the specified Hydrocarbon Tax Act §4 income; excluded here | §5(4) |

[Assessment Act][rate]. The 18% is the combined national and municipal amount; the 70%/30% allocation divides that tax, not additional tax rates. TAKS also describes the 18% treatment for specified funds and insurers, which this ordinary-company Guide does not analyse. [TAKS company-tax guidance][taks]

## The base

Start with a reconciled trial balance and a separate tax-adjustment schedule. Operating expenditure incurred to earn, secure and maintain income is addressed by Tax Act §31. Tax depreciation is governed separately, so an accounting depreciation charge is not its own tax deduction. Check business interest under §33 and related-party restrictions under §37b before allowing it. [Tax Act][tax]

Working-paper sequence:

1. Identify the entity, period and applicable rate provision.
2. Reconcile revenue, costs and accounting profit to signed accounts and ledgers.
3. Separate ordinary income from capital-income items and special regimes; document the legal classification for each material item.
4. Reverse accounting charges that require separate tax treatment; insert only deductions supported by the applicable law and schedules.
5. Establish the allowable loss balance, then apply it against positive ordinary taxable income. Preserve the unused balance by origin year and entity.
6. Multiply the resulting ordinary taxable income by the established rate. Reconcile the assessment and actual payment notices separately.

### Losses

Section 33a allows forward deduction, using available earlier profits before carrying losses to a later year. Company losses are forfeited under its ownership-continuity rule if at least 50% of capital or voting value is not in the same hands at the beginning of the utilisation year as at the end of the loss year. The statute preserves an exception where the company carried on significant business activity involving economic risk when ownership changed. Do not treat every share sale as automatic forfeiture. [§33a(1)–(2)][tax]

Debt cancellation/reduction also reduces losses; debt-to-equity conversion uses the difference between face and market value, with adjustment for debt-release income taxed. Review the transaction before using the old loss balance. [§33a(3)][tax]

TAKS describes ordinary-income losses as deductible in the capital-income return but not the reverse. Do not combine the two bases into a single net-profit figure. The exact capital-income ordering and computation remain outside this Guide. [TAKS][taks]

### Group taxation

Regulation 148/2015 requires eligible Faroese-registered entities, matching financial years and full subsidiary ownership throughout the subsidiary's income year. Application is written, ordinarily by 1 July following the first relevant year, with returns/accounts submitted before consideration. Companies in liquidation cannot obtain permission; liquidation ends their participation from that income year. Section 4(4) prohibits renewed permission after departure. Treat approval as evidence, not an assumption. [Regulation §§1–5][group]

Each company computes its own result. Pre-group losses first offset its own profit; the regulation prescribes further ordering involving its own capital income and group-period losses before group allocation. Do not transfer an acquired company's pre-group loss directly to its parent. The parent reports the joint result; §9 requires intercompany tax/loss compensation to be paid or booked by 1 October following the income year. [§§6–9][group]

This is a screening summary, not a complete group-loss calculator. Capital-income grouping requires its own authority and review.

## Deadlines and filing

Company returns are ordinarily due **1 July following the income year** under §100(3). For a calendar-year 2026 company, that means 1 July 2027. A permitted extension cannot exceed **15 August** under §105. [Tax Act][tax]

TAKS requires company accounts with the return, including exempt companies; accounts must be submitted on Borgaragluggin. Retrieve the current return and accounting template and retain submission receipts. [TAKS returns][returns]

Ordinary company tax falls due in three payments on **1 October, 1 November and 1 December**, with payment permitted through the **20th** of each month. Use the assessed year and issued amounts; do not substitute the return deadline for the payment calendar. [Tax Act §81][tax]; [TAKS][taks]

New-company first periods and cessation have separate §21 rules. This Guide does not supply an incorporation/closure calendar; resolve it before applying the ordinary-year example.

## Penalties and interest

Section 104 provides estimated assessment for a missing timely complete return, a DKK **1,000–5,000** fine, and income-tax increases of **2%** when less than seven days late or **5%** when seven or more days late. Relief requires a supported application under subsection 3. [Tax Act][tax]

Section 81(2) states ordinary late-payment interest of **0.7% per commenced month**, subject to §146(1). That latter provision addresses specified offence penalties and underpaid tax, with **12% annual interest** for the specified companies. Do not stack or substitute these mechanically. TAKS's short guidance describes the ordinary calculation from the timely-payment date, whereas §81 says the due date; obtain the assessment's calculation if the start-date distinction affects the charge. [Tax Act][tax]; [TAKS][taks]

## Cross-border points

Foreign incorporation does not settle residence where effective management is Faroese. Foreign businesses require a separate domestic-source/PE and treaty analysis under §§1–2. Controlled transactions and thin capitalisation require their own schedules; see the transfer-pricing Guide. Foreign tax credits, participation relief, withholding and treaty procedures are unresolved here. [Tax Act §§1–2, 37a–37b][tax]

## Two worked examples that recompute

### 1. Ordinary profit bridge

Assume a qualifying 18% company, no special regime or capital-income items, accounting profit DKK 600,000, accounting depreciation DKK 80,000 and independently verified tax depreciation DKK 100,000. The ordinary base is DKK 580,000 and tax DKK 104,400. The depreciation input is a case assumption, not a rate established by this Guide.

```oa-check
name: Faroese ordinary company profit bridge
inputs:
  profit: 600000
  accounting_depreciation: 80000
  verified_tax_depreciation: 100000
  rate: 0.18
steps:
  taxable: profit + accounting_depreciation - verified_tax_depreciation
  tax: taxable * rate
expected:
  taxable: 580000
  tax: 104400
```

### 2. Loss use and a failed continuity condition

A qualifying company's ordinary profit before loss relief is DKK 300,000, with DKK 500,000 verified carried losses. If the losses survive §33a and no other adjustment applies, DKK 300,000 is used, ordinary tax is zero and DKK 200,000 remains. If ownership continuity fails and the significant-business exception does not apply, assume the whole DKK 500,000 is forfeited: tax is DKK 54,000 and no such loss remains. This is a conditional comparison, not a factual finding about a share transfer.

```oa-check
name: Faroese loss eligibility changes the result
inputs:
  profit: 300000
  eligible_loss: 500000
  rate: 0.18
steps:
  used: min(profit, eligible_loss)
  taxable: max(0, profit - used)
  tax: taxable * rate
  remaining: eligible_loss - used
  tax_if_forfeited: profit * rate
expected:
  used: 300000
  taxable: 0
  tax: 0
  remaining: 200000
  tax_if_forfeited: 54000
```

## Ask the client first

- What are the legal form, relevant capital, registration and actual management location?
- What are the financial year and incorporation/closure dates?
- Which items involve capital income, special industries or foreign operations?
- What are the loss-year balances, ownership histories and debt restructurings?
- Is group taxation approved, and were all ownership and period conditions met?
- What returns, assessments, extension decisions and payment notices have been received?

## Review limits

Source-cited draft, not professional attestation. Asset-specific depreciation, capital-income computation/grouping, shareholder distributions, special industries, minimum-tax applicability and treaty relief remain open. Neither the examples nor this file establish comprehensive corporate or country coverage.

## Sources

All read 23 October 2026.

| Source | Locator |
|---|---|
| Consolidated Tax Act | [§§1–2, 21, 31, 33a, 37a–b, 81, 100, 104–105, 146][tax] |
| Assessment Act | [§5][rate] |
| TAKS company tax | [Rates, losses and payment guidance][taks] |
| Group taxation regulation 148/2015 | [§§1–9][group] |
| TAKS returns | [Company filing procedure][returns] |

[tax]: https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt
[rate]: https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170
[taks]: https://www.taks.fo/fo/vinna/skattur/partafelagsskattur
[group]: https://logir.fo/Kunngerd/148-fra-18-12-2015-um-samskatting-av-felogum
[returns]: https://www.taks.fo/en/individuals/tax/tax-return
