---
name: is-corporate-income-tax
description: >
  Prepare Iceland corporate income-tax workpapers for 2026 for resident
  limited companies and other separately taxable legal entities. Determine
  the legal-form rate, reconcile accounting profit to the tax base, support
  deductions, depreciation, participation deductions and loss carryforwards,
  screen group taxation and related-party finance, and reconcile assessment
  payments. Includes the separately identified 2026 filing cycle for 2025
  income. Use for ehf., hf., taxable partnerships, RSK 1.04 and annual tax
  reconciliations. Sector taxes, foreign credits, restructurings, some financial
  instruments and independent Icelandic legal review require further work;
  this source-cited draft is not comprehensive country coverage.
jurisdiction: IS
category: international
tax_year: 2026
last_updated: 2026-10-23
version: 0.5
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland corporate income tax v0.5

## Who this applies to

Prepare **income-year 2026** workpapers for separately taxable Iceland-resident legal entities. Article 2 residence includes Icelandic registration, domicile under the constitution or actual management in Iceland. Confirm the legal form and separate-taxpayer status, including any partnership election; a business name alone does not establish the tax rate. Residents are taxed on worldwide income under Article 2. [Income Tax Act 90/2003, Article 2][law]

An individual's sole trade belongs in the [individual income-tax Guide](iceland-income-tax.md). Exempt bodies require Article 4 and Article 71(4)–(5) review: ordinary income-tax exemption does not itself settle capital-income tax. Non-residents require the source-category method in the [cross-border Guide](is-cross-border.md), rather than a blanket resident-company computation. [Articles 3–4, 70–71][law]

**Keep years separate.** A return labelled 2026 ordinarily reports **2025 income**. The official 2026 assessment page expressly uses that pairing. This Guide distinguishes the current 2026 income computation from confirmed 2026 filing/payment rules; no unissued 2027 deadline is inferred. [2026 assessment information][assessment]; [Article 59][law]

## Rates, bands and thresholds

Amounts are ISK. The rates below concern the ordinary statutory computation, before any applicable sector taxes or relief.

