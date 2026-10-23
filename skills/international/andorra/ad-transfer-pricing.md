---
name: ad-transfer-pricing
description: >
  Identify related parties and support market pricing for Andorran company
  transactions: apply the distinct ownership and control tests, document
  services and financing, reconcile pricing adjustments, and prepare an
  advance-pricing request and annual agreement report. Use for Andorra
  intercompany charges, shareholder loans and related-party pricing.
  Country-by-country reporting and treaty dispute procedures need separate work.
jurisdiction: AD
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
---

# Andorra transfer pricing v0.1

## Who this applies to

Article 16 of Law 95/2010 requires related-party transactions to use normal market value: the value independent parties would agree in free competition. The provision is not limited to international transactions. Begin with the relationship test, then the actual transaction and its pricing evidence. A related-party invoice alone does not establish a market value. [Article 16(1)–(3)][law]

This source-cited draft uses the legal portal's current law and regulation consolidations, both expressly labelled as lacking official legal status. Full underlying-amendment reconciliation and independent review remain open. It covers company transaction pricing and advance-pricing agreements, not a complete country-by-country reporting or treaty-dispute procedure.

## Rates, bands and thresholds

These are relationship tests, not rates of tax or exemptions from pricing documentation.

| Relationship | Test | Source |
|---|---|---|
| Shareholder/participant and entity | At least 15%; at least 3% for securities admitted to trading on a secondary market | [Article 16(2)][law] |
| Entity indirectly participating in another | At least 25% of capital or net assets | [Article 16(1)(d)][law] |
| Common owners or specified family holders in two entities | Direct or indirect participation of at least 25% of capital or net assets | [Article 16(1)(f)][law] |
| Directors, including de facto directors | Separate relationship category; do not impose the shareholder threshold on it | [Article 16(1)(b)][law] |
| Family relationships specified in the law | Spouses and blood relatives through the third degree, direct or collateral line | [Article 16(1)(c), (f)][law] |
| Group entities | Direct/indirect control; majority voting rights establish the stated presumption | [Article 16(1)(e), (2)][law] |
| Resident entity and foreign PE; non-resident entity and Andorran PE | Express relationship categories | [Article 16(1)(g)–(h)][law] |

The opening test also addresses common direct/indirect participation in management, control or capital. Review the complete relationship, not only a percentage. Do not use the 25% indirect/common-ownership tests as a universal threshold. [Article 16(1)–(2)][law]

## The base

For each controlled transaction, establish what was supplied, by whom, to whom, the contractual terms and the market evidence supporting the value. The finance ministry can check and correct values. Its administrative valuation binds it for the other related parties and must not create combined income exceeding that actually arising from the transaction. This domestic rule does not itself prove that another country will grant a corresponding adjustment. [Article 16(3)–(4)][law]; [Regulation, Article 7][reg]

### Services and allocation evidence

The taxpayer must supply necessary group documentation, related-party contracts and other information enabling market value to be determined. For related-party employment remuneration, the regulation identifies market value with the remuneration's CASS contribution base; do not extend this special employment rule to management-service invoices or royalties. [Regulation, Article 7(4)–(5)][reg]

As a practical workpaper, reconcile the charge to the service supplied and the ledger, identify the beneficiaries, explain the allocation key and record the evidence for the selected pricing method. These are preparation steps to support market value, not a claim that the law prescribes a universal markup. Separate unsupported shareholder charges or duplicated costs for further analysis; neither an internal cost schedule nor a group policy proves deductibility by itself.

### Financing

Finance costs incurred by a resident entity on direct or indirect transactions with related resident individuals or related non-resident persons/entities are non-deductible unless the taxpayer proves financing terms comparable to those between independent parties. Record currency, amount, term, security, repayment, borrower credit risk and contemporaneous comparable terms. A market interest rate alone does not answer all financing conditions or other deduction restrictions. [Article 16(6)][law]

The examples below show pricing arithmetic only. The selected prices and rates are assumed supported facts, not statutory safe harbours, benchmarks supplied by this Guide or proof of a full tax deduction.

## Deadlines and filing

An advance-pricing request is made before the transactions and contains the proposed valuation, facts, circumstances and method. It must reflect that all related participants know of and accept the request. For a group, include the organisational/legal/operating structure, relevant entities and flows, functions/risks, intangibles, pricing policy, cost-sharing/service agreements, relevant existing agreements/disputes and annual report. Taxpayer documentation identifies counterparties and transactions, explains the method and resulting value, and supports shared-service allocation. These detailed requirements apply to the advance-pricing application; they must not be presented as a verified universal annual master-file/local-file submission obligation. [Regulation, Article 8][reg]

