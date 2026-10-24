---
jurisdiction: SM
version: 0.1
last_updated: 2026-10-24
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: sm-income-tax
  IT-CORP: sm-corporate-income-tax
  VAT: sm-vat-gst
  SC: sm-payroll-social
  PR: sm-payroll-social
  TP: sm-transfer-pricing
  XB: sm-cross-border
partial:
  IT-IND: "Existing 2025 summary preserved; current progressive/separate bases, 2026 credits/SMaC and October amendments still need reconciliation."
  IT-CORP: "2026 ordinary rate/base/loss, conditional incentives and advance method drafted; full assets/exemptions/sector/incentive/foreign and filing scope remains open."
  VAT: "Existing 2025 import-tax summary preserved; current monofase law, full tariff, exemptions/refunds and Italy/documentation interface need verification."
  SC: "Existing approximate 2025 contribution summary remains unreconciled; 2026 pension/FONDISS evidence located, full coverage/bases/funds/calendars remain open."
  PR: "Existing 2025 payroll summary remains unreconciled; 2026 wage base, tax credits, withholding/reporting/remittance and benefit rules need work."
  TP: "Normal-value and 2026 international advance-agreement method drafted; actual comparables, downward-adjustment/implementation procedures and specialist scope remain open."
  XB: "Current residence/source/PE and selected withholding/credit methods drafted; actual treaties, personal credit, exit/special cases and operational claims remain open."
---

# San Marino tax pack

Accountable owner: Michael. Active writer: ChatGPT support chat under [OWNERS](../../../OWNERS.md) and [issue #426](https://github.com/openaccountants/openaccountants/issues/426). Taking was recorded before writing on 24 October 2026. Local branch: `codex/san-marino-country-completion`, starting from shared published `532a1568`. Reuse consolidated draft [PR #514](https://github.com/openaccountants/openaccountants/pull/514) after the whole country is prepared, independently reviewed and corrected, then make one combined country content push. This San Marino batch is local and unpublished.

Primary chat retains Montenegro. Liechtenstein and Finland are parked after reviewed country publication, with exact-source and coverage limits preserved. Iceland, Norway, Guernsey, Gibraltar and Bosnia remain parked.

## Existing work and current preparation

The six original source paths and platform attribution/licence fields are preserved; prior bodies remain in Git history. TP and XB methods are added locally. All eight source Guides remain tier 2. No core domain is counted complete, and no named San Marino accountant review is claimed.

| Domain | Guide | Current status |
|---|---|---|
| IT-IND | [sm-income-tax](sm-income-tax.md) | Approximate 2025 source still requires current-law reconciliation; not a verified 2026 method |
| IT-CORP | [sm-corporate-income-tax](sm-corporate-income-tax.md) | 2026 ordinary method with four executable controls; full specialist/application scope open |
| VAT/indirect tax | [sm-vat-gst](sm-vat-gst.md) | Existing import-tax summary; full monofase law/rate/claim/Italy interface still open |
| SC | [sm-payroll-social](sm-payroll-social.md) | Old approximate rates remain to be replaced with current ISS/FONDISS and coverage evidence |
| PR | [sm-payroll-social](sm-payroll-social.md) | Current withholding base, credit/election and reporting/remittance method still needs reconciliation |
| TP | [sm-transfer-pricing](sm-transfer-pricing.md) | New normal-value and international agreement method, three executable controls; procedures/comparables open |
| XB | [sm-cross-border](sm-cross-border.md) | New 2026 source/PE/nonresident and selected corporate-credit method, four executable controls; treaties/special claims open |

The [formation Guide](sm-company-formation.md) remains an older secondary summary requiring statutory verification. The [overview](sm-tax-overview.md) is a router; it supplies no standalone tax calculation. Formation/route presence does not resolve a core tax gap. All eleven current controls are conditional arithmetic examples, not taxpayer eligibility decisions.

## Source dates and current amendments

The [official IGR coordinated archive](https://www.consigliograndeegenerale.sm/on-line/documento17086436.html) contains two separately dated PDFs: no-notes 22 December 2025 and with-notes 12 December 2025. The catalogue describes these as recognition aids, with authentic post 2012 acts in the Bollettino Ufficiale. Do not call either a complete 2026 consolidation or silently treat their dates/texts as identical.

Current preparation reads [Law 141/2025](https://www.consigliograndeegenerale.sm/on-line/home/archivio-leggi-decreti-e-regolamenti/documento17155359.html) with the authentic [DD 156/2026 dated 12 October](https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=9c3a0dfeb72a7aeab52d1c5c0440879b4cf2ad33), expressly applicable from tax year 2026. The [2026 international advance-agreement decree](https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=26a68bf4326bc216b251bc3af7fd385bc9f7c7a0) and [Finance circular 1/2026](https://www.finanze.sm/pub2/dam/jcr%3Ac7b6c29b-5894-4a96-914b-00785958a63a/Circolare%20n.1-2026.pdf) add specific methods. The latter anticipates 2027 systems/manuals; it is not proof they are live now. Retrieved PDFs and hashes support source identity; only selected provisions have been read.

The [ISS household-worker circular](https://www.iss.sm/on-line/home/menudestra/area-modulistica/modulistica-ufficio-contributi/documento49156660.html) supplies 2026 pension/FONDISS evidence but is not a complete general employer-cost table. The [July 2026 import-table amendment](https://www.bollettinoufficiale.sm/on-line/RicercaBU?operation=getDocBU&id=e54431a0e32f941616323ba3300c13a32828e853) is one tariff change, not the entire monofase schedule. These limits remain in the pending work.

## Next country actions

Reconcile individual income/SMaC credits and current payroll/social funds, verify monofase law/rates/refunds and the Italy interface, and replace unverified formation assertions. Complete the operative-date/implementation checks, retain each source/read limit, then run whole-country schema, metadata, calculation and repository checks. Obtain one independent full-pack source review, fix and close findings against exact source blobs, and push the country once to existing PR #514. Exact-head CI follows publication. Keep issue #426 open, all partial flags and the PR draft; named accountant review, specialist coverage and live filing/ingestion remain separate gates.
