---
name: gi-global-minimum-tax
description: >
  Prepare Gibraltar global minimum-tax scope, domestic top-up and compliance working papers under the Global Minimum Tax Act 2024, checked in October 2026. Covers commencement, wholly domestic groups, separate calculation pools, covered-tax exclusions, information returns, exchange notifications, payment, records and selected penalties. Use for Pillar Two, domestic minimum top-up tax and income inclusion rule questions. This source-cited draft does not implement the complete GloBE income, deferred-tax, substance exclusion or safe-harbour calculations. Establish those inputs separately, retain the applicable source versions and obtain independent source and qualified professional review before filing, paying or claiming an exemption.
jurisdiction: GI
category: international
tax_year: 2024
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
sources:
  - url: "https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf"
    title: "Global Minimum Tax Act 2024, sections 2–52"
    as_of: "2026-10-22"
  - url: "https://www.gibraltarlaws.gov.gi/legislations/global-minimum-tax-act-2024-7478"
    title: "Official legislation index and linked Act"
    as_of: "2026-10-22"
  - url: "https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/12/tax-challenges-arising-from-digitalisation-of-the-economy-global-anti-base-erosion-model-rules-pillar-two_eed81a23/782bac33-en.pdf"
    title: "OECD GloBE Model Rules 2021, Article 1.1 scope"
    as_of: "2026-10-22"
---

# Gibraltar global minimum tax v0.1

> **Source-cited draft.** Independent source review and professional attestation are pending. This is a domestic-law calculation and compliance framework, not a complete Pillar Two engine.

## Who this applies to

