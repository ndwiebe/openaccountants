---
name: es-capital-gains
description: Use this Guide to compute Spanish common-territory individual capital gains and losses for 2026. It covers transfer versus non-transfer classification, acquisition and disposal values, fees, improvements, depreciation, homogeneous-security identification, main-home reinvestment, over-65 relief, insured life annuities, pre-1994 abatement, repurchase-deferred losses, annual savings-pool integration and the current savings scale. Trigger phrases include capital gains Spain, ganancia patrimonial, sell shares, property gain, reinversión vivienda habitual, coeficientes de abatimiento, pérdida por recompra and compensación de pérdidas. Obtain the actual residence, asset and lot records, prices, eligible costs, prior-loss and repurchase history and relief evidence. The computation uses the taxpayer’s whole annual savings position and minimum allocation rather than taxing each sale through fresh first bands. Non-resident and special incoming-worker cases follow their companion routes.
version: 1.1
jurisdiction: ES
tax_year: 2026
last_updated: 2026-10-27
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
drafted_by: OpenAccountants
approved_by: pending
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain: individual capital gains and losses v1.1

Compute common-territory resident gains for 2026, then integrate losses, exemptions and the annual savings tax. This revision is sourced from the law; independent whole-pack review is pending and no accountant has signed it off.

## Who this applies to

[LIRPF art. 33](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a33) defines a gain/loss as a value change revealed by an alteration in asset composition, unless classified as another income category. A **transfer** gain normally enters the savings base; a non-transfer gain enters the general base ([arts. 45–46](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a46)). A long holding period does not itself create a lower tax rate.

An individual business's fixed-asset disposal can remain a capital gain under [art. 28.2](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a28); distinguish it from selling trading stock. Do not label every business-related sale trading income. Death has the art. 33.3.b no-gain rule for the deceased; the recipient's inheritance tax is separate. A gift can produce a donor gain, while the donor's gift loss is not deductible. Partition/co-ownership events require the art. 33.2 conditions and do not permit an automatic basis uplift.

This Guide covers common-territory IRPF. Use [es-income-tax](es-income-tax.md) for general/regional taxation and minimum allocation, [es-irpf-deductions](es-irpf-deductions.md) for regional credits, [spain-crypto-tax](spain-crypto-tax.md) for crypto-specific identification/reporting, [es-beckham](es-beckham.md) for an art. 93 election, and [the cross-border Guide](es-non-resident-income-tax-irnr-and.md) for ordinary IRNR and departure. Foral income tax, inheritance/gift tax, municipal urban-land tax and wealth tax require their own rules.

## Rates, bands and thresholds

| 2026 resident savings-base slice | Combined marginal rate | Quota at lower boundary | Source |
|---|---:|---:|---|
| 0–6,000 | 19% | 0 | [LIRPF arts. 66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a66) |
| >6,000–50,000 | 21% | 1,140 | [Arts. 66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a76) |
| >50,000–200,000 | 23% | 10,380 | [Arts. 66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a66) |
| >200,000–300,000 | 27% | 44,880 | [Arts. 66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a76) |
| >300,000 | 30% | 71,880 | [Arts. 66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a66) |

The state/autonomous savings halves are respectively 9.5/10.5/11.5/13.5/15% in each slice, fixed by those articles. The ordinary general-income scale has a separately determined regional half. The savings tax is **not** computed by automatically subtracting the whole personal minimum from every gain: allocate available minima between general/savings and state/regional calculations under [arts. 56/66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a56). Apply the tax-on-minimum mechanism where available, rather than simply tax `(gain −minimum)` through the progressive scale.

