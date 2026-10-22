---
name: gi-property-stamp-duty
description: >
  Prepare Gibraltar property stamp-duty working papers for ordinary conveyances, qualifying first- and second-time buyers, specified affordable-housing resales and principal mortgage security. Distinguishes property value from consideration, verifies buyer eligibility conditions, and supplies recomputable boundary examples. Based on the December 2024 statutory consolidation checked in October 2026. Leases, indirect interests, procedural filing requirements and individual relief evidence still require further work and independent professional review.
jurisdiction: GI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.2
verified_by: pending
sources:
  - url: "https://www.gibraltarlaws.gov.gi/uploads/legislations/stamp-duties/2005-73/2005-73(23-12-24).pdf"
    title: "Stamp Duties Act 2005, sections 19–19C and Schedule 1; 23 December 2024 consolidation"
    as_of: "2026-10-22"
---

# Gibraltar property conveyance and mortgage stamp duty

**Source-cited draft. Independent review pending.** Scope: ordinary conveyances, the stated buyer relief, specified special duty and principal mortgage security. This is not a complete property-tax Guide. The official index identifies 23 December 2024 as the current consolidation on the access date.

## Statutory calculation

Schedule 1 distinguishes whole-property value from consideration. For ordinary conveyances:

| Whole-property value | Duty on consideration |
|---|---|
| Up to £200,000 | Zero |
| Above £200,000 through £350,000 | 2% on first £250,000; 5.5% on excess |
| Above £350,000 | 3% on first £350,000; 3.5% on next £450,000; 4.5% above £800,000 |

