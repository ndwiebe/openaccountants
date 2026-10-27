---
name: spain-vat-return
description: Reconciles a Spanish ordinary VAT return for 2026 to invoices, bank settlements, customs assessments, registers and accepted prior returns for sole traders and companies in the peninsula and Balearic Islands. Uses es-vat-return for the underlying computation and checks business-use restrictions, general versus special prorrata, investment-good adjustment signs, reverse-charge mapping and credit roll-forward against current Modelo 303 instructions. Separates withheld income tax and platform fees from VAT bases and distinguishes dated energy and housing changes from ordinary rates. Use for revisar IVA, revisar Modelo 303, conciliación IVA, return review, prior credit and investment adjustment. Preserves this existing entry point while recording territorial, special-regime and unresolved computation limits.
version: 2.1
category: international
jurisdiction: ES
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain: VAT return reconciliation, 2026

**Sourced from the law.** This draft has not had an independent whole-pack review or accountant sign-off. It preserves this existing entry point and reconciles the calculation in [es-vat-return](es-vat-return.md) to invoices, registers and the actual 2026 Modelo 303. Use that Guide's complete ordinary computation, including both prorrata methods; this review route does not supply a competing historical box map.

## Who this applies to

Ordinary IVA taxpayers in the peninsula/Balearic Islands, including businesses with both deduction-entitling and exempt turnover. Establish the taxpayer, period, establishment, regime and competent administration. The Canary Islands, Ceuta and Melilla use separate indirect taxes; foral allocation and special-regime computations remain outside the completed ordinary route ([LIVA art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a3)).

Read actual invoices, customs documents, registers/SII, prior filed returns, credit/refund decisions and relevant elections. Merchant names, foreign IBANs, round sums or personal-looking counterparties are leads for reconciliation, not legal classifications. A bank-only draft cannot substantiate recoverable input VAT or resolve supply place, exemption, tax point or reverse charge ([LIVA arts. 69–70/84/97](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a97)).

## Rates, bands and thresholds

