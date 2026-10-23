---
jurisdiction: IS
version: 0.19
last_updated: 2026-10-23
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: {}
covered_by:
  IT-IND: iceland-income-tax
  IT-CORP: is-corporate-income-tax
  XB: is-cross-border
  TP: is-transfer-pricing
  SC: iceland-social-contributions
  PR: iceland-payroll
  VAT: iceland-vat
partial:
  IT-IND: "2026 resident salary, sole-trader and capital methods have nine arithmetic controls; resident foreign-relief workpaper and full-year positive-tax individual credit method added; other individual relief cases, special regimes, source conflicts, live filing and professional review remain open."
  IT-CORP: "2026 primary-source workpaper method added; positive-profit interest-cap and CFC implementation methods added; R&D, three financial-sector taxes and stated restructuring methods added with ten new controls; negative-profit financing, CFC timing/substance disputes, remaining treaty-specific relief, other sector/incentives, disputed restructuring/valuation/loss cases, operational and independent review remain open."
  VAT: "Direct/shared and private-use attribution, annual reconciliation, capital adjustment and stated property registration/construction methods have eleven controls; other special schemes, property start-date/valuation disputes, actual use/evidence, operational and independent review remain open."
  SC: "2026 ordinary employer and self-employed method rebuilt with three arithmetic controls; confirmation of the derived 2026 A1 component result, conflicting annual payment dates, fund-specific and independent review remain open."
  PR: "Twelve arithmetic controls, levy/PAYE penalty distinction and stated 2026 benefit valuation methods added; special workers, A1, disputed benefit/contractual bases, weekly rounding, operational and independent review remain open."
  TP: "2026 pricing and documentation draft added; independent Icelandic legal review, litigation, live filing and case-specific CbC/treaty procedures remain open."
  XB: "2026 cross-border screening draft added; residence boundary, treaty-specific PE/attribution and relief beyond the UK company/full-year individual credit examples, assessment categories outside the added annualisation and positive-tax credit methods, exit cases outside the added company/asset migration method, operational checks and independent review remain open."
---

# Iceland tax pack