The ministry must notify acceptance or rejection of starting/applying the procedure within six months of receipt or required correction. The law and regulation provide deemed acceptance where no express decision occurs within that period and a reasoned valuation proposal accompanied the request. Preserve receipt, correction and notification evidence; do not infer approval from an informal enquiry or an incomplete file. [Law, Article 16(5)][law]; [Regulation, Article 8(5)][reg]

The agreement records the covered transactions, method, applicable periods and effective date. The law permits specified current/prior-period effect, provided those prior transactions have not already been adjusted by the ministry. Do not assume a fixed maximum term or automatic retrospective coverage. Significant economic changes require modification or cancellation under the law. [Law, Article 16(5)][law]; [Regulation, Articles 9–12][reg]

With the tax declaration, an approved-agreement holder submits a report identifying covered transactions and values, relevant economic changes and similar transactions with their prices. Calendar this with the entity's applicable tax return; no separate universal annual TP filing date is asserted here. [Regulation, Article 11][reg]

## Penalties and interest

Pricing adjustments and failure to substantiate the specified financing deduction are immediate tax-base risks. This draft does not supply an unverified standalone TP penalty or interest rate. Apply the current general tax-procedure enforcement rules separately after establishing the conduct and period. [Law, Article 16(4), (6)][law]

## Cross-border points

Andorran PEs and foreign head offices are included in the related-party rules. IRNR Article 16 also refers non-resident controlled transactions to the corporate-tax provision. Reconcile any pricing adjustment with source classification, withholding and PE attribution; pricing alone does not determine treaty relief. [IRNR, Article 16][irnr]

Country-by-country reporting is a separate obligation under Articles 16 bis–quater. The ministry cannot use that report alone to adjust transfer prices. A CbCR filing or group size below its threshold does not replace the transaction-level market-value analysis above. Detailed reporting triggers, notifications, exchanges and deadlines remain separate work. [Articles 16 bis–ter][law]

## Worked examples that recompute

### 1. Underpriced service charge

Assume a documented controlled service of 400 hours. A valid comparable, adjusted for actual terms, supports EUR 100 per hour. Only EUR 32,000 was recorded as supplier revenue. The supported charge is EUR 40,000 and the supplier's revenue shortfall is EUR 8,000. This example does not establish the recipient's deduction, foreign corresponding adjustment or any VAT result.

```oa-check
name: Andorra controlled service price reconciliation
inputs:
  hours: 400
  supported_hourly_price: 100
  recorded_revenue: 32000
steps:
  market_charge: hours * supported_hourly_price
  revenue_shortfall: market_charge - recorded_revenue
expected:
  market_charge: 40000
  revenue_shortfall: 8000
```

### 2. Financing amount reconciliation

Assume a EUR 200,000 loan outstanding for a full year, with independently supported comparable terms and a 4% simple annual rate. The booked finance expense is EUR 12,000. The supported interest amount is EUR 8,000, leaving EUR 4,000 above that amount. This is a pricing comparison; Article 16(6)'s proof requirement and every other deduction condition still apply. Four percent is an example assumption, not an Andorran safe harbour.

```oa-check
name: Andorra related financing pricing comparison
inputs:
  principal: 200000
  supported_rate: 0.04
  years: 1
  booked_interest: 12000
steps:
  supported_interest: principal * supported_rate * years
  excess_over_supported: booked_interest - supported_interest
expected:
  supported_interest: 8000
  excess_over_supported: 4000
```

## Ask the client first

- Who owns, controls or directs each party, including indirect holdings and relevant family links?
- What transactions occurred, under which agreements, and how do they reconcile to the ledger?
- What independent comparables and adjustments support the selected terms?
- For financing, who is the lender, where are they resident, and what evidence supports all loan terms?
- Is an advance agreement in place, what periods does it cover, and have circumstances changed?
- Are a foreign adjustment, treaty dispute or separate CbCR obligation involved?

## Sources and review limits

Read 23 October 2026. Source-cited draft; independent review and professional attestation remain outstanding. Current general enforcement rules, full method application, CbCR and treaty dispute procedures remain open. The topic's presence does not establish comprehensive TP or country coverage.

- [Law 95/2010, Article 16 and reporting provisions][law].
- [Current corporate-tax regulation, Articles 7–12][reg].
- [Law 94/2010, non-resident controlled transactions][irnr].

[law]: https://www.portaljuridicandorra.ad/L2010095
[reg]: https://www.portaljuridicandorra.ad/R20231229C
[irnr]: https://www.portaljuridicandorra.ad/L2010094
