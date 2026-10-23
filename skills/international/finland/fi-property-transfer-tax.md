---
name: fi-property-transfer-tax
description: >
  Prepare Finnish property-transfer tax calculations for real estate and
  housing-company shares, distinguish contract and ownership-transfer dates,
  and reconcile the debt-free price. Statutory, exception and independent review
  remain outstanding.
jurisdiction: FI
category: property
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
---

# Finland property transfer tax v0.1

## Who this applies to

Use this draft for a buyer of Finnish real estate, a building or housing/real-estate-company shares. Classify the legal asset before calculating tax. A dwelling can be acquired through shares rather than direct ownership of land/buildings. The following official rates are displayed on Vero's current transfer-tax page: [Transfer-tax overview][overview]

| Acquisition | Rate |
|---|---|
| Real estate and buildings | 3% |
| Housing-company or real-estate-company shares | 1.5% |

This is a transfer-tax draft. Annual property tax, rental income, capital gains, VAT and financing deductions require separate work.

## Housing shares: establish the debt-free base

Vero's apartment guidance includes the purchase price, other agreed consideration and the unpaid company-loan portion allocated to the acquired shares. Immediate repayment versus later instalments does not remove that loan from the base. Reconcile the agreement and company records before applying the rate. [Housing-company shares][shares]

Keep the following preparation evidence: share identifiers, ownership percentage, purchase consideration, allocated debt statement, payment terms and the effective ownership-transfer date. Explain any mismatch between advertised cash price, contract consideration and debt-free price. These are practical reconciliation controls; unusual consideration and corporate transactions require further legal analysis.

## Deadlines and who files

| Purchase route | Ordinary guidance |
|---|---|
| Real estate requiring title/leasehold registration | Buyer files and pays before applying; registration application within six months of signing |
| Building without title registration | Buyer files and pays within six months of signing |
| Existing housing shares, private transaction | File and pay within two months of signing |
| Existing housing shares through an agent | Pay at signing; agent files |
| New construction under the stated ownership-transfer arrangement | Buyer files and pays within two months of ownership transfer, including agent-assisted sales |

[Vero deadline table][deadlines]. An agent does not take over the buyer's filing responsibility for a direct real-estate acquisition. Do not automatically start every two-month period from the same event. The guidance says first-home relief ended for purchases from 1 January 2024; historical purchases require their own eligibility and filing check. [Deadline table][deadlines]

Confirm any special acquisition route, holiday rule and current instructions before calendaring the actual transaction. No live filing or title registration was tested for this draft.

## Non-resident buyers and scope traps

Vero distinguishes ordinary corporate stock from housing/real-estate-company shares when both parties are non-residents. Its corporate-stock guidance still directs non-resident property-company-share buyers to register, file and pay. Do not transplant an ordinary corporate-stock exemption to housing shares. Foreign property-holding companies and indirect transfers need further scope review. [Corporate-stock guidance][stock]

Likewise, “first home”, a gift label or a stock-exchange connection does not itself establish exemption. Consideration, asset category, acquisition date and the exact exemption must be checked. This draft supplies no blanket exemption finding.

## Preparation sequence

1. Identify the buyer, seller, residences, asset and percentage acquired.
2. Read the signed agreement and establish the relevant signing/ownership dates.
3. Reconcile consideration and company debt to the supported tax base.
4. Identify the correct filer, return route, due date and payment reference.
5. Preserve submission confirmation, tax payment and registration evidence.

Record any unverified condition before advising on payment. Payment and filing are separate completion checks.

## Worked examples

### 1. Housing shares with allocated company debt

Assume cash consideration of EUR 180,000 and allocated unpaid housing-company debt of EUR 60,000, no other consideration and no exemption. Base EUR 240,000 at 1.5% gives EUR 3,600. Using cash consideration alone would understate the assumed tax by EUR 900.

```oa-check
name: Finland housing share debt free price
inputs:
  cash_consideration: 180000
  allocated_company_debt: 60000
  transfer_tax_rate: 0.015
steps:
  established_base: cash_consideration + allocated_company_debt
  transfer_tax: established_base * transfer_tax_rate
  cash_only_tax: cash_consideration * transfer_tax_rate
  omitted_tax: transfer_tax - cash_only_tax
expected:
  established_base: 240000
  transfer_tax: 3600
  cash_only_tax: 2700
  omitted_tax: 900
```

### 2. Direct real-estate acquisition

Assume EUR 250,000 is the correctly established taxable consideration for a direct real-estate purchase and no exemption applies. At 3%, transfer tax is EUR 7,500. This example assumes the base and asset classification; it does not establish additional-consideration or special-transaction treatment.

```oa-check
name: Finland assumed direct real estate transfer tax
inputs:
  established_consideration: 250000
  rate: 0.03
steps:
  transfer_tax: established_consideration * rate
expected:
  transfer_tax: 7500
```

## Ask the client first

- What legal asset and share are being acquired, and by whom?
- What are the signed agreement and ownership-transfer dates?
- What consideration and company debt are attached to the asset?
- Was an agent involved, and is the property newly constructed?
- What exemption is claimed, and what evidence supports it?
- Which filings, payments and registrations already exist?

## Sources and review limits

Official Vero text retrieved in the search index on 23 October 2026:

- [Current overview][overview], updated 7 January 2026.
- [Housing-share base guidance][shares].
- [Deadline table][deadlines].
- [Corporate-stock/non-resident distinction][stock].

Not yet confirmed: full Transfer Tax Act and amendment chain; detailed consideration rules for direct real estate and reorganisations; indirect/foreign property-company transfers; exemptions and historical transitions; refunds, penalties, interest, current forms and holiday rules. Independent review and professional attestation remain outstanding. Property and country coverage remain partial.

[overview]: https://www.vero.fi/en/individuals/property/transfer-tax/
[shares]: https://www.vero.fi/en/individuals/property/transfer-tax/buyer-of-a-flat/
[deadlines]: https://www.vero.fi/en/individuals/property/transfer-tax/instructions-for-filing-and-paying-transfer-tax/table-of-filing-and-payment-deadlines/
[stock]: https://www.vero.fi/en/individuals/property/transfer-tax/corporate-stock/