Accountable owner: Michael Cutajar. Assigned writer: ChatGPT under [OWNERS.md](../../../OWNERS.md). Work relates to [issue #404](https://github.com/openaccountants/openaccountants/issues/404). This map preserves existing material and identifies work still needed; no domain is claimed complete.

| Tax domain | Existing Guide | Status |
|---|---|---|
| Individual income tax | [Income tax](iceland-income-tax.md) | Source-cited draft; stated scope and review gaps open |
| Corporate income tax | [Corporate income tax](is-corporate-income-tax.md) | Source-cited draft; 2026 method, stated specialist and review gaps open |
| VAT | [VAT](iceland-vat.md) | Source-cited draft; stated scope and review gaps open |
| Social contributions | [Social contributions](iceland-social-contributions.md) | Source-cited draft; stated scope and review gaps open |
| Payroll | [Payroll](iceland-payroll.md) | Source-cited draft; stated scope and review gaps open |
| Transfer pricing | [Transfer pricing](is-transfer-pricing.md) | Source-cited draft; independent review and stated gaps open |
| Cross-border | [Cross-border screening](is-cross-border.md) | Source-cited draft; stated substantive and review gaps remain open |

Formation, the overview and tax optimisation are supplementary and do not establish completion of the tax domains. All existing Guides and provenance are preserved.

## Official sources

For the new transfer-pricing draft, read 23 October 2026: [Income Tax Act 90/2003](https://www.althingi.is/lagas/nuna/2003090.html), [Regulation 1180/2014](https://island.is/reglugerdir/nr/1180-2014), [Regulation 766/2019](https://island.is/reglugerdir/nr/0766-2019), and [Skatturinn transfer-pricing guidance](https://www.skatturinn.is/atvinnurekstur/skattskylda/milliverdlagning/). The Guide records additional sources, access methods and administrative discrepancies. This source check does not reverify the legacy Guides.

## Local country-batch validation

The seven domain Guides now have the deep-tax section order and at least two recomputable examples each. The 23 October pass preserves the existing VAT, payroll and individual methods, adds their executable examples and source records, and replaces the stale social-contribution method. It corrects the employer-pension levy base, historical A1 reuse, the pension payment cycle and the distinction between PAYE surcharges and levy interest. This is preparation for a whole-country independent review, not professional attestation or completion of issue #404.

Remaining work is declared in `partial` above. Source access or passing arithmetic does not establish that every source conflict, special regime or live filing path has been resolved. Follow Michael's country batching instruction: finish and review the country batch locally before its next push.

The local finance/migration extension adds the Article 57b positive-profit interest method, CFC statutory screening and the Article 51/56a company/asset migration valuation, deferral, security and reporting method. The migration example excludes a supported retained Icelandic PE and separates interest from principal. No taxpayer-specific entitlement or professional review is claimed.

The local relief/VAT extension adds country/category foreign-income matching, a current-UK credit example, mixed-activity attribution and annual reconciliation, private-use and partly creditable foreign-service controls, and indexed capital-input adjustment rules. The Guide preserves the different property periods for clawbacks and additional deductions.

The CFC extension adds ownership/substance, profit/loss and reporting steps; the PE extension reconciles the domestic implementing regulation; the individual extension supplies the qualifying partial-year/short-stay annualisation method. The A1 note identifies the expired 2024–2025 component and a derived 2026 residual rate for independent confirmation, rather than treating an old rate table as current.

The independent source review of snapshot `355b3194` identified five corrections. The local correction pass clarifies eligible temporary employees’ day-based personal credit, replaces the payroll six-month shorthand with the common residence method, preserves the permanent-establishment and initial-stay qualifications for foreign-expert relief, screens Article 10 exempt bodies before the ordinary VAT shared-input method, and excludes wage-paying activities from the simplified RSK 4.10 route. This records findings addressed, not a completed professional review.

The review’s primary-source clarifications also establish the inclusive 700,000 full-year own-remuneration withholding boundary under Regulation 591/1987, while retaining any registration dispute separately, and identify the municipal percentage range as the ordinary Article 23 rule subject to checking the actual municipality and Article 24.

The next local country pass adds the approved R&D credit method, its 2026 amendment, signed project costs, purchased-cost and related-applicant ceilings, public-aid cumulation, approval/claim sequence, refundable balance and surcharge base. Four additional controls are preparation pending independent country review. This extension is not included in the prior published source-review snapshot and does not establish complete corporate coverage.

The same 23 October country pass adds the financial remuneration, additional-profit and bank-liability tax methods, separate bases and deductions, filing/payment controls and three further arithmetic checks. It preserves special classification/exception and live-filing limits; the previous source review does not cover this extension.

The same country delta now adds conditional domestic mergers/splits and sole-trade incorporation, separate cumulative loss-transfer conditions, continued tax/share bases despite accepted book revaluation, formation versus document-lodging dates and three further controls. The individual Guide refers sole-trader incorporation to that workpaper. Atypical structures, disputed valuations/losses, live procedure and independent review remain open.

The local VAT extension distinguishes voluntary commercial-rent registration from special construction registration, tenant/buyer declarations, continued adjustment obligations, per-property construction statements and guarantee/cancellation/refund reconciliation. Two controls cover required rental security and avoiding a second refund of unpaid cancelled output. Approval dates, actual use, construction valuation and current indexed repair/calculated-price inputs still require their stated evidence; all domains remain partial.

The resident-relief extension adds a full-year individual progressive-tax ceiling after personal credit, using current 2026 annual figures and a supported treaty credit branch. The official 2026 return handbook demonstrates the method on 2025 income; its figures are not reused as 2026 parameters. One further control covers foreign tax above/below the ceiling. Multiple-country/category, unused-credit, spouse and part-year cases remain separately open.

The independent delta review identified two clarifications: the authority-approved property guarantee waiver under Regulation 577 Article 5 with Regulation 515 conditions, and the foreign-municipal-tax requirement for Municipal Revenue Act Article 34 relief. The writer added both with sources, and the reviewer independently confirmed them at exact corrected snapshot `9de5b54d`.

The [independent country-delta review](../../../docs/research/2026-10-23-iceland-incentives-sector-restructuring-review.md) covers the incentives, three financial-sector charges, restructuring and property-VAT additions at `a82c59b0`, the individual-relief follow-on at `c6ada9af`, and the verified corrections at `9de5b54d`. It closes that source-review scope with all 56 controls passing. It complements the earlier core-pack review and does not attest to unchanged legacy content, live filing, every remaining specialist case or named-accountant review. All seven domains remain partial and issue #404 remains open.

A subsequent local country pass, based on published `ad570bbc`, adds 2026 employee-benefit classification, vehicle value/running-cost rules, ordinary versus owner housing, food, commuting, fitness, loan benchmarks and reporting controls. Six new arithmetic blocks supplement the prior 56. Social contributions refers to the same valuation method while preserving separate pension/levy bases. The prior review does not cover this new delta; it stays local for independent country review and does not establish complete payroll coverage.