| Item | Rule for the stated period | Official source |
|---|---|---|
| Ordinary Article 2(1)(1)–(2) entities, including hf./ehf. | 20% of taxable income for 2026 | [Article 71(1)][law]; [2026 rates][rates] |
| Other separately taxable Article 2(1)(3)–(5) entities | 37.6% of taxable income for 2026 | [Article 71(2)][law]; [2026 rates][rates] |
| Dividends received by the specified higher-rate entities | Separate 22% treatment; do not apply 37.6% indiscriminately | [Article 71(3)][law] |
| Loss vintage | Unused qualifying trading losses from the ten years preceding the income year | [Article 31(8)][law] |
| Eligible closing business receivables/loans; inventory | Optional reductions up to 5%; reverse previously expensed prior-year reductions | [Article 31(3)–(4)][law] |
| Immediate expensing of an asset or asset group | Acquisition cost **below 600,000**, not equal to it | [Article 39][law] |
| Ordinary office equipment depreciation | 20%–35% of the statutory depreciation base | [Article 37(4)(a)][law] |
| Related-party financing, absent an exception | Excess above 100,000,000 limited to 30% of statutory profit; first 100,000,000 retained subject to ordinary deductibility | [Article 57b][law]; [2020 amendment](https://www.althingi.is/altext/stjt/2020.033.html) |
| Ordinary domestic group-tax ownership screen | At least 90%, with approval and further conditions | [Article 55][law] |
| 2026 assessment-year advances | 8.5% of 2025 assessed public levies at each due date; current guidance describes eight February–September payments totalling 68% | [Regulation 1370/2025, Articles 1–2][payment-reg]; [Advance-tax guidance][advances] |

Article 71(3) also imposes a separate 6% financial-activity tax on the defined in-scope taxpayers' base above ISK 1 billion, without group taxation or brought-forward losses for that calculation. This is a screening flag, not a complete sector-tax method. The 2024 exceptional 21%/38.4% ordinary rates in transitional provision LXXVI do not replace the 2026 rates. [Article 71(3), transitional provision LXXVI][law]

## The base

### 1. Reconcile income and timing

Start with a reconciled trial balance and statutory accounts. Identify trading receipts, interest, dividends, gains, foreign items and related-party transactions. Article 59 ordinarily recognises income when the claim arises, subject to its uncertain-income rule. Bank receipts alone do not establish the income year. Under Article 61(2), legal-entity taxable income is statutory income less deductions permitted by Article 31. [Articles 7–8, 59, 61][law]

Prepare a bridge from accounting profit **before tax**. Add back book depreciation and any expenses not permitted for tax; replace them with the supported statutory depreciation/deductions. Reconcile provisions, reserves, share income, exchange differences and losses separately. Keep income-tax payments and withholding credits in a payment schedule, not as deductions from taxable profit. [Articles 31–50, 61, 112][law]

### 2. Support deductions and adjustments

| Area | Workpaper rule | Source |
|---|---|---|
| Operating expenses | Evidence the cost, relevant year and connection to acquiring, securing or maintaining income. Missing required payroll/contractor reporting can lead to deduction denial under the stated procedure. | [Article 31(1)][law] |
| Bad debts | Distinguish business-connected debts demonstrably lost from an accounting provision. For an elected up-to-5% closing reduction, verify the eligible base and reverse the prior year's expensed reduction. | [Article 31(3)][law] |
| Inventory | Establish the Article 73 valuation first; calculate the optional up-to-5% reduction once and reverse the prior year's expensed reduction. Do not duplicate a book write-down and tax deduction. | [Articles 31(4), 73(4)][law] |
| Gifts/donations | Review Article 31(2)'s recipient registration, qualifying purposes and limits; do not deduct all gifts under the general expense rule. | [Articles 31(2), 50(1)][law] |
| Fines and unlawful payments | Article 50 disallows the specified criminal penalties, related unlawful-gain costs and unlawful payments. Classify the actual charge; this is not a blanket conclusion about every interest or fee item. | [Article 50][law] |
| Interest and FX | Apply Article 49's business connection and timing rules. Its net exchange-loss rule spreads the qualifying net loss equally over three years; a book loss is not automatically the same-year tax deduction. Review related-party interest separately under Article 57b. | [Articles 49, 57b][law] |
| Start-up and specified development costs | Article 32 permits the stated cost classes to be written down in the year incurred or equally over five years; classify the cost before choosing that treatment. | [Article 32][law] |

Retain invoices, contracts, allocation evidence, payroll filings and the reconciliation to each return field. These are preparation controls implementing the cited rules; they do not establish an expense's eligibility without its facts.

### 3. Depreciation and disposals

Build an asset register showing original cost, category, business use, first-use date, prior tax depreciation, opening tax value, additions, disposals and closing value. Articles 33–36 define depreciable assets, first use and the base. Movable assets under Article 33(1) use cost less prior depreciation; other specified classes use original cost. Do not apply the office-equipment rate to buildings or purchased intangibles. [Articles 33–37][law]

Selected statutory ranges are 10%–20% for the specified ships/passenger vehicles and aircraft, 10%–30% for industrial machinery, 20%–35% for office equipment and the stated other movables, 1%–3% for residential/office/retail buildings, 15%–20% for purchased intellectual-property rights and 10%–20% for purchased goodwill. Other building classes have their own ranges. Determine the precise class and business use before selecting a rate. [Article 37][law]

Article 39's immediate-expense threshold is strictly below ISK 600,000 for the asset **or asset group**. Articles 35 and 45 address disposal/cessation years; an ordinary annual charge is not automatically available then. Article 42 generally leaves a 10% original-cost residual for Article 33(1)–(2) assets. Reconcile disposal proceeds, tax value and any gain/loss under the relevant disposal provisions instead of simply deleting the asset. [Articles 12–27, 33–45][law]

### 4. Dividends, share gains and losses

Article 31(9) provides a deduction for qualifying dividends received by the specified entity classes. It extends to foreign dividends only under its foreign-tax and rate conditions. Article 31(9a) addresses qualifying share gains and states that excess share-sale losses are neither generally deductible from other income nor carried forward as trading losses. Retain recipient/issuer classifications, dividend decisions, holding/disposal schedules and the evidence supporting foreign treatment. A group relationship alone does not establish a participation deduction. [Article 31(9), (9a)][law]

Keep higher-rate entities' Article 71(3) dividend treatment separate. Do not assume that the limited-company deduction or ordinary 37.6% rate resolves every partnership's dividend receipt. [Articles 31, 71][law]

### 5. Trading-loss schedule

For a calendar 2026 computation, the ordinary preceding-ten-year window covers **2016–2025**, subject to adequate original reporting, unused balances and the change-of-ownership/business rules. A 2015 vintage is outside that ordinary window. Retain origin, opening balance, prior use, eligible amount used now and closing balance for each vintage. Article 31(8) restricts use after material business/activity changes unless the ordinary-business-purpose condition is established; age alone is insufficient. [Article 31(8)][law]

Separate share-loss restrictions, foreign CFC losses and pre-group losses. Mergers/splits also require Article 54's loss-transfer conditions; unused losses do not automatically follow a purchase or reorganisation. This Guide supplies no loss carryback claim. [Articles 31(9a), 54–55, 57a][law]

### 6. Group taxation and related-party finance

Article 55 group taxation requires authority approval, at least 90% ownership, the same accounting year and all-year ownership subject to the stated new-entity/closure exceptions. It normally lasts at least five years; the statute also restricts restarting after termination. Apply at least **30 days before the applicable return deadline**. Current-year results are settled before brought-forward losses; losses from before group taxation remain usable only in their originating company. Do not consolidate separate returns merely because management prepares group accounts. [Article 55][law]

### 7. Related-party interest limitation

First establish that a financing cost is otherwise deductible under Articles 31 and 49, then apply arm's-length terms under Article 57 and the separate Article 57b limitation. The limitation covers related-party interest and discounts; do not net unrelated interest income against that gross pool without a legal basis. Keep principal, counterparty, related status, dates, rates, discounts and charges in the financing schedule. See the [transfer-pricing method](is-transfer-pricing.md). [Articles 31, 49, 57–57b][law]

For the **amount above ISK 100 million**, deduction is limited to 30% of Article 57b profit. The first 100 million is not made subject to the cap merely because the pool exceeds it. This reading is confirmed by the enacted 2020 amendment and its official explanation: interest 300 million and statutory profit 400 million produce allowed interest **220 million** and disallowed interest **80 million**. [Article 57b][law], [Act 33/2020, Article 6](https://www.althingi.is/altext/stjt/2020.033.html), [bill 626/150, section 3.5](https://www.althingi.is/altext/150/s/0626.html)

Prepare these stages:

1. **Statutory profit:** start from annual-accounts profit; add income tax, the finance-item adjustment, depreciation and fixed-asset write-downs. Subtract within-group equity-method income and add distributed dividends from that same company where paid. Reconcile every signed adjustment to the accounts; a management “EBITDA” label is insufficient.
2. **Domestic-group exception:** establish Article 55 approval or eligibility and that every company in the relevant group is Iceland-resident. One resident lender alone is insufficient.
3. **Equity exception:** establish that the taxpayer's equity ratio is no more than two percentage points below its group's ratio. Use cost rather than equity-method carrying value for a group holding where Article 57b requires it. The exception does not apply to an equity increase less than six months before balance-sheet date reversed by a corresponding decrease less than six months afterwards.
4. **Financial-sector exception:** document whether the taxpayer falls within the statutory financial undertaking, insurer or specified owned similar-business category; do not exempt every group finance company by name.
5. **If no exception:** deduct the otherwise-eligible first 100 million plus the allowed part of the excess, capped at the actual interest pool. Record the disallowed amount as a tax adjustment. Article 57b states that excess is not deductible and supplies no carryforward permission; do not create an automatic deferred interest deduction.

[Article 57b(1)–(3)][law]

For a nonnegative established statutory profit, the arithmetic control is:

```text
excess_pool = max(0, related_interest_and_discounts − 100,000,000)
allowed = min(pool, 100,000,000) + min(excess_pool, statutory_profit × 30%)
disallowed = pool − allowed
```

A loss/negative statutory-profit case needs a documented local interpretation before a final calculation; this positive-profit control does not resolve that boundary.

### 8. Controlled foreign holdings

Article 57a's low-tax comparison is **less than two thirds of the Icelandic tax that would apply to the foreign entity's profit**, not simply a country's headline rate. Establish direct/indirect ownership or control throughout the year: the provision addresses at least half held by Icelandic taxpayers or management control during the year. Trace the taxpayer's proportionate interest and recompute the foreign profit under Icelandic rules, without waiting for distribution. [Article 57a][law]

Test the exceptions from evidence: a qualifying treaty/information-exchange case whose income is not mainly passive, or qualifying EEA/EFTA/Faroe establishment carrying on genuine business with the required information access or taxpayer disclosure. Location alone does not establish genuine activity. Ring-fence losses to that entity's profits and retain adequate loss support; do not use them against unrelated Icelandic operations. Keep a previously taxed-income/distribution ledger to avoid taxing the same included profit again, subject to Article 57a's excess-distribution rule. The following implementation stages apply alongside the current statute. [Article 57a][law]

**CFC workpaper under Regulation 1102/2013.** Reconcile the foreign accounts to Icelandic income/deduction rules for the comparable legal form, then compare actual foreign income tax with two thirds of the resulting hypothetical Icelandic tax. Multiply ownership along each indirect chain, aggregating the relevant Icelandic holdings/control for the trigger. The regulation distinguishes a control/ownership trigger at any time in the year from the year-end share used to allocate profit/loss; preserve acquisitions/disposals and refer a disputed timing case rather than assuming continuous ownership. [Regulation, Articles 2–5 and 8](https://files.reglugerd.is/pdf/1102-2013/current)

The substance file addresses actual premises/equipment, local management and staff, their decision-making authority and expertise, local economic connections and demonstrable value from intragroup services. For the Article 7 outside-EEA/EFTA/Faroe exception, establish the information-access agreement and that more than half of income arises from genuine business. For the within-area exception, prove genuine activity and the required information access/disclosure. A registered-office service or treaty listing alone does not settle these tests. [Regulation, Articles 6–7](https://files.reglugerd.is/pdf/1102-2013/current); [Article 57a][law]

If taxable, allocate the Icelandic-rule profit to the supported ownership share. Keep losses by **owner, foreign entity and origin year**: only proved losses arising during that owner's holding period, verified at year end, offset that owner's later share of the same entity's profit. The regulation excludes pre-2010 losses, permits a ten-year period and does not transfer the unused owner loss to a buyer. Keep distributions and previously taxed inclusions in a separate roll-forward; only the specified excess distribution is taxable again. Any underlying or distribution-level foreign-tax relief needs its own legal basis and claim. [Regulation, Articles 8–9](https://files.reglugerd.is/pdf/1102-2013/current)

**Reporting.** Skatturinn specifies an Icelandic identifier for the CFC, applied for through RSK 17.90 if needed; the annual entity report RSK 4.24 with accounts; and each owner's RSK 4.25 with the owner's return. Multiple Icelandic owners coordinate the entity report. Current general guidance describes the entity report as a paper form and owner reporting as electronically available; confirm the accepted current-year route before submission. Do not substitute a foreign annual report for both filings. [CFC reporting guidance](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/cfc-felog/)

The regulation reproduction says the official Gazette prevails if texts differ. Read it with the current Article 57a, not as authority to override later legislation.


## Deadlines and filing

### Return and assessment workflow

Use **RSK 1.04** for the legal-entity business return through the taxpayer service or software meeting Skatturinn's electronic specification. The legal-entity version is distinct from an individual's business schedule. Reconcile accounts, asset register, deductions, loss/group schedules and applicable information returns; retain submission and acceptance evidence. [RSK 1.04 guidance][return]

For **2025 income filed in 2026**, the 30 January 2026 notice states a general deadline of **31 May 2026** and a professional extension available up to **21 September 2026**. An extension is not automatic. The former generic 30 September statement did not match that notice. Article 93 establishes annual deadline-setting: verify the notice for **2026 income filed in 2027** when available. [2026 filing notice][filing-notice]; [Article 93][law]

Calendar year is the ordinary income period; another accounting year needs the Article 59 permission. For approved foreign-currency accounts, Article 91 requires the supporting accounts and statutory ISK conversion statement; it distinguishes income/expense average rates from balance-sheet closing rates. Check its detailed tax-basis rules before using a single year-end rate for the whole return. [Articles 59, 90–91][law]

Compare assessment with the return, tax calculation and payment ledger. Article 99 gives legal entities a **one-month** initial assessment-complaint period measured from the specified assessment announcement; do not substitute the different individual period or assume every later reassessment follows the same trigger. [Article 99][law]

### Payment-year reconciliation

Regulation 1370/2025 governs **2026 payments towards the 2026 assessment on 2025 income**. Each pre-assessment payment is 8.5% of 2025 assessed public levies; current guidance describes eight equal February–September payments totalling 68%. Reconcile actual notices, reductions and payments rather than treating advances as a tax expense or calling them payments against 2026 trading profit. The regulation also has an ISK 5,000 collection minimum per due date. [Regulation, Articles 1–2][payment-reg]; [Advance guidance][advances]

Article 112 allocates the assessed balance, after the stated advances/credits, across remaining due dates. Do not promise two identical November/December instalments without checking the actual assessment and prior payments. **Final-date discrepancy:** Article 112(1)'s ordinary wording is the month's last business day, whereas Regulation 1370/2025 Article 1 and the guidance say one month after due date. Preserve the issued payment notice and obtain a documented resolution where dates differ; this draft does not silently treat them as identical. [Articles 112, 114][law]; [Regulation, Articles 1–4][payment-reg]

For a requested advance reduction, Regulation 1370/2025 Article 6 says the relevant 2025 bases are **more than 25%** below 2024; the authority's general guidance instead says **at least 25%**, adds an ISK 100,000 tax reduction and describes a 31 May application deadline. Exactly 25% and the applicable year's notice require resolution before assuming eligibility. A request does not itself reduce the amount due. [Regulation, Articles 5–7][payment-reg]; [Advance guidance][advances]

## Penalties and interest

Article 108 increases **tax bases**, rather than imposing the listed percentages directly on tax due:

| Circumstance | Statutory maximum/treatment | Source |
|---|---|---|
| No timely return; estimated bases | Up to 15%, considering withholding already collected | [Article 108(1)][law] |
| Late return received before assessment finishes | 0.5% of bases per late day, capped at 10% | [Article 108(1)][law] |
| Defective/understated bases | Up to 25%; maximum 15% if corrected before assessment | [Article 108(2)][law] |
| Proven absence of taxpayer fault/uncontrollable circumstances | Statutory waiver conditions in Article 108(3) | [Article 108(3)][law] |

Article 114 links assessment late interest to the Central Bank rate. Regulation 1370/2025 Article 4 says unpaid 2026 advances/assessments after a month attract interest from the due date and addresses acceleration after partial nonpayment. Use the actual collection basis, due dates and period-specific rate; no undated floating rate is quoted here. Documentation fines, payroll/VAT collection penalties and criminal sanctions are separate regimes. [Article 114][law]; [Regulation, Article 4][payment-reg]

## Cross-border points

Resident worldwide income still needs treaty and foreign-tax-relief analysis. Article 119 permits an application-based reduction where no double-tax treaty exists and the statutory conditions apply; it is not automatic dollar-for-dollar credit. Use the [resident foreign-income relief workpaper](is-cross-border.md) for country/category matching, tax attribution and the conditional current-UK credit example. Other treaty-specific limitations and exemption methods still need the actual treaty analysis. Company/asset migration now has a statutory computation and payment workpaper in the [cross-border Guide](is-cross-border.md); do not treat a qualifying move as automatically tax-free. [Articles 2, 119][law]

For non-resident payments, preserve the [cross-border Guide](is-cross-border.md)'s distinctions: Article 70 national rates include 20% for the relevant company service/dividend categories, **22% for Article 3(6) royalties**, and **12% for taxable corporate interest**, before exclusions/treaty relief. Do not apply ordinary resident CIT to every gross cross-border receipt. [Articles 3, 70][law]

Screen foreign holdings under Article 57a, related-party transactions under Article 57, CbC reporting under Article 91a, and migration/restructuring under Articles 51–56a. These screens require their own evidence and computations. Sector taxes, incentives/R&D credits, financial instruments and any other applicable group minimum-tax regime require a separate applicability audit; nothing in this ordinary computation establishes their absence.

## Worked examples that recompute

### 1. Profit-to-tax reconciliation

Assume a resident ehf. with ISK 12 million accounting profit before tax, including book depreciation ISK 2 million, a supported nondeductible item ISK 1 million and qualifying dividend income ISK 2 million. Tax depreciation is ISK 3 million and substantiated eligible brought-forward losses are ISK 4 million. The bridge is 12 + 2 + 1 − 3 − 2 = **ISK 10 million** before losses; taxable income is **ISK 6 million** and ordinary tax **ISK 1.2 million**. Assume all participation/loss conditions are met and no other adjustment or sector tax applies. Eligibility is a fact assumption requiring evidence.

```oa-check
name: Iceland company profit to ordinary tax bridge
inputs:
  accounting_profit: 12000000
  book_depreciation: 2000000
  disallowed_item: 1000000
  tax_depreciation: 3000000
  qualifying_dividend_deduction: 2000000
  eligible_losses: 4000000
  ordinary_rate: 0.20
steps:
  before_losses: accounting_profit + book_depreciation + disallowed_item - tax_depreciation - qualifying_dividend_deduction
  loss_used: min(eligible_losses, max(0, before_losses))
  taxable_income: max(0, before_losses - loss_used)
  ordinary_tax: taxable_income * ordinary_rate
expected:
  before_losses: 10000000
  loss_used: 4000000
  taxable_income: 6000000
  ordinary_tax: 1200000
```

### 2. Reverse last year's closing reductions

Assume eligible closing receivables ISK 20 million and inventory ISK 30 million, already valued under the relevant rules. Elect 5% reductions: ISK 1 million and ISK 1.5 million. Prior-year expensed reductions of ISK 750,000 and ISK 1.2 million must be reversed. The net current deduction is **ISK 550,000**, not ISK 2.5 million. Assume no overlapping book or other tax write-down. [Article 31(3)–(4)][law]

```oa-check
name: Iceland closing reductions with prior year reversals
inputs:
  eligible_receivables: 20000000
  eligible_inventory: 30000000
  elected_rate: 0.05
  prior_receivable_reduction: 750000
  prior_inventory_reduction: 1200000
steps:
  current_receivable_reduction: eligible_receivables * elected_rate
  current_inventory_reduction: eligible_inventory * elected_rate
  net_deduction: current_receivable_reduction + current_inventory_reduction - prior_receivable_reduction - prior_inventory_reduction
expected:
  current_receivable_reduction: 1000000
  current_inventory_reduction: 1500000
  net_deduction: 550000
```

### 3. Exact acquisition threshold and the depreciation floor

Assume qualifying office equipment first used this year costs **exactly ISK 600,000**. Article 39's below-threshold expensing does not apply. At an elected permitted 20% rate, first-year depreciation is **ISK 120,000**, leaving **ISK 480,000**. Separately, assume continuing-use equipment with the same original cost but opening tax value ISK 65,000: a 20% charge would be ISK 13,000, but Article 42's ISK 60,000 floor limits the charge to **ISK 5,000**. These are not disposal-year examples. [Articles 34, 36–39, 42][law]

```oa-check
name: Iceland office equipment depreciation and residual floor
inputs:
  original_cost: 600000
  elected_rate: 0.20
  later_opening_tax_value: 65000
  residual_rate: 0.10
steps:
  first_depreciation: original_cost * elected_rate
  first_closing_value: original_cost - first_depreciation
  residual_floor: original_cost * residual_rate
  later_uncapped_depreciation: later_opening_tax_value * elected_rate
  later_depreciation: min(later_uncapped_depreciation, max(0, later_opening_tax_value - residual_floor))
  later_closing_value: later_opening_tax_value - later_depreciation
expected:
  first_depreciation: 120000
  first_closing_value: 480000
  residual_floor: 60000
  later_uncapped_depreciation: 13000
  later_depreciation: 5000
  later_closing_value: 60000
```

### 4. Assessment-year cash reconciliation

Assume 2025 assessed public levies of ISK 5 million, eight unreduced 2026 advances paid in full, and a 2026 assessment on 2025 income of ISK 3.6 million, with no other credits or charges. Each advance is **ISK 425,000**, total **ISK 3.4 million**, leaving **ISK 200,000**. This is a payment reconciliation for the 2026 assessment cycle; it does not calculate tax on 2026 trading income or establish actual instalment dates. [Regulation, Articles 1–2][payment-reg]

```oa-check
name: Iceland 2026 assessment advances and balance
inputs:
  assessment_2025: 5000000
  instalment_rate: 0.085
  paid_instalments: 8
  assessment_2026: 3600000
steps:
  each_advance: assessment_2025 * instalment_rate
  paid_advances: each_advance * paid_instalments
  assessment_balance: assessment_2026 - paid_advances
expected:
  each_advance: 425000
  paid_advances: 3400000
  assessment_balance: 200000
```

### 5. Related-party financing, official positive-profit illustration

Assume all 300 million of related-party interest/discounts is otherwise eligible, statutory profit is 400 million, and no exception applies. The official amendment explanation's result is 220 million deductible, 80 million disallowed. [Bill 626/150, section 3.5](https://www.althingi.is/altext/150/s/0626.html); current [Article 57b][law]. This is a deduction adjustment, not a claim that 80 million itself is tax due.

```oa-check
name: Iceland related-party interest, first 100 million plus capped excess
inputs:
  related_interest: 300000000
  statutory_profit: 400000000
  protected_slice: 100000000
steps:
  - excess_pool: max(0, related_interest - protected_slice)
  - profit_capacity: statutory_profit * 0.30
  - allowed_interest: min(related_interest, protected_slice) + min(excess_pool, profit_capacity)
  - disallowed_interest: related_interest - allowed_interest
expected:
  excess_pool: 200000000
  profit_capacity: 120000000
  allowed_interest: 220000000
  disallowed_interest: 80000000
```

### 6. Financing threshold and equity-ratio boundaries

With otherwise eligible interest exactly 100 million, no amount enters the capped excess pool. Separately, taxpayer equity ratio 28% and group ratio 30% meet the two-percentage-point numeric boundary; 27.9% does not. The latter is only an arithmetic screen: timing, valuation and the other conditions still require evidence. [Article 57b][law]

```oa-check
name: Iceland interest exact threshold and equity-ratio distance
inputs:
  related_interest: 100000000
  taxpayer_ratio: 28
  lower_ratio: 27.9
  group_ratio: 30
steps:
  - excess_pool: max(0, related_interest - 100000000)
  - boundary_distance_points: group_ratio - taxpayer_ratio
  - failing_distance_points: group_ratio - lower_ratio
expected:
  excess_pool: 0
  boundary_distance_points: 2
  failing_distance_points: 2.1
```

### 7. CFC indirect ownership, tax comparison and owner loss

Assume the taxpayer owns 60% of an intermediate company which owns 90% of the foreign entity throughout the year, with a combined 54% indirect interest and no applicable exemption. The foreign entity's profit has already been reconciled to an Icelandic comparable-company base of 20 million; at 20%, hypothetical Icelandic tax is 4 million, so the two-thirds comparison is 2,666,666.67. Actual foreign income tax of 1 million is below that threshold. The owner's profit share is **10.8 million**. A proved eligible same-owner/same-entity carried loss of 2.8 million leaves an **8 million** inclusion; gross Icelandic tax at 20% is **1.6 million before any separately established relief**. No unrelated domestic income is reduced by the ring-fenced CFC loss. [Article 57a][law], [Regulation 1102/2013, Articles 2, 4 and 8](https://files.reglugerd.is/pdf/1102-2013/current)

```oa-check
name: Iceland CFC indirect share and owner-specific same-entity loss
inputs:
  intermediate_share: 0.60
  intermediate_cfc_share: 0.90
  foreign_profit_reconciled_to_iceland_rules: 20000000
  comparable_iceland_rate: 0.20
  actual_foreign_income_tax: 1000000
  proved_owner_same_entity_loss: 2800000
steps:
  - indirect_share: intermediate_share * intermediate_cfc_share
  - hypothetical_iceland_tax: foreign_profit_reconciled_to_iceland_rules * comparable_iceland_rate
  - low_tax_comparison: hypothetical_iceland_tax * 2 / 3
  - owner_profit_share: foreign_profit_reconciled_to_iceland_rules * indirect_share
  - loss_used: min(owner_profit_share, proved_owner_same_entity_loss)
  - inclusion: owner_profit_share - loss_used
  - gross_iceland_tax_before_separate_relief: inclusion * comparable_iceland_rate
expected:
  indirect_share: 0.54
  hypothetical_iceland_tax: 4000000
  low_tax_comparison: 2666666.67
  owner_profit_share: 10800000
  inclusion: 8000000
  gross_iceland_tax_before_separate_relief: 1600000
```

## Ask the client first

- What are the entity's legal form, separate-taxpayer election, residence/management, accounting year and approved currency?
- Which accounts, ledgers, contracts, payroll reports, asset registers, inventory and receivable schedules reconcile to the return?
- What dividends, share disposals, financing, FX and foreign items need distinct adjustments?
- Which loss vintages, ownership/business changes, group approvals or reorganisations affect use of losses?
- What filing extension, assessment, advance notices, reductions, withholding and actual payments already exist?
- Are there regulated financial activities, foreign holdings, incentives, related parties or planned asset/company moves?

<!-- openaccountants-cta-block -->

## Talk to an accountant

For professional review of the facts and workpapers, [contact OpenAccountants](https://www.openaccountants.com/contact).

## Sources

Read **23 October 2026**. Statutes display the 1 October 2026 compilation. Regulation 1370/2025 was retrieved directly as HTML; its page states that the official Gazette prevails over its reproduction. The primary-source rewrite replaces the former short 2025 summary while preserving its file identity and attribution. This is a source-cited draft, not professional attestation. Independent Icelandic legal review, the negative-profit interest-cap boundary, CFC timing/substance disputes and foreign-relief cases outside the shared workpaper, sector/incentive/minimum-tax applicability, restructurings and current filing-system verification remain open. The 2027 filing/payment timetable is not established by the 2026 notices. Example amounts are invented assumptions.

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 90/2003, Articles 2–4, 7–8, 12–61, 70–71, 90–99, 108, 112–114, 119 | [Alþingi][law] | 2026-10-23 |
| Skatturinn, corporate income tax | [Authority guidance][corporate] | 2026-10-23 |
| Skatturinn, 2026 rates | [Current-year rate table][rates] | 2026-10-23 |
| Skatturinn, 2026 assessment on 2025 income | [Assessment information][assessment] | 2026-10-23 |
| Skatturinn, RSK 1.04 filing method | [Return instructions][return] | 2026-10-23 |
| Skatturinn, 30 January 2026 corporate filing notice | [Filing notice][filing-notice] | 2026-10-23 |
| Regulation 1370/2025, 2026 payment cycle | [Regulation][payment-reg] | 2026-10-23 |
| Skatturinn, corporate advance-tax guidance | [Advance payments][advances] | 2026-10-23 |
| Act 33/2020, Article 6, excess-interest wording | [Enacted amendment](https://www.althingi.is/altext/stjt/2020.033.html) | 2026-10-23 |
| Bill 626/150, section 3.5, positive-profit interest calculation | [Official explanation](https://www.althingi.is/altext/150/s/0626.html) | 2026-10-23 |
| CFC Regulation 1102/2013, computation, substance, losses and reports | [Regulation](https://files.reglugerd.is/pdf/1102-2013/current) | 2026-10-23 |
| Skatturinn, CFC report and identifier requirements | [Reporting guidance](https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/cfc-felog/) | 2026-10-23 |

[law]: https://www.althingi.is/lagas/nuna/2003090.html
[corporate]: https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tekjuskattur/
[rates]: https://www.skatturinn.is/einstaklingar/helstutolur/2026
[assessment]: https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/alagningarsedill-og-forsendur/2026/
[return]: https://www.skatturinn.is/atvinnurekstur/framtal-og-alagning/skattframtal-rekstraradila/
[filing-notice]: https://www.skatturinn.is/um-rsk/frettir-og-tilkynningar/opnad-fyrir-skil-a-skattframtali-logadila-2026
[payment-reg]: https://island.is/reglugerdir/nr/1370-2025
[advances]: https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/fyrirframgreidsla-thinggjalda/
