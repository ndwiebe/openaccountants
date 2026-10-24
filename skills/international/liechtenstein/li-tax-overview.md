---
name: li-tax-overview
description: >
  Route 2026 Liechtenstein tax questions to the applicable source Guide and
  country gap register. Use for individual wealth-and-income tax, corporate profit,
  VAT, payroll/social contributions, transfer pricing, cross-border and formation
  intake. Identify the person, entity, country and period before choosing a method.
  This overview replaces the earlier approximate rate/deadline summary with a
  routing map; it supplies no standalone liability, treaty entitlement or filing
  instruction. The linked Guides contain the actual rules, sources, calculations
  and limits. All remain source-cited drafts with partial domain coverage, pending
  independent whole-pack and named Liechtenstein accountant review; presence is
  not proof of completeness.
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.1
---

# Liechtenstein tax overview v0.1

## Start with the question

This is a router for the 2026 source-cited country draft, not a standalone tax calculation. Establish legal person/entity, residence and activity countries, dates, income/supply/payment category, existing registrations, records and the authority decision before selecting a workpaper. The [country README](README.md) declares all seven applicable domains partial.

| Work | Read first | Key boundary |
|---|---|---|
| Individual income and wealth | [li-income-tax](li-income-tax.md) | Established taxable income/wealth, family tariff and actual annual municipality rate |
| Corporate profit | [li-corporate-income-tax](li-corporate-income-tax.md) | Tax adjustments, modified equity, losses and minimum-tax eligibility |
| VAT | [liechtenstein-vat](liechtenstein-vat.md) | Actual authority/registration, supply evidence, deduction entitlement and method |
| Employee withholding and insurance | [li-payroll-social](li-payroll-social.md) | Separate tax/social bases, 2026 Liechtenstein rates and coverage |
| Related parties and PEs | [li-transfer-pricing](li-transfer-pricing.md) | Actual relationship, documentation route and supported arm's-length method |
| Migration, foreign income and relief | [li-cross-border](li-cross-border.md) | Domestic liability, actual treaty and claim/deferral procedure |
| Entity setup | [li-company-formation](li-company-formation.md) | Selected form, contributions, actual register/governance and licensing evidence |

The earlier summary's rates/deadlines, Swiss-derived payroll/VAT assumptions and secondary citations remain in Git history. They are not substitutes for the current topic's source check. The [Liechtenstein Tax Administration](https://www.llv.li/de/landesverwaltung/steuerverwaltung) and the [official legislation collection](https://www.gesetze.li) are source entry points; the exact Acts/sections and read limits are linked in each Guide.

## Evidence and unresolved work

The local country batch is being prepared on `codex/liechtenstein-country-completion` under [issue #406](https://github.com/openaccountants/openaccountants/issues/406). Preserve the original six Guides and research history; the missing TP and XB methods have been added locally. This router intentionally has no calculation blocks because it supplies no independent tax formula.

No named local accountant review, complete tax-domain coverage, filing acceptance or production ingestion is asserted. Complete the remaining source/specialist work in README, run country checks, obtain independent whole-pack review and fix findings before the single country content push to consolidated draft PR #514.

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