The Act applies generally to fiscal years beginning **on or after 31 December 2023**; its Part 3 income inclusion rule (IIR) applies to fiscal years beginning **on or after 31 December 2024**. Thus an ordinary calendar-year group first tests domestic top-up for 2024 and IIR for 2025. A year beginning exactly on either statutory date is included. [Section 2](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

The incorporated Model Rules' ordinary MNE threshold is consolidated UPE revenue of **at least EUR750 million in at least two of the four immediately preceding fiscal years**. Article 1.1 also addresses non-twelve-month periods and points to Article 6.1 for special threshold cases; mergers, demergers and short periods need that separate analysis. [Model Rules, Article 1.1](https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/12/tax-challenges-arising-from-digitalisation-of-the-economy-global-anti-base-erosion-model-rules-pillar-two_eed81a23/782bac33-en.pdf).

Gibraltar additionally defines a **Wholly Domestic Group** by UPE and all constituent entities being located in Gibraltar and consolidated revenue of at least EUR750 million in two of the four preceding fiscal years. Section 15 treats it as an MNE group **for Part 4**, not automatically for every IIR provision. Location follows Model Rule 10.3, not incorporation alone. For four ordinary twelve-month years, revenues EUR740m, EUR750m, EUR760m and EUR730m meet the two-year revenue test; EUR740m, EUR749m, EUR760m and EUR730m do not. These examples assume unchanged group scope and do not establish each entity's inclusion. [Sections 3 and 15](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

Map excluded entities and ownership before calculating. Part 4 expressly excludes **Investment Entities and Insurance Investment Entities**; a commercial label such as “investment company” is not proof of the defined classification. Section 12 charges specified parent entities under the IIR in accordance with the Model Rules. Section 13 excludes the UTPR charging articles from Part 3. Domestic constituent entities are jointly liable under section 16; domestic joint ventures/subsidiaries have the separate joint-liability rule in section 17. [Sections 12–18](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

## Rates and computation rules

The minimum rate is **15%**, under section 11. A headline corporate-tax rate of 15% does not itself establish a zero top-up liability: the Act requires a Model Rules calculation with domestic modifications. Establish GloBE income, adjusted covered taxes, effective tax rate, top-up percentage, excess profits and additional current top-up tax before using the formula below. This Guide does not derive those inputs from ordinary taxable profits. [Sections 11 and 18–25](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

1. Identify the applicable fiscal-year Model Rules, Commentary, administrative guidance and Gibraltar notices. Sections 4 and 6 incorporate interpretation rules and specify timing for Commentary amendments; do not apply a later release to an earlier year without checking that timing and any ministerial notice.
2. Apply domestic modifications. Section 19 disapplies the listed Model Rules, including the ordinary jurisdictional formula/allocation provisions. Section 20 disapplies the **QDMTT Safe Harbour for Part 4**. That is not a statement that every safe harbour is unavailable, or that another jurisdiction cannot recognise Gibraltar's QDMTT.
3. Under section 21, exclude the specified foreign tax accrued by a foreign owner/main entity on domestic GloBE income from domestic adjusted covered taxes. Section 22 excludes domestic covered tax allocated to a foreign entity under the stated Model Rule 4.3 provisions. Do not add foreign parent tax to the domestic pool indiscriminately.
4. Section 25 requires separate jurisdictional computations for minority-owned constituent entities, domestic JV groups and other domestic constituent entities. For each applicable pool use **top-up percentage × excess profits + additional current top-up tax**. Sections 23–24 separate the domestic constituent-entity total from domestic JV totals.
5. If computed in a foreign currency, section 8 converts the liability to sterling using the **average exchange rate for the fiscal year**. Document the rate and quotation direction; the Act does not supply the numerical rate.

Source for these steps: [sections 3–8 and 18–25](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf). Elections affecting the Model Rules calculation have the same effect under section 7; preserve the actual election and applicable conditions. Safe-harbour eligibility, excluded-entity definitions, deferred-tax adjustments and complete IIR allocation remain outside this draft's verified computation scope.

## Worked example 1: domestic formula and currency

Assume a reviewed pool has an established top-up percentage of 3%, excess profits EUR800,000 and additional current top-up tax EUR2,000. Section 25 gives **EUR26,000**. If the evidenced fiscal-year average is GBP0.85 per EUR1, section 8 gives **GBP22,100**. The rate and all inputs are illustrative, not official figures. At a zero top-up percentage, the same EUR2,000 additional current top-up tax still produces EUR2,000 under the formula; do not discard that component. [Sections 8 and 25](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

```oa-check
name: Gibraltar domestic top-up formula and sterling conversion
inputs:
  topup_percentage: 0.03
  excess_profits: 800000
  additional_current_tax: 2000
  gbp_per_eur: 0.85
steps:
  - tax_eur: topup_percentage * excess_profits + additional_current_tax
  - tax_gbp: tax_eur * gbp_per_eur
  - zero_percentage_tax: 0 * excess_profits + additional_current_tax
expected:
  tax_eur: 26000
  tax_gbp: 22100
  zero_percentage_tax: 2000
```

## Filing, notification and payment calendar

Sections 26–27 set the ordinary GIR deadline at the **last day of the fifteenth month following fiscal-year end**. The eighteenth-month deadline applies only if this is the group's first fiscal year subject to the Act **and it has not been required to file a GIR elsewhere for a previous fiscal year**. First filing in Gibraltar alone does not prove eligibility for eighteen months. The UPE or designated filing entity files for the group under Part 3; Part 4 requires appointment of a designated local entity to file for the domestic entities/JVs. Required supporting information accompanies the return. [Sections 26–27](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

Section 28 provides a local-filing exception where the GIR has been filed in a jurisdiction with a **qualifying competent authority agreement effective with Gibraltar for that reporting year**. A general tax treaty or an intention to file overseas is insufficient evidence that the exception is satisfied. The required notification that the GIR has or will be filed abroad is due **no later than three months before the GIR filing deadline**. Verify both the agreement and actual filing; identify who must notify under the relevant subsection. [Section 28](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

Payment is due by the GIR filing deadline. The Part 3 parent pays for the group, with joint liability where more than one parent has liability; under Part 4 the designated local entity pays for the domestic entities/JVs. The foreign-filing exception does not itself remove payment. [Section 29](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

For a 31 December 2024 year-end, an established eighteen-month case has a GIR/payment deadline of **30 June 2026**; the ordinary fifteen-month case has **31 March 2026**. Calculate the separate three-month-prior notification deadline using the applicable date and confirm administrative date conventions. These historical dates do not grant a late filer a new extension. Current registration, filing formats, payment references and correction channels remain unverified: the official registration guidance URL returned 404 when fetched on 22 October 2026.

## Records, assessments and repayment

Keep the records needed for a GIR **or notification for ten years from the fiscal-year end**, under section 30. Sections 33–34 prescribe the stated ten-year assessment/amendment limits; section 35 imports the Income Tax Act assessment-appeal provision. Consult the [assessment appeals Guide](gi-income-tax-assessment-appeals.md), but do not transfer its ordinary income-tax refund or surcharge rules to this Act. [Sections 30–36](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

Section 52 allows proven overpayment to be refunded, with a claim within **ten years from the end of the fiscal year concerned**, and Commissioner certification of the amount. This differs from the ordinary income-tax six-year refund rule. For fiscal year ending 31 December 2024, the ten-year endpoint is 31 December 2034. Keep refund procedure, assessment appeal and record-retention obligations distinct. [Section 52](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

## Worked example 2: late-payment surcharge

Section 44 imposes **2% of unpaid top-up tax on the day after payment is due**. At its further thirty-day trigger, **5% of the remaining unpaid tax and first surcharge** becomes payable. If GBP10,000 and its first surcharge remain wholly unpaid throughout, the first surcharge is GBP200 and the second GBP510, leaving **GBP10,710**. If the first surcharge is paid before that second trigger but all principal remains unpaid, the second amount is GBP500. Establish actual dates and payments before computing a live liability. [Section 44](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

```oa-check
name: Gibraltar minimum-tax late-payment surcharge
inputs:
  unpaid_tax: 10000
steps:
  - first_surcharge: unpaid_tax * 0.02
  - second_all_unpaid: (unpaid_tax + first_surcharge) * 0.05
  - total_all_unpaid: unpaid_tax + first_surcharge + second_all_unpaid
  - second_first_surcharge_paid: unpaid_tax * 0.05
expected:
  first_surcharge: 200
  second_all_unpaid: 510
  total_all_unpaid: 10710
  second_first_surcharge_paid: 500
```

Section 43 specifies a GBP1,000 failure-to-file/notify penalty, but the published text contains the wording “shall may be liable”; record this drafting defect rather than asserting automatic imposition. Section 45 specifies GBP5,000 for record failures. Section 47 specifies GBP500 for the relevant notice failure and a further GBP1,000 after its one-month trigger. Section 48 gives conditional discretionary relief; do not assume a waiver. Notices, offences and penalty appeals require their own analysis. [Sections 43–49](https://www.gibraltarlaws.gov.gi/uploads/legislations/minimum-tax/2024-20/2024-20o.pdf).

## Intake and remaining verification

Obtain the ownership/entity map, four-year consolidated revenue, fiscal-year dates, entity-location analysis, excluded-entity evidence, accounting standards, GloBE working papers, tax allocations, elections, prior overseas GIR obligations, filer appointments, exchange-agreement evidence, payment history and average exchange rate.

The official index links the Act used here, while displaying both “Current Version” and an out-of-date version label. The same PDF is linked in both entries; that does not certify absence of later notices or changes. Remaining acceptance work includes a full fiscal-year OECD guidance/notice reconciliation, complete GloBE calculations and exclusions, safe harbours, parent allocations, current forms/portal access, payment and correction procedures, the Income Tax Act election interaction and independent/professional review. No live return or payment was made. No comprehensive coverage or professional attestation is claimed.

## Self-checks

- Verify both group threshold and each entity's classification, location and liability.
- Separate IIR commencement from domestic top-up commencement and identify each calculation pool.
- Reconcile the full GloBE inputs before applying the domestic formula.
- Test first-year deadline conditions against earlier foreign GIR obligations.
- Keep registration, GIR, notification, payment and appeal steps distinct.

## Disclaimer

General tax and accounting reference only. A qualified professional must check current law, the group's facts, calculations, elections and filing requirements before action.