| Relief/loss item | Amount or period | Official source |
|---|---|---|
| Cross-offset between negative/positive savings pools | Maximum 25% of positive other-pool balance | [LIRPF art. 49](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a49) |
| Unused admitted loss carryforward | Four following years, mandatory maximum use in statutory order | [Art. 49](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a49) |
| Listed homogeneous-security loss deferral | Acquisitions two months before/after sale | [Art. 33.5.f](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a33) |
| Unlisted homogeneous-security loss deferral | Acquisitions one year before/after | [Art. 33.5.g](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a33) |
| Other sold asset repurchased | Within following year | [Art. 33.5.e](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a33) |
| Main-home reinvestment | Two years before/after disposal, subject to entitlement and amount | [RIRPF art. 41](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a41) |
| Over-65 insured-annuity reinvestment | Six months; cumulative qualifying reinvestment ceiling 240,000 | [LIRPF art. 38.3](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a38) |
| Pre-1994 abatement | Cumulative qualifying **transfer values** since 1 January 2015 capped at 400,000 | [DT 9](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dtnovena) |

## The base

### Identify and value the transaction

For an ordinary sale under [art. 35](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a35):

`acquisition_value = acquisition_price + eligible_acquisition_costs/taxes + improvements −required_depreciation`.

`transfer_value = actual_consideration_or_required_market_value −eligible_seller_transfer_costs/taxes`.

`gain_or_loss = transfer_value −acquisition_value`.

Exclude acquisition interest from basis. Distinguish capital improvements from repairs already deducted; do not deduct the same cost twice. For a let asset use the legally required depreciation adjustment, including the minimum depreciation, under [RIRPF art. 40](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a40). For gifts/inheritances use [LIRPF art. 36](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a36), including the succession-agreement and qualifying-business-gift carryover rules where applicable, not an invented cash purchase price.

For listed shares, unlisted shares, funds, exchanges and other special transactions, [art. 37](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a37) overrides the ordinary method as stated. Use FIFO for homogeneous securities under art. 37.2. Unlisted-share minimum valuation and fund-transfer deferral have their own conditions; actual proceeds alone do not override the statutory test. Identify lots, acquisition dates and fees before calculating.

### Main-home and annuity relief

Keep these three reliefs separate:

1. **Main-home reinvestment**, [LIRPF art. 38.1/RIRPF art. 41](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a41): `exempt_gain = positive_gain ×min(qualifying_reinvestment /required_reinvestment_amount, 1)`. Required amount is the transfer value less outstanding principal on the qualifying acquisition loan. There is no general 240,000 ceiling for this home relief. Reinvest within two years before/after; state the reinvestment intention where it occurs later than the sale year. Check the new home's actual main-home entitlement. Qualifying rehabilitation needs the article's route; the structural-rebuilding alternative also requires cost **over 25%** of the applicable acquisition/market value excluding land.
2. **Main-home disposal by a person over 65 or with qualifying severe/great dependency**, [art. 33.4.b](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a33): no reinvestment requirement or monetary ceiling. Establish the actual main-home/full-ownership position; do not grant the relief to a bare owner/usufructuary merely because they lived there. [RIRPF art. 41 bis](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a41bis) generally requires continuous three-year residence, twelve-month occupation after acquisition/completion, with statutory necessary-change exceptions, and permits the relevant main-home status in the two years before transfer.
3. **Over-65 reinvestment of proceeds from any qualifying asset into an insured life annuity**, [LIRPF art. 38.3/RIRPF art. 42](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a42): `eligible_reinvestment = min(actual_qualifying_reinvestment, max(240,000 −prior_eligible_reinvestment, 0))`; exempt only the proportional positive gain matching that amount. The ordinary deadline is six months, with the specified withheld-proceeds extension. The insured contract must name the taxpayer as beneficiary, pay at least annually, start within a year and meet the maximum 5% annual decrease/other contract conditions. Early anticipation of economic rights revives the affected gain.

A property that is neither the taxpayer's main home nor eligible for the annuity relief is not exempt just because they buy another property. If entitlement or the required-reinvestment denominator is not proved, do not compute a full exemption from the new purchase price alone.

### Pre-1994 abatement