| Check | Required rule | Period | Official source |
|---|---|---|---|
| Ordinary rates | **21% / 10% / 4%** under the exact categories; **0%** only where the specific statutory conditions hold | 2026 | [LIVA arts. 90–91](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a91) |
| Dated energy supplies | Apply the spring temporary rates and later conditional product/CPI rules in the computation Guide; do not assume all-year 21% or all-year 10% | 2026 | [RDL 7/2026 art. 42](https://www.boe.es/buscar/act.php?id=BOE-A-2026-6544#a4-4); [RDL 18/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-14112); [RDL 25/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20265) |
| Housing period split | New furnished-short-letting, renovation and permanently protected-home wording applies from **1 December 2026**, not January | 2026 cutover | [RDL 29/2026 art. 7](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823#a7) |
| Prorrata percentage | Round annual eligible-turnover fraction **up to whole percent** | 2026 | [LIVA art. 104](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a104) |
| Mandatory special method | General recovery exceeds special recovery by **10% or more**; this is not a ten-percentage-point test | 2026 | [Art. 103](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a103) |
| Passenger vehicle | **50%** business-use presumption after establishing business allocation, or the statutory supported/100% category | 2026 | [Art. 95](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a95) |
| Investment-good adjustment | Percentage change **strictly over ten points**, divisor **5**, land/buildings **10** | Statutory adjustment window | [Arts. 107–109](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a109) |
| Deduction and return-credit clocks | Separate **four-year** clocks from entitlement arising and original credit-return filing, respectively | 2026 | [Art. 99](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a99) |

## The base

### Reconcile the source ledger

Use one row per actual transaction/invoice with issuer/recipient NIF, legal counterparty and establishment, description, supply/movement evidence, invoice/receipt/devengo dates, base, actual rate/quota, business-use fraction, blocked amount, sector/use allocation, prorrata method/percentage, deductible quota, return box and source reference. Keep amendments, prior-period claims, returned payments and unpaid invoices separately. Reconcile opening bank balances plus all movements to closing balances without treating each movement as a sale or purchase.

Reconstruct the invoice settlement as **base + VAT − documented withholding − other settled credits = money received**. If the platform deducts fees, record the gross underlying sales and actual separately invoiced platform service. Do not infer a universal VAT or withholding rate from the amount received. Loans, own-account transfers, owner capital/draws, payroll and statutory payments receive their actual treatment, not an invented VAT extraction ([LIVA arts. 4/7/75/78](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a78)).

Check invoice support before deduction: issuer/recipient details, separate VAT quota and statutory content, including extra details on a simplified invoice. Missing/incorrect documents require correction or an unresolved item, not a fabricated invoice. The investment-good definition is a VAT test separate from book capitalisation. Foreign VAT is not Spanish deductible quota ([LIVA arts. 97–100/108](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a97); [RD 1619/2012 arts. 6–7](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696#a7)).

### Recompute recovery before mapping boxes

Apply business/private allocation and art. 96 restrictions first. The passenger-car presumption is not an automatic deduction on an unrelated personal vehicle. A property partly used by the business can support proportionate utility recovery under the binding TEAC criterion; it does not establish the same proportion for every private mobile service ([LIVA arts. 95–96](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a95); [TEAC 19 July 2023 RG 00/06654/2022](https://serviciostelematicosext.hacienda.gob.es/TEAC/DYCTEA/criterio.aspx?id=00%2F06654%2F2022%2F00%2F0%2F1)).

Rebuild the annual art. 104 included-turnover fraction and retain each exclusion. Exempt turnover is not subject to a generic de-minimis refusal. Under general prorrata, apply the rounded percentage to the eligible business pool; under special, allocate exclusively entitling/exempt/shared costs separately. Recompute both methods for the mandatory comparison. The final correction is **definitive annual recovery − all provisional recovery**, including whatever provisional amount has already been entered for the last period. Do not multiply private-use deductions twice, allow exempt-only costs in special recovery, or use the special method voluntarily without its required election/holding rules ([LIVA arts. 101–106](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a106); [RIVA art. 28](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a28)).

For an investment-good adjustment, preserve the original quota/deduction, first-use date, relevant years and annual percentages. A repayment under art. 109 enters box 43 as a **negative input adjustment**. A positive additional deduction has the opposite sign. A current-year definitive-prorrata correction is box 44; it is not also posted to 43 ([LIVA arts. 107–110](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a107)).

### Reconcile the 2026 form and credit roll-forward

Use the relevant January/1T or later-period AEAT instructions. Domestic output 4/10/21% uses **01–03/04–06/07–09**. Intra-EU goods/services received use output **10/11** and ordinary input **36/37**; other reverse charge output **12/13**, with the domestic input-row interpretation disclosed in the computation Guide. Imports use **32/33**, and the corresponding investment-input pairs are **30/31 domestic, 34/35 import, 38/39 intra-EU**. Thus an EU service does not use the old sibling's 17/18 mapping, nor does non-EU service output use 19/20 ([AEAT 2026 instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html)).

Tie output to **27**, input/adjustments to **45**, and net to **46 = 27 − 45**. In a simple state-only original return with no special adjustments, 64/66 follow the ordinary result, **69 = 66 − 78**, and **71 = 69**. Verify prior credit **110**, actual applied credit **78**, and remaining **87 = 110 − 78**. Newly generated negative current-period VAT is not put into 87: it is a separate current-period amount added to the next ledger. No already requested refund remains available for compensation. Carry the original filing date for each unused balance, not a restarted four-year clock at every return ([LIVA art. 99](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a99); [AEAT later-period credit instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026/instrucciones-02-12-2t-4t-2026.html)).

Use a formula-driven working paper with transaction totals, box summary, adjustments and separate prior/current credit schedules. Reconcile invoices to VAT registers/SII, then returns to payment/refund confirmations. Keep the tax computation and payment status distinct: a draft, saved form or bank transfer by itself is not the accepted filing receipt. Detailed fuel, foral, correction and special-regime result fields require their own rule rather than a balancing entry.

## Deadlines and filing

Ordinary 303 quarters file in the first **20 calendar days of April/July/October**; the final quarter in the first **30 days of January**. Monthly filers generally have the first **30 days** of the next month, with January's period due by the last day of February. Confirm holidays and direct-debit windows for the actual period. Monthly status depends on the statutory categories, including prior-year turnover **over 6,010,121.04** and REDEME; monthly filing alone does not establish monthly-refund entitlement ([RIVA art. 71](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a71)).

Check 390 filing or the exact exoneration/last-303 annual data requirements; its ordinary annual deadline is the first **30 January days**. Reconcile 349 using the supplied-goods/services **50,000** quarterly test and the preceding four quarters, rather than applying a threshold to all purchases indiscriminately. SII has its separate four/eight-day and before-16th deadlines ([390 order art. 8](https://www.boe.es/buscar/act.php?id=BOE-A-2009-18472#a8); [RIVA arts. 69 bis/81](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a81); [AEAT 2026 exemptions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html)).

## Penalties and interest

Classify voluntary late filing, underpayment, late collection and record/invoice infringements separately. LGT art. 27 provides **1% plus 1% per complete late month** through twelve months, then **15% plus the prescribed interest**; offence and collection amounts depend on their own conditions. A rectificative label does not remove a surcharge or establish a harmless error. Use the full sourced penalty table in [the computation Guide](es-vat-return.md#penalties-and-interest), with the conduct, notice, date, unpaid amount and payment evidence recorded ([LGT arts. 26–28/188/191/198](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27)).

## Cross-border points

Confirm the actual supplier/customer establishment, business status and goods movement. General B2B services, property/other exceptions, intra-EU acquisition, export and import are different legal routes. Reverse-charge output is reported in full; the input side remains restricted by business use, blocking and prorrata. Check a supplier's incorrect foreign VAT separately from the Spanish recipient tax obligation. Reconcile relevant 349, customs and VAT-register entries without assuming that every foreign payment is a reverse charge or every foreign receipt an export ([LIVA arts. 13/21/25/69–70/84/94](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a84)).

## Two worked examples that recompute

### Invoice settlement and prior credit are separate from the VAT base

The source invoice states **1,000 base + 210 VAT − 150 withholding = 1,060 received**. These are assumed documented facts, not a rule assigning every payment that withholding rate. Eligible input VAT is **80**. The VAT base stays 1,000 and current net VAT is **130**. Of **200** prior credit, apply 130 and carry **70** in box 87; the original return result is zero. Do not extract VAT from the 1,060 bank receipt or deduct the withholding from output VAT.

```oa-check
name: Spain 2026 invoice withholding settlement and prior VAT credit
inputs:
  invoice_base: 1000
  invoice_vat: 210
  documented_withholding: 150
  eligible_input: 80
  prior_credit: 200
steps:
  bank_receipt: invoice_base + invoice_vat - documented_withholding
  current_net: invoice_vat - eligible_input
  prior_used: min(prior_credit, max(current_net, 0))
  prior_remaining: prior_credit - prior_used
  return_result: current_net - prior_used
expected:
  bank_receipt: 1060
  current_net: 130
  prior_used: 130
  prior_remaining: 70
  return_result: 0
```

### Investment adjustment sign and ordinary result

A machine within its adjustment window originally bore **1,260 VAT**, with an **80%** deduction. Current definitive deduction is **60%**, a **20-point** change, so adjustment is required. Original recovery **1,008** minus current-percentage recovery **756**, divided by five, is **50.40 repayable**. Enter **−50.40** in box 43. Assuming **500** other fully reconciled final-period input after its own current-year percentage correction and **1,000** output, total input including box 43 is **449.60**, and the original state-only result without prior credit is **550.40 payable**. No second copy of this same adjustment goes into box 44.

```oa-check
name: Spain 2026 investment-good adjustment reduces input recovery
inputs:
  original_vat: 1260
  original_percentage: 80
  current_percentage: 60
  divisor: 5
  other_final_input: 500
  output: 1000
steps:
  points_change: abs(original_percentage - current_percentage)
  original_deduction: original_vat * original_percentage / 100
  current_equivalent: original_vat * current_percentage / 100
  repayment: (original_deduction - current_equivalent) / divisor
  box43: 0 - repayment
  total_input: other_final_input + box43
  payable: output - total_input
expected:
  points_change: 20
  original_deduction: 1008
  current_equivalent: 756
  repayment: 50.40
  box43: -50.40
  total_input: 449.60
  payable: 550.40
```

## Ask the client first

1. Which legal taxpayer, VAT territory, filing period, regimes/elections and previous accepted returns apply?
2. Which invoices, customs assessments, credit notes and payment/withholding records explain every material register-to-bank difference?
3. What proves business/private and taxable/exempt use, sector allocation, annual turnover and any special-prorrata election?
4. What original investment-good deductions, first-use years and changes/disposals require adjustment?
5. What prior credit/refund ledger and filing receipts establish the opening balance, actual use and unexpired closing balances?
6. Which energy/housing tax points or cross-border facts need the dated or territorial rule before approval?

## Sources

| Official source | Scope read | Read on |
|---|---|---|
| [LIVA, Ley 37/1992](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740) | Tax point/base, invoice-supported deduction, use/blocking, prorrata and investment adjustments, credit and refund clocks | 2026-10-26 |
| [RIVA, RD 1624/1992](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925), [invoice regulation](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696), [390 order](https://www.boe.es/buscar/act.php?id=BOE-A-2009-18472) | Elections, records, invoice details, return/SII/349 and annual-summary periods | 2026-10-26 |
| [AEAT January/1T 2026](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html), [later periods](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026/instrucciones-02-12-2t-4t-2026.html), [approved 303](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-1761) | Current ordinary output/input/credit mapping and signed adjustments, replacing stale sibling box references | 2026-10-26 |
| [TEAC RG 00/06654/2022](https://serviciostelematicosext.hacienda.gob.es/TEAC/DYCTEA/criterio.aspx?id=00%2F06654%2F2022%2F00%2F0%2F1) | Business/private property utility recovery, not a general mobile-phone percentage | 2026-10-26 |
| [RDL 7/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-6544), [RDL 18/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-14112), [RDL 25/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20265), [RDL 29/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823) | Dated/conditional energy rules and December housing provisions, with unresolved timing/index points inherited from the computation Guide | 2026-10-26 |
| [LGT, Ley 58/2003](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) | Conduct-based surcharge, penalty and collection classification | 2026-10-26 |

**Not yet confirmed:** the specific energy CPI/equality, investment acquisition-value boundary, non-intra-EU reverse-charge input-row, startup/differentiated-sector, simultaneous-use-change, correction-route and specialised fuel-result points recorded in [es-vat-return Sources](es-vat-return.md#sources); foral allocation and IGIC/IPSI. This review route does not close an unresolved computation by agreeing with a duplicate draft. Independent whole-pack review remains outstanding.

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
