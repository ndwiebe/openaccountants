# Azerbaijan 2026 source research receipt

Read date: 24 October 2026. Base: `b1f4afab6bc0f5bc1f2d1930e992179bbcae2013`, freshly cloned from the authoritative public repository. Branch: `codex/azerbaijan-country-pack-2026`. Issue #380 and the live open-PR list were read before edits; no competing Azerbaijan PR was present. The `OWNERS.md` allocation on `origin/codex/world-country-pr-split` was inspected, preserving all other country allocations.

## Retrieval and actual reading scope

- The State Tax Service legislation landing page links the Tax Code to `https://e-qanun.az/framework/46948`. The landing page rendered only a shell in the web reader; normal browser navigation timed out. The public register page resources identify `https://api.e-qanun.az/framework/46948`, which returned the official consolidated HTML URL. Its first unadorned fetch returned 403; a normal Referer/User-Agent fetch succeeded. No CAPTCHA or security warning was bypassed. The HTML's saved document timestamp was 23 October 2026. No Internet Archive substitution was needed.
- Full official consolidated Tax Code HTML was retrieved. Targeted reading covered arts. 2, 13–19, 33–34, 57–59, 71, 76-1, 95–130, 149–179, 218–221 and the relevant commencement annotations. Superseded `<s>` text was excluded for reading. Future commencement notes were retained: 413-VIIQD's 25 December 2026 leasing changes and 476-VIIQD's 1 January 2027 changes were not silently treated as already effective.
- Full official Social Insurance, Medical Insurance and Unemployment Insurance laws were fetched. Reading covered scope, sector definitions, contribution schedules, bases/exclusions, payment/reporting and tax-administration incorporation. See each Guide's specific articles.
- The current registered TP Rules at `https://frameworks.e-qanun.az/35/f_35074.html` were fetched and read, including scope, methods, documentation, interval, advance method agreements and Appendix examples. The authority still links an older 2017 PDF at `https://www.taxes.gov.az/uploads/qanun/2017/transfer.pdf`; it was read for comparison and rejected as the operative current source where amended. In particular, the current rules remove a blanket 500,000 exemption and use an interquartile median adjustment/documentation set absent from the older text.
- Cabinet Decision 556 size criteria were fetched from the official register; Cabinet Decision 56 employer-sector criteria were read on the tax authority page. The Ministry's 2026 social indicators confirm the 400 minimum monthly wage.
- The authority's 2026 PIT/payroll/profit/VAT booklets, amendment FAQ, TP/CFC FAQ, DTA administration Rules, treaty register and current CbCR summary were consulted. They support only the scope actually stated in the Guides; no blanket claim that all treaties, implementing decrees or sector schemes were read is made.
- Machine-readable hashes and exact retrieved statute URLs are in `2026-10-24-azerbaijan-source-retrieval.json`. Raw HTML/text stays in local `work/`, not the public source tree. Web-read official supplemental sources are cited with actual read dates in the Guides; they have no invented local hash receipt.

## Substantive replacements

Existing tax paths are preserved. The six existing tax Guides (individual, corporate, payroll, contributions, VAT and overview) are rewritten for 2026; TP and XB are added. The pack has eight tax Guides, each with the required nine sections and exactly two recomputing arithmetic examples. Existing platform frontmatter fields, attribution and full CTA marker-to-EOF blocks are preserved. Versions/date advance, existing dependencies remain. New Guides claim no platform metadata or professional review.

Replaced unsupported secondary citations and the old mixed 2025/prospective prose with article-level primary citations. The drafts distinguish 2026 salary PIT, the primary-workplace exemption, monthly contribution bases, the private medical 2,500 threshold, employer social insurance above 8,000, quarterly wage reporting, monthly payment obligations, ordinary versus new-business advances, actual simplified-tax eligibility, 2026 POS threshold weighting, domestic VAT input conditions, TP scope versus statement threshold, and gross non-resident versus PE taxation.

## Remaining core gaps

The README deliberately marks all seven domains partial:

| Domain | Missing computation or group |
|---|---|
| IT-IND | Land/building disposal and fixed-receipt individual tax computations; complete bank-deposit exemption conditions |
| IT-CORP | Ordinary expense deductions requiring Cabinet representation, employee housing/food and travel caps |
| VAT | Foreign B2C electronic-seller implementation; 25 December 2026 leasing transition |
| SC | Informal-worker medical-category commencement and implementing amount |
| PR | Director/corporate-office fees outside an employment contract |
| TP | Complete CbCR parent/surrogate/local filing and exchange-failure exceptions |
| XB | Full CFC inclusion; preferential-jurisdiction payment list/exclusions/interactions; migration/exit asset calculations; leasing transition |

These are unfinished research/implementation items. They are not statements that the law is necessarily unclear or inaccessible. Supported ordinary calculations are supplied without extrapolating into those gaps. Specialist PSA/pipeline, territorial/park/investment incentives, subsidy claims, special VAT schemes and country-specific treaty rates are separately named out of scope, not used as artificial core gaps. Tier 1 still requires a licensed human's actual sign-off.

## Adjacent accounting material, unchanged

`az-company-formation.md` remains dated to tax year 2025, contains unsupported formation timing/fee/capital claims, a secondary-law source chain and monthly payroll-reporting wording contradicted by the current payroll statutes. `azerbaijan-tax-optimization.md` still carries 2025 metadata, secondary-source claims and micro/simplified/startup/park descriptions that require separate primary re-verification. Their tax propositions must not override this batch's domain Guides. Under the repository's sibling-conflict rule, record them for their own correction PR; do not rewrite them as bonus accounting work in this country tax batch.

## Initial validation

The per-file arithmetic checker reported 16 blocks, zero failures. A global validator attempt initially could not import PyYAML; dependency setup and the required validators are recorded in the final review/validation receipt. This is writer research, not independent review or accountant attestation.
