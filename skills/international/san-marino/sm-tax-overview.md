---
name: sm-tax-overview
description: >
  Route 2026 San Marino tax questions to the relevant source Guide and country gap register. Use for corporate and personal IGR, monofase import tax, payroll/social contributions, related-party dealings, international agreements, nonresident income, selected foreign credit and formation intake. Establish the actual person, entity, transaction, period and current Guide status before choosing a method. The country batch preserves six older entry paths and adds TP/XB. This router replaces the prior approximate rate/deadline summary; it supplies no independent liability formula or treaty/filing entitlement. Several linked older 2025 Guides still require reconciliation. All domains remain partial, and independent whole-pack and named San Marino accountant review are open.
jurisdiction: SM
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.1
---

# San Marino tax overview and routing v0.1

## Establish person, transaction and year

Use the [country register](README.md) for each Guide's scope and remaining gaps. The corporate, TP and XB methods are locally prepared 2026 drafts; individual, payroll/social, monofase and formation source reconciliation is still in progress. Original bodies remain in Git history. This local batch is unpublished and all source Guides remain tier 2.

| Question | Start with |
|---|---|
| Resident individual income, wage/pension or business base and SMaC credits | [Individual IGR](sm-income-tax.md), with its unreconciled 2025 limitations |
| Corporate base, losses, ordinary rate, conditional new-activity relief and advances | [Corporate IGR](sm-corporate-income-tax.md) |
| Import tax, goods classification and Italian invoice interface | [Monofase/indirect tax](sm-vat-gst.md), pending full current-law reconciliation |
| Employee withholding and social/pension/FONDISS coverage | [Payroll/social](sm-payroll-social.md), pending current 2026 reconciliation |
| Related-party normal value, adjustments and international advance agreements | [Transfer pricing](sm-transfer-pricing.md) |
| Residence/source/PE, nonresident receipts and selected corporate foreign credit | [Cross-border](sm-cross-border.md) |
| Entity capital, governance, registration and annual compliance | [Formation](sm-company-formation.md), pending statutory verification |

## Source and status controls

The [official IGR coordinated archive](https://www.consigliograndeegenerale.sm/on-line/documento17086436.html) has separate dated 2025 editions. Read its relevant provisions with [Law 141/2025](https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html) and authentic [DD 156/2026](https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33). Current methods identify provisions read and their limits; no full amendment chain, municipality/special-case outcome or live portal acceptance is inferred from a source URL.

The working branch `codex/san-marino-country-completion` is tracked on [issue #426](https://github.com/openaccountants/openaccountants/issues/426) and will reuse consolidated draft [PR #514](https://github.com/openaccountants/openaccountants/pull/514). Complete local country preparation and independent whole-pack review/corrections before one combined country content push. Preserve all seven partial flags and the separate named local accountant gate.

This router supplies no standalone rates or calculation blocks. Use the exact tax-year/source/status of the selected method and the actual case evidence before computing or filing.

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