Preserve the research trail, but apply the complete [DT 9](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#dtnovena) method:

- Only qualifying assets acquired **before 31 December 1994** and outside economic-activity use qualify; de-affection must meet the provision's more-than-three-year rule. Separate improvements by their own acquisition/holding component.
- Calculate the ordinary gain. For the general asset method, pre-20 January 2006 gain is `gain ×days_from_acquisition_through_19_Jan_2006_inclusive /total_holding_days`.
- **Listed securities and relevant fund units have DT 9.1.2's special 2005 wealth-tax value method**, not that automatic linear-day split. If sale value is at least the prescribed 2005 value, take the eligible pre-2006 gain by substituting that value as sale value. If sale value is below it, all the positive gain is treated as pre-2006 under that rule.
- Count pre-31 December 1996 holding years rounded up. The rate per year beyond two is 11.11% for the specified real estate/property-rich securities; 25% for qualifying listed shares; 14.28% for the residual assets. Apply the article's exclusions between those categories. The corresponding complete pre-2006 exclusion uses holding periods over ten/five/eight years respectively.
- Check cumulative qualifying **transfer values**, not gains, since 1 January 2015. For a disposal crossing the 400,000 ceiling, apply abatement only to the pre-2006-gain fraction corresponding to the unused transfer-value capacity. Prior use above the cap leaves no current capacity. Keep the actual prior-disposal ledger; do not assume 400,000 per asset or per year. The exact boundary wording and an exceptional fact pattern need verification where it changes the claim.

### Loss pools and final tax

Under [art. 49](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a49), first net investment-income items together, and independently net admitted transfer gains/losses together. If one pool is negative and the other positive, cross-offset only up to **25% of the positive pool**. Carry admitted unused losses for four following years in the statutory order and maximum permitted amounts; preserve origin-year/type balances and do not restart their clock. General non-transfer gains/losses use [art. 48](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a48), not the savings pool.

Before pooling, defer repurchase-blocked losses under art. 33.5 until the corresponding retained asset/securities are later disposed of. A deferred loss is not the same as a currently admitted loss carried forward for four years. Other art. 33.5 losses from consumption, unproved losses, gifts and gambling excess are not automatically deductible.

Integrate with all other savings income, apply available minima as above, then the combined savings scale and actual credits/payments on account. Compute **incremental gain tax** as annual tax with the relevant taxable item less annual tax without it where other income changes the bands; do not apply the first 6,000 band again to each disposal. Ceuta/Melilla uses the conditional art. 68.4 credit against attributable tax, not a different capital-gain marginal table; the non-resident-in-those-cities exclusions matter for movable-property gains ([art. 68.4](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a68)).

### Urban property acquired in 2012 and non-resident old assets

For an individual resident, [LIRPF DA 37](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#datrigesimaseptima) exempts **50% of the gain** on a qualifying urban property **acquired for consideration from 12 May through 31 December 2012**. Exclude acquisition from or transfer to the spouse, relatives by blood or affinity through the second degree, and the specified art. 42 group-connected entity, applying the statutory family/entity connection test. Do not halve a loss, proceeds or every property bought before 2013. For an eligible main-home reinvestment, apply this exemption **first**, then the proportional reinvestment exemption to the remaining gain under the incorporated conditions.

A non-resident **without a Spanish PE** has the separate [TRLIRNR DA 4](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#dacuarta)50% urban-property gain exemption for the same acquisition window, with the incorporated individual family/entity exclusions and the special entity-related exclusions where the transferor is an entity. Establish acquisition documents, urban classification, parties and connection before applying it. Purchaser withholding remains 3% of agreed consideration, credited against final tax; it does not become 1.5% because half the gain is exempt. [TRLIRNR DT 1](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#dt) preserves the specified old-asset transitions for non-PE individuals. A pre-1994 non-resident acquisition is therefore not automatically outside abatement: use the actual incorporated transition, eligible pre-2006 gain, asset class, residence and cumulative-disposal history. [AEAT’s current non-resident pre-1994 guidance](https://sede.agenciatributaria.gob.es/Sede/no-residentes/irnr-sin-establecimiento-permanente/determinacion-bi-irnr-sin-establecimiento-permanente/ganancias-patrimon-proced-bienes-adquiridos-1994.html), read 2026-10-27, expressly applies the 400,000 cumulative qualifying transfer-value cap for gains accrued from 1 January 2015. It also supplies the pre 20 January 2006 allocation,11.11%/25%/14.28% asset-class abatements for qualifying years to 31 December 1996 exceeding two, the proportional remaining-cap calculation and the 2005 wealth-value method for listed securities. Apply that current non-resident method using actual earlier disposals and asset history; the amount is not a fresh annual cap or a limit on gain.

## Deadlines and filing

Residents include the gain/loss and exemption/election evidence in **Modelo 100 for the accrual year**, using [LIRPF art. 14](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a14) timing and the approved campaign window. Do not invent permanent 1 April/30 June dates for the 2026 return filed in 2027. Maintain lot records, cost/depreciation evidence, deferred/carryforward ledgers and later reinvestment proof.

If reinvestment conditions fail, [RIRPF arts. 41/42](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820#a41) require the specified original-year supplementary declaration with interest in the special interval ending with the filing period for the failure year. A later sale and a new loss release do not automatically amend every old return.

For a non-resident's Spanish-property sale, the purchaser's **Modelo 211/3%** payment is due within one month; the seller's 210 window is the next three months after that first month, including nil/refund results ([IRNR regulation art. 14](https://www.boe.es/buscar/act.php?id=BOE-A-2004-14532#a14); [210 order art. 5](https://www.boe.es/buscar/act.php?id=BOE-A-2010-19707#a5)). Other non-resident disposals have their own reporting/withheld-income rules.

## Penalties and interest

Distinguish an unprompted late tax-due filing under [LGT art. 27](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27), an assessed under-declaration under [art. 191](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a191), an information failure and a special relief-recapture supplement. The ordinary voluntary surcharge is 1% plus 1% per complete month through twelve months; after twelve months it is 15% with the specified subsequent interest, subject to the article's conditions. Use [arts. 26/28](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a26) for the actual interest/collection stage; do not impose a universal 150% gain penalty or charge a surcharge to an original-year reinvestment supplement without checking its special rule.

## Cross-border points

Ordinary non-resident transfer gains use **19%**, subject to domestic exemption/treaty, rather than 24% solely because the person lives outside the EU ([TRLIRNR art. 25.1.f](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#a25)). Basis follows the applicable art. 24.4 method. A Spanish property buyer's 3% credit is on consideration; it is not the seller's final gain tax.

The IRNR transitional/qualifying-property and EU/EEA former-main-home reinvestment provisions require their own evidence. A treaty residence/gain article and MLI/protocol conditions must be read before overriding domestic source tax. Use [the cross-border Guide](es-non-resident-income-tax-irnr-and.md) for residence, PE, property return and individual exit-tax methods, and [es-beckham](es-beckham.md) for special-regime source/aggregation. A foreign broker does not remove a resident's worldwide gain, or convert a resident loss into an IRNR pool.

## Two worked examples that recompute

### 1. Ordinary disposal with costs

A hypothetical common-territory resident sells an asset in 2026 for **20,000**, pays eligible selling costs 100, and has acquisition price 10,000 plus eligible acquisition costs 50. No exemption, depreciation, earlier losses or other savings income applies; their minimum is already fully allocated to general income. Transfer value 19,900 less acquisition value 10,050 gives gain **9,850**. Savings tax is `6,000 ×19% +3,850 ×21% =1,948.50` ([LIRPF arts. 35/66/76](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a35)).

```oa-check
name: Spain 2026 resident sale with acquisition and transfer costs
inputs:
  sale_price: 20000
  selling_costs: 100
  purchase_price: 10000
  purchase_costs: 50
steps:
  transfer_value: sale_price - selling_costs
  acquisition_value: purchase_price + purchase_costs
  gain: transfer_value - acquisition_value
  tax: min(gain, 6000) * 0.19 + max(gain - 6000, 0) * 0.21
expected:
  transfer_value: 19900
  acquisition_value: 10050
  gain: 9850
  tax: 1948.50
```

### 2. Repurchase deferral and capped loss offset are different ledgers

A hypothetical resident has realised transfer losses **10,000**, of which **2,000** is correctly allocated to homogeneous repurchased shares and deferred under art. 33.5. Thus current admitted transfer loss is 8,000. Positive investment income is 10,000, with no other items or prior losses and no remaining personal minimum. Cross-offset is at most 25% ×10,000 =**2,500**. Savings base is **7,500**, tax **1,455**. Carry **5,500 admitted loss** to the four following years and separately retain **2,000 deferred repurchase loss** until its release event ([LIRPF arts. 33.5/49](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#a49)).

```oa-check
name: Spain 2026 repurchase-blocked loss and savings-pool cross-offset
inputs:
  realised_transfer_loss: 10000
  deferred_repurchase_loss: 2000
  positive_investment_income: 10000
steps:
  admitted_loss: realised_transfer_loss - deferred_repurchase_loss
  cross_offset: min(admitted_loss, positive_investment_income * 0.25)
  admitted_loss_carryforward: admitted_loss - cross_offset
  savings_base: positive_investment_income - cross_offset
  savings_tax: min(savings_base, 6000) * 0.19 + max(savings_base - 6000, 0) * 0.21
expected:
  admitted_loss: 8000
  cross_offset: 2500
  admitted_loss_carryforward: 5500
  savings_base: 7500
  savings_tax: 1455
```

## Ask the client first

1. What residence, territory and special-regime status applied in the disposal year?
2. What asset, lots, acquisition/transfer dates, actual values, costs, improvements and depreciation establish the gain?
3. What main-home ownership/use, age/dependency, loan balance and actual reinvestment/annuity evidence supports relief?
4. For pre-1994 assets, what holding/improvement history, 2005 securities value and cumulative qualifying disposals since 2015 establish abatement?
5. What current/prior savings pools, repurchases and deferred-loss releases affect offset and expiry?
6. What withholding, foreign tax, prior filings and relief-condition dates determine the balance and correction route?

## Sources

| Official source | Scope read | Read on |
|---|---|---|
|[AEAT non-resident pre-1994 asset guidance](https://sede.agenciatributaria.gob.es/Sede/no-residentes/irnr-sin-establecimiento-permanente/determinacion-bi-irnr-sin-establecimiento-permanente/ganancias-patrimon-proced-bienes-adquiridos-1994.html)|Current non-PE individual abatement,400,000 cumulative transfer cap,proportion and 2005 listed-security value method|2026-10-27|
| [LIRPF, Ley 35/2006](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764) | Arts. 28/33–38, 45–49, 56/66/68/76, DT 9: classification, basis, exemptions, loss pools, current rate and special old-securities valuation | 2026-10-26 |
| [RIRPF, RD 439/2007](https://www.boe.es/buscar/act.php?id=BOE-A-2007-6820) | Arts. 40–42, depreciation, main-home definition, reinvestment, annuity and recapture | 2026-10-26 |
| [TRLIRNR](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527), [IRNR regulation](https://www.boe.es/buscar/act.php?id=BOE-A-2004-14532), [210 order](https://www.boe.es/buscar/act.php?id=BOE-A-2010-19707) | Non-resident rate/basis and property-sale withholding/filing gateway | 2026-10-26 |
| [LIRPF DA37](https://www.boe.es/buscar/act.php?id=BOE-A-2006-20764#datrigesimaseptima), [TRLIRNR DA 4/DT 1](https://www.boe.es/buscar/act.php?id=BOE-A-2004-4527#dacuarta) | 2012 urban-property half-gain exemption, excluded related parties, ordering and specific non-resident historical transition | 2026-10-27 |
| [LGT, Ley 58/2003](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) | Late filing, recapture distinction, interest and penalty classification | 2026-10-26 |

**Not yet confirmed:** current primary judgment/administrative evidence for a bare-ownership/usufruct main-home exemption boundary; exact DT 9 equality-at-cap treatment where decisive; specialised non-cash restructuring, succession-agreement or treaty outcomes without the required fact/source record. Ordinary sale basis, savings-loss integration and current savings tax are supplied. Independent whole-pack review remains outstanding.

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