These are alternative schedules, not one continuous marginal table. First/second-buyer treatment has separate eligibility and bands, set out below. Establish the property and transaction category before using a rate table. [Stamp Duties Act 2005, ss19A–19C and Schedule 1, pp13–14 and 28; accessed 22 October 2026](https://www.gibraltarlaws.gov.gi/uploads/legislations/stamp-duties/2005-73/2005-73(23-12-24).pdf).

## Worked boundary checks

Assume value equals consideration, with no relief or special duty:

- £200,000: £0.
- £250,000: £5,000.
- £350,000: £5,000 + £5,500 = £10,500.
- £400,000: £10,500 + £1,750 = £12,250.
- £900,000: £10,500 + £15,750 + £4,500 = £30,750.

The £200,000 exemption is not a universal deductible slice.

## Qualifying first- and second-time buyers

Section 19A defines a first-time buyer as an **individual** who has not previously purchased property subject to duty where the Gibraltar real property consisted of residential property. A second-time buyer has done so on only one previous occasion. Check the statutory Gibraltar-property history, not simply whether the person currently owns a home. A company does not meet the individual definition. [Section 19A(1)](https://www.gibraltarlaws.gov.gi/uploads/legislations/stamp-duties/2005-73/2005-73(23-12-24).pdf).

Schedule 1 paragraph (1A) requires **every purchaser** to be a first- or second-time buyer and the Gibraltar property conveyed to consist entirely of residential property for use as a single dwelling. The instrument must be accompanied by the Commissioner's required certificate establishing the buyer status of each purchaser. Knowingly or recklessly false/misleading certification is an offence; the current form and supporting evidence requirements need confirmation. [Section 19A(2)–(3), Schedule 1 conveyance paragraph (1A)](https://www.gibraltarlaws.gov.gi/uploads/legislations/stamp-duties/2005-73/2005-73(23-12-24).pdf).

| Eligible conveyance: slice of consideration | Duty |
|---|---|
| First £300,000 | 0% |
| Above £300,000 through £350,000 | 5.5% |
| Above £350,000 through £800,000 | 3.5% |
| Above £800,000 | 4.5% |

All figures: [Schedule 1, conveyance paragraph (1A)](https://www.gibraltarlaws.gov.gi/uploads/legislations/stamp-duties/2005-73/2005-73(23-12-24).pdf), current text checked for 2026. These are consideration slices for the eligible category, not an exemption that ends when the price exceeds £300,000.

**Buyer-status example:** for a £400,000 single dwelling with value equal to consideration, all purchasers qualifying and no special duty, the result is £50,000 × 5.5% + £50,000 × 3.5% = **£4,500**. If one joint purchaser is neither a first- nor second-time buyer, paragraph (1A) does not apply; with the same facts otherwise, ordinary duty is **£12,250**. A qualifying purchaser's ownership share does not make the whole instrument eligible.

```oa-check
name: Qualifying buyer versus ordinary conveyance at 400000
inputs:
  consideration: 400000
steps:
  - qualifying_duty: min(max(consideration - 300000, 0), 50000) * 0.055 + min(max(consideration - 350000, 0), 450000) * 0.035 + max(consideration - 800000, 0) * 0.045
  - ordinary_duty: min(consideration, 350000) * 0.03 + min(max(consideration - 350000, 0), 450000) * 0.035 + max(consideration - 800000, 0) * 0.045
expected:
  qualifying_duty: 4500
  ordinary_duty: 12250
```

## Specified affordable-housing transactions

Section 19B applies to a residential sale/transfer at **Beach View Terraces or Mons Calpe Mews within ten years of the first underlease assignment from Gibraltar Residential Properties Limited**. It requires a Commissioner's certificate and imposes additional duty payable by the **vendor or transferor**, in addition to other duty. The Schedule 1 certificate entry sets this at **7.5% of the amount or value of consideration**. Do not charge this to every Gibraltar resale or assume buyer relief removes it. [Section 19B(1)–(4), Schedule 1 certificate entry](https://www.gibraltarlaws.gov.gi/uploads/legislations/stamp-duties/2005-73/2005-73(23-12-24).pdf).

The Land Management Committee can direct non-payment for a forced sale or meritorious upgrade to a qualifying relevant property. That is a discretionary direction, not an automatic exemption on assertion of hardship. Government and Gibraltar Residential Properties Limited are exempt. Non-payment can lead to refusal to register the conveyance. Record the first assignment date, estate, consideration and any actual exemption direction before applying the special duty. [Section 19B(5)–(8)](https://www.gibraltarlaws.gov.gi/uploads/legislations/stamp-duties/2005-73/2005-73(23-12-24).pdf).

For an assumed covered sale at £400,000, within the ten-year period and without a direction or exempt seller, special duty is **£30,000**. An eligible buyer's £4,500 conveyance computation remains a separate item. Combining them for a transaction reconciliation gives £34,500 but does not change who owes the special £30,000.

Section 19C separately exempts the **first assignment of an underlease** at qualifying Government-developed affordable housing estates from ad-valorem duty. The definition requires residential property prescribed by the Minister in writing. Obtain the relevant prescription; the phrase “affordable housing” in marketing or a later resale does not by itself establish this exemption. [Section 19C](https://www.gibraltarlaws.gov.gi/uploads/legislations/stamp-duties/2005-73/2005-73(23-12-24).pdf).

## Principal mortgage security

For the only/principal/primary security, other than an equitable mortgage, Schedule 1's mortgage entry charges **£0.13 per £100 or fractional part** where the sum repayable does not exceed £200,000, and **£0.20 per £100 or fractional part** where it exceeds £200,000. The threshold selects the rate for the secured amount; it is not a progressive slice calculation. Collateral, substituted and equitable securities and releases have separate entries and must be classified separately. [Schedule 1, mortgage entry (1)–(5); section 35](https://www.gibraltarlaws.gov.gi/uploads/legislations/stamp-duties/2005-73/2005-73(23-12-24).pdf).

**Mortgage boundary example:** £200,000 secured is 2,000 units × £0.13 = **£260**. At £200,001, round the number of £100 units up to 2,001 and use £0.20 throughout, giving **£400.20**. This is security duty, not conveyance duty or a fee on the property's purchase value.

```oa-check
name: Principal mortgage threshold and partial hundred
inputs:
  lower_security: 200000
  higher_security: 200001
steps:
  - lower_duty: ceil(lower_security / 100) * 0.13
  - higher_duty: ceil(higher_security / 100) * 0.20
expected:
  lower_duty: 260
  higher_duty: 400.20
```

## Working-paper evidence

Record the instrument date, parties, consideration, independently supported whole-property value and legal character of the transaction. Ask the reviewer to confirm the chosen Schedule 1 category before using the arithmetic. Do not substitute the cash paid at completion for the entire consideration without examining the contract.

Attach a copy of the executed instrument or proposed execution version to the calculation. Keep valuation support separate from financing documents. Reconcile the calculation's consideration to the contract and explain any difference from the valuation. This is our preparation workflow, not an assertion that every listed document is a prescribed filing attachment.

## Scope remaining

Complete relief eligibility and prescribed estate evidence, other security types, leases, indirect property investments, gifts, electronic filing, payment timing and penalties remain unresolved. Income-tax treatment of rental profits and residential-property disposals is a separate question from stamp duty. Do not reuse this table for those transactions. A reviewer must check current amendments and the actual facts before filing or paying. No accountant attestation is claimed.
