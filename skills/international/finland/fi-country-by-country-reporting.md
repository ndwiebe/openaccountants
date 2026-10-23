---
name: fi-country-by-country-reporting
description: >
  Screen Finland country-by-country reporting, identify the reporting entity,
  distinguish notification from the full report and prepare submission records.
  Local-filing exceptions, current statutory reconciliation and exchange checks
  remain outstanding.
jurisdiction: FI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
---

# Finland country-by-country reporting v0.1

## Who this applies to

Vero's guidance uses preceding-period consolidated net sales of **at least EUR 750 million**, together with the relevant international structure, for CbCR screening. The full-report instructions also address Finnish-resident standalone enterprises with a foreign PE. This is a group reporting test, distinct from the documentation-size rules in the [transfer-pricing Guide](fi-transfer-pricing.md). [Full-report instructions][report]

Read the source and limits below before using this draft for a filing. Statutory reconciliation, exceptional local filing and independent review remain open.

## Filing roles and the threshold

The Finnish ultimate parent generally files the full report. A foreign parent's report can reach Finland through exchange, but the Finnish entity must establish the parent's obligation and applicable exchange arrangements. If that route fails, examine surrogate and exceptional Finnish local-filing requirements; foreign ownership alone does not settle the issue. [CbCR overview][overview]

For non-euro accounts, the overview describes the ultimate parent's jurisdictional threshold and January 2015 currency basis. Do not mechanically convert the euro threshold at today's rate. The detailed currency and local-filing rules still require case-specific verification. [CbCR overview][overview]

## Notification of the reporting entity

The notification instructions cover Finnish-resident companies and qualifying Finnish PEs in an in-scope group. The PE condition refers to separate financial statements prepared for specified reporting, regulatory, tax or management purposes. Determine the full-report filer before completing the notification. [Notification instructions][notification]

Prepare the reporting entity's name, Finnish Business ID or foreign identifier as applicable, and the jurisdiction receiving the report. Preserve the filer-role decision and any other Finnish entities included in the notification. Vero describes including other Finnish subsidiaries in one notification; record which entities it actually covers rather than assuming group-wide completion. [Notification instructions][notification]

The MyTax guidance distinguishes an unfinished saved notification from a submitted one. Preview it, submit it and preserve the confirmation. Verify amendments and the represented entities before using a prior notification as a template. [Notification instructions][notification]

## Dates and submission

The full-report instructions require filing **within twelve months after the accounting period ends**. Confirm the actual period, including any change of year end. Supply reporting-entity, jurisdiction and constituent-entity data with supporting additional information; identify the currency and explain relevant conversion assumptions. [Full-report instructions][report]

Vero's 2023 service-change notice describes notification filing before the reported accounting period ends and an extension request through MyTax if that cannot be met. The current statutory deadline, extension decision and taxpayer-specific notice must be checked before a live filing. The same notice records the closure of Lomake.fi in February 2024; it must not be used as the current filing route. [Service-change notice][service]

The overview describes MyTax and Ilmoitin.fi submission, with XML for full reports and the applicable year-specific specification for notification files. Check the current schema and agent authorisation before transmitting; no live account or file upload was tested for this draft. [CbCR overview][overview]

## Preparation workpaper

This is our practical reconciliation framework, not an additional statutory form:

1. Record the reported period, previous-period revenue, consolidation basis and entities included.
2. Identify the ultimate parent, reporting entity and any surrogate or proposed local filer.
3. Obtain evidence of foreign filing obligations and exchange conditions.
4. Reconcile jurisdiction totals and constituent-entity identifiers to the underlying records.
5. Track notification and full-report submission separately, retaining confirmations and corrections.

## Worked example

Assume euro-denominated consolidated net sales for the preceding period consist of EUR 760 million external revenue and EUR 40 million intragroup revenue eliminated in consolidation. The consolidated amount is EUR 760 million, EUR 10 million above the screening threshold. This assumes the consolidation is correct and the international-structure conditions are met; it does not identify the filer or establish local-filing duties.

```oa-check
name: Finland CbCR assumed consolidation threshold
inputs:
  external_revenue: 760000000
  intragroup_revenue: 40000000
  eliminated_intragroup_revenue: 40000000
  threshold: 750000000
steps:
  before_eliminations: external_revenue + intragroup_revenue
  consolidated_revenue: before_eliminations - eliminated_intragroup_revenue
  excess_over_threshold: consolidated_revenue - threshold
expected:
  before_eliminations: 800000000
  consolidated_revenue: 760000000
  excess_over_threshold: 10000000
```

## Ask the client first

- What are the group period, consolidation basis, currency and preceding-period revenue?
- Which entity files the full report, in which jurisdiction, and with what evidence?
- Which Finnish entities and PEs exist, and what notifications already cover them?
- Are there exchange failures, surrogate arrangements or authority notices?
- What submission confirmations and corrections are available?

## Sources and review limits

Official Vero text retrieved through the search index on 23 October 2026:

- [CbCR overview][overview].
- [Full-report MyTax instructions][report].
- [Reporting-entity notification instructions][notification].
- [MyTax service-change notice][service].

Not yet confirmed: full current sections 14d–14e and related amendments; detailed local/surrogate conditions; live exchange relationships; sanctions; data-category definitions; current XML and authorisations; extensions and specific calendar deadlines. Independent review and professional attestation remain outstanding. Reporting and country coverage remain partial.

[overview]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/
[report]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/country-by-country-report---how-to-file-the-report-in-mytax/
[notification]: https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/notification-of-the-reporting-entity-how-to-file-the-notification-in-mytax/
[service]: https://vero.fi/en/About-us/newsroom/news/uutiset/2023/country-by-country-reporting-in-mytax/
