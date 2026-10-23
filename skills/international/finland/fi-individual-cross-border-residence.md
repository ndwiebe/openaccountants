---
name: fi-individual-cross-border-residence
description: >
  Screen Finnish individual residence on arrival and departure, distinguish
  domestic status from treaty residence, and assemble a nonresidency claim.
  Income-specific taxation, treaties, statutes and independent review remain open.
jurisdiction: FI
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
---

# Finland individual cross-border residence v0.1

## Who this applies to

Use this draft for an individual arriving in Finland, leaving Finland or maintaining homes and activity in several countries. It is a residence-screening workflow, not a tax calculation or a conclusion about company residence, PE, social insurance or immigration status.

Vero's guidance bases domestic residence on the main abode/home or continuous presence exceeding six months. Temporary absences can leave continuity intact, and the period can cross calendar years. Exactly six months is not enough for that presence route, but the home route must still be checked. Do not replace the test with a universal 183-day count. [Detailed residence guidance, sections 2.4–2.5][detailed]

## Arrival and departure evidence

Prepare a dated timeline with arrival, departure, every absence, home availability, work and family facts. Registration in a population system does not itself resolve tax residence; the detailed guidance requires the actual situation to be assessed. A short stay can still involve a main home. [Detailed guidance, section 2.4][detailed]

For a foreign citizen departing Finland, check whether the main home remains or continuing presence still meets the residence test before treating departure as ending residence. Special statutory positions and a change of citizenship need their own analysis. [Nonresident-income guidance][nonresident]

## Finnish citizens leaving Finland

Vero describes continued residence for the relocation year and the following three tax years. Earlier nonresidency requires a specific request and evidence that substantial Finnish ties have ended for the relevant period. A planned temporary move of two or three years does not establish that those ties were broken. [Three-year guidance][three]

The detailed guidance distinguishes ties broken at departure from ties broken later: the latter generally leads to a claim from the following year's beginning. It describes a claim on the year's tax return, in MyTax or using Form 50A. Check the actual facts and legal effective date before selecting the claimed period. [Detailed guidance, sections 3.2 and 6.1][detailed]

## Treaty residence and income scope

Domestic nonresidency and treaty residence are separate decisions. Vero's treaty guidance discusses permanent home, centre of vital interests, habitual abode, citizenship and competent-authority agreement. Use the actual treaty's wording and sequence rather than importing a generic tie-breaker. [Treaty-article guidance][treaties]

A person can remain subject to domestic residence rules while a treaty limits Finland's taxing rights. Conversely, nonresidency does not itself remove taxation of every Finnish-source receipt. Classify employment, pensions, rent, investments and business income separately and verify the applicable source and treaty article. [Nonresident-income guidance][nonresident]; [Treaty-article guidance][treaties]

No universal withholding rate, treaty exemption or foreign-tax credit is supplied here. See the [payroll draft](fi-employer-payroll.md) for the ordinary wage-reporting preparation framework; it does not settle cross-border payroll eligibility.

## Preparation checklist

This is our practical evidence framework:

- Record all citizenships, historical residence decisions and the intended claim period.
- Reconcile travel and accommodation records with the actual home and work timeline.
- Identify family, property, business and other continuing connections.
- Obtain foreign tax-residence evidence and identify the actual treaty.
- Inventory income by category, source, payer and date, with deductions and foreign tax records.
- Preserve the claim, supporting evidence, authority decision and changes in circumstances.

The outcome must identify the facts relied on, the domestic status, any treaty conclusion and the periods covered. A timeline alone does not establish a legal result.

## Worked example

Assume a Finnish citizen relocates during 2026 and no earlier nonresidency claim succeeds. The ordinary three-following-years window covers 2027, 2028 and 2029. Its last year is 2029; 2030 follows it. This does not prove nonresidency in 2030: home, presence and special rules still require review. The calculation is year arithmetic, not a statutory status engine.

```oa-check
name: Finland assumed departure residence window
inputs:
  relocation_year: 2026
  following_years: 3
steps:
  last_year_of_ordinary_window: relocation_year + following_years
  year_after_window: last_year_of_ordinary_window + 1
expected:
  last_year_of_ordinary_window: 2029
  year_after_window: 2030
```

## Ask the client first

- What citizenships and prior residence decisions apply?
- Which homes were available, to whom, and on what dates?
- What travel, family, work and business connections continued after the move?
- Is the move permanent, and what evidence supports that?
- Which income and foreign tax assessments are involved?
- Has a nonresidency or treaty-residence claim already been made or decided?

## Sources and review limits

Official Vero text retrieved through the search index on 23 October 2026:

- [Detailed individual residence guidance][detailed].
- [Finnish citizens and the three-year rule][three].
- [Taxation of nonresident individuals][nonresident].
- [Treaty articles guidance][treaties].

Not yet confirmed: complete current Income Tax Act sections 9–11 and amendments, exact day-count and temporary-absence application, full substantial-ties and special-position cases, each treaty, income-specific source/rate rules, foreign-tax relief, forms and current procedures. Independent review and professional attestation remain outstanding. Cross-border coverage remains partial.

[detailed]: https://www.vero.fi/en/detailed-guidance/guidance/48999/tax-residency-nonresidency-and-residency-in-accordance-with-a-tax-treaty--natural-persons4/
[three]: https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/moving_away_from_finland/finnish_citizens_and_the_3year_rul/
[nonresident]: https://vero.fi/en/detailed-guidance/guidance/334489/taxation-of-income-received-by-nonresidents-natural-persons/
[treaties]: https://www.vero.fi/en/detailed-guidance/guidance/85707/articles-of-tax-treaties3/
