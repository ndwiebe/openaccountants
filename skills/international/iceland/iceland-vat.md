---
name: iceland-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Iceland VAT (VSK) return for any client. Trigger on phrases like "prepare VSK return", "Iceland VAT", "virðisaukaskattur", "Icelandic VAT filing", or any request involving Icelandic VAT. Iceland is NOT an EU member but IS in the EEA. This skill covers Iceland only. MUST be loaded alongside vat-workflow-base v0.1 or later. Does NOT require eu-vat-directive (Iceland is not EU). ALWAYS read this skill before touching any Iceland VSK work.
version: 2.3
jurisdiction: IS
tax_year: 2026
last_updated: 2026-10-23
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland VAT (VSK): 2026 registration, return and payment method

**Status:** **Source-cited draft** by the OpenAccountants team. It is not accountant-authored, accountant-verified or an attestation. Current administrative guidance was retrieved from Iceland Revenue and Customs (Skatturinn) on 24 September 2026, and the consolidated VAT Act No. 50/1988 (Alþingi text in force from 1 September 2026) was read on 25 September 2026. Where Skatturinn's English page is older than the Act, this skill follows the Act and says so. This operational replacement retains the public `iceland-vat` skill's Iceland VSK scope for registration, rate/exemption classification, ordinary foreign-service liability, input VAT, return preparation, correction and payment.

Figures are for tax year 2026. Alþingi lists bills to amend the VAT Act that were tabled in September 2026; before relying on a rate, threshold or deadline for a period after this skill was written, check the current consolidated Act.

## Who this applies to

Obtain the legal seller, Icelandic ID (`kennitala`), VAT registration number, registration certificate, settlement period, start date and any prior return. Keep separate facts for each supply: customer identity and location, what was supplied, supply date, amount excluding VAT, invoice, rate/exemption reason, and import or foreign-service evidence.

Skatturinn says domestic and foreign companies and self-employed people selling taxable goods or services in Iceland generally register using form RSK 5.02. A business selling only exempt labour/services, or taxable goods/services of **ISK 2,000,000 or less in each 12-month period from commencement**, is exempt from registration duty; employees are not within that duty. A foreign taxable person follows the same rules. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

Apply the ISK 2,000,000 test with these conditions:

- The amount is taxable sales **excluding VAT**, measured over any 12-month period, not the calendar year.
- The duty to notify and register arises **as soon as it should be clear that sales will reach ISK 2,000,000** in a 12-month period. Do not wait until the amount has actually been passed.
- The small-business exemption is optional. A business under the limit may register voluntarily, and once registered it must charge VAT on its sales.
- A business starting VAT-liable activity must notify the Director of Internal Revenue no later than eight days **before** the activity starts. [Skatturinn VAT-register guidance](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/virdisaukaskattsskra/) and [VAT Act, Articles 4 and 5](https://www.althingi.is/lagas/nuna/1988050.html)

Registration is a factual test, not a rate election. A foreign company without an Icelandic permanent establishment that sells taxable services in Iceland must use an Iceland-domiciled representative; both are responsible for collection and payment. A foreign business that only supplies goods/services from abroad to Icelandic recipients, other than electronically supplied services, is not liable under the general statement on Skatturinn's page. Imported goods remain taxable at import. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

**VOES is separate.** It is an optional simplified, pay-only registration for qualifying foreign suppliers to non-taxable Icelandic customers. It covers listed electronic, telecom, paper/magazine-subscription, broadcasting and certain tourist services; it cannot be used where an Icelandic permanent establishment supplies the goods/services. A VOES seller cannot deduct input tax. A foreign B2C supplier of electronic services exceeding ISK 2,000,000 in a 12-month period must register/account for VAT, while a registered Icelandic B2B buyer that can count the VAT as input tax is not a trigger for the seller's registration. Establish the seller, customer status and supply before choosing ordinary registration, VOES or a different route. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) and [VAT Act, Articles 4(3) and 35](https://www.althingi.is/lagas/nuna/1988050.html)

## Rates, bands and thresholds

| Figures used below | Status | Official source |
| --- | --- | --- |
| 2026; ISK 2,000,000; 24%; 11%; 12-month; one month and five days; 5 April; ISK 4,000,000; 15 February; eight days; seven years; ISK 5,000; 1%; 10%; 30 days; 5,000 kg; 19.35%; 9.91% | Published administrative figures or periods. Apply only under the conditions stated in the method. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| 5 February; 1 March; 1 September | Annual and agricultural due dates. | [Skatturinn VAT-register guidance](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/virdisaukaskattsskra/) |
| ISK 10,000; ISK 6,000; ISK 100,000 (input-VAT correction cap); 15 days | Statutory thresholds and periods in Articles 20, 24, 26 and 35. | [VAT Act No. 50/1988](https://www.althingi.is/lagas/nuna/1988050.html) |
| ISK 100,000; ISK 24,000; ISK 20,000; ISK 4,800; ISK 19,200; ISK 50,000; ISK 5,500; ISK 250,000; ISK 10,000; ISK 2,400; ISK 1,950,000; ISK 12,000; ISK 8,000; ISK 300,000; ISK 11,000; 5 June | Hypothetical inputs or arithmetic outputs in the labelled worked cases, not authority figures. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| RSK 5.02 | Official registration form identifier. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| 0% | Case-only mathematical output for the zero-rated cases; the zero-rate category still requires its stated conditions. | [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) |
| RSK 10.24 | Official foreign-service VAT report identifier. | [Skatturinn form RSK 10.24](https://www.skatturinn.is/media/rsk10/rsk_1024.is.pdf) |
| RSK 10.26; RSK 10.01 | Official annual-reconciliation correction form and VAT statement identifiers. | [Skatturinn VAT-register guidance](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/virdisaukaskattsskra/) |

## The base

1. Confirm the entity, registration status, settlement period and prior statement.
2. Build invoice-backed sales, purchases and import schedules, then classify each line.
3. Reconcile output and supported input VAT, file the current electronic statement, pay the stated amount (or claim the refund) and retain confirmation.

### Classify every supply from evidence

Iceland VAT is generally charged on domestic business transactions and imports unless a direct exemption applies. The published rates are **24% standard** and **11% reduced** (plus a temporary 11% rate on listed fuels from 1 May 2026 to 31 August 2026, shown in the reduced-rate row below). Do not choose a rate from a merchant name, product label or the customer's country alone. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

| Classification | Operational treatment | Evidence to retain |
| --- | --- | --- |
| Standard taxable supply | Apply 24% to the VAT-exclusive consideration once the domestic taxable supply is confirmed. | Contract/order, invoice, customer/location and rate calculation. |
| Reduced taxable supply | Apply 11% only when the actual supply fits the statutory list. The conditions matter: hotel/guest rooms at 11%, and other commercial accommodation (private homes, lodges, cottages, hostels) only where the rent period is **less than one month**; campground facilities; food and other products for human consumption as defined in the Act's annex, including alcohol, and catering; passenger transport that is not exempt, including organised tours; travel-agent services for 11%-rated or exempt services; tour guiding; spas, saunas and baths that are not athletic facilities; access to tunnels and road structures; radio/TV subscriptions; books, newspapers and magazines (printed or electronic); music recordings without pictures; **hot water, electricity and oil for heating houses and swimming pools**; and listed contraceptives, reusable and children's diapers and menstrual products. Access to campground electricity, toilets and showers supplied to campsite guests is 11% whether included in the camping fee or billed separately; access unconnected to camping is 24%. [Administrative campground guidance](https://www.skatturinn.is/english/companies/value-added-tax/) **Temporary fuel rate (dated):** fuel under customs tariff numbers 2710.1221, 2710.1229, 2710.1930, 2710.2021, 2710.2029, 2710.2065 and 3826.0000 is 11% on import and taxable sale from 1 May 2026 to 31 August 2026 inclusive, and 24% before and after that window. Sellers must pass the reduction on in full to the final retail price. Input VAT on fuel bought in that window is the 11% shown on the invoice or Customs document (the usual input-VAT conditions and the vehicle block still apply). [VAT Act, temporary provision XLIX](https://www.althingi.is/lagas/nuna/1988050.html) | What was supplied, duration/location where relevant, and invoice description. |
| Zero-rated supply | Charge 0% only after meeting a stated zero-rate condition. See the services test below. Other examples include exported goods, international goods transport and domestic legs of it, passenger transport to/from Iceland, qualifying supplies to inter-country vessels/aircraft (not pleasure boats or private aircraft), and sale, lease, building and repair of ships and aircraft (not ships under 6 metres, pleasure boats or private aircraft). A zero-rated supply remains within VAT scope. | Export/customs or transport evidence; customer establishment and use evidence for services. |
| Exempt supply | Do not charge output VAT. Skatturinn lists, among others, health, social/education, certain culture/sport, listed public transport, postal, qualifying property rental (more than one month) and property sale, insurance, banking/financial, lotteries and certain artistic activities. Exempt-business purchases do not give input VAT credit. | Legal/service facts and any voluntary property-registration evidence. |
| Import of goods | VAT is collected by Customs on the customs value plus duties. A registered business may count import VAT as input tax for goods used in its taxable activity, on the Customs payment document. Blocked categories below still apply. | Customs declaration and payment document, supplier invoice, use. |
| Foreign-service purchase from abroad | Apply the Article 35 buyer-liability test in the foreign-service purchaser workflow and report on RSK 10.24 where it applies. | Supplier invoice/contract, service description, supplier country/Iceland VAT registration or agent status, purchaser's registration and input-credit facts, transaction date and full VAT-exclusive total consideration. [RSK 10.24](https://www.skatturinn.is/media/rsk10/rsk_1024.is.pdf) |

**Services sold to customers outside Iceland (current law).** Skatturinn's English page still describes the older rule that services must be wholly used abroad. The VAT Act as amended by Act No. 63/2024 (in force since June 2024) says:

- A service sold to a **business** that is neither domiciled in Iceland nor operating from a fixed establishment in Iceland is not taxable turnover (0%). This does **not** apply to: rental of property in Iceland under voluntary registration; services connected with property or structures in Iceland; hotel rooms and campsites in Iceland (whatever the rental period) and other accommodation in Iceland let for less than one month; access to road structures; passenger transport carried out in Iceland; admission to events, exhibitions, conferences, baths and spas held in Iceland; restaurant/catering service delivered in Iceland; rental of vehicles handed over in Iceland; telecom and broadcasting actually used in Iceland; and travel-agent, tour-operator and guide services used in Iceland. Those fall outside the zero rate and follow their normal domestic treatment (rate or exemption).
- A service sold to a **non-business** customer who is not resident in Iceland is 0% only for listed services (electronic, telecom, broadcasting, rights, advertising, consulting/engineering/legal/accounting and similar, data processing, non-exempt financial services, employment agency, rental of movables other than means of transport, and related obligations) **and** only where the service is actually used outside Iceland. For these non-business customers, a service relating to property, structures or movables in Iceland is always taxable in Iceland. [VAT Act, Article 12](https://www.althingi.is/lagas/nuna/1988050.html)
- Skatturinn's English page still carves out services related to movable property in Iceland for business customers too; that is the pre-2024 wording. Under current point 2 the only property exception for business customers is services connected with property or structures in Iceland.

For ordinary calculations, use `output VAT = taxable VAT-exclusive sales × confirmed rate`. Keep 24%, 11%, zero-rated and exempt sales in separate schedules. A zero rate is not an exemption: zero-rated supplies keep the right to deduct input VAT, while exempt activities do not. A transfer of inventory and operating assets on the sale of a business to a buyer whose business is registered or required to register is not taxable turnover; the seller must notify the Director of Internal Revenue within eight days of the transfer. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

### Test input VAT before deducting it

Input VAT is deductible only for VAT on goods, business assets and services bought for a VAT-liable business activity. The VAT must be verified by a sales invoice (or, for imports, the Customs payment document), and the vendor must have charged VAT and been VAT-registered at the transaction date. Check the invoice and vendor registration; a bank line alone is not sufficient. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) and [VAT Act, Articles 15, 16 and 20](https://www.althingi.is/lagas/nuna/1988050.html)

Apply an invoice-control check to every ordinary sales and purchase invoice before it enters the VAT schedules. Subject to the fact-specific Article 21 exception, confirm seller and buyer name and kennitala, seller VAT number, issue date, consecutive invoice number, clear supply description, quantity, unit price, total price, and whether VAT is included. The VAT amount must be shown separately, or the invoice must state that VAT is 19.35% of the total (standard rate) or 9.91% (reduced rate); on a sale to a registered buyer the VAT amount must always appear. One exception: a receipt of ISK 6,000 or less from a retailer, or from a seller that sells almost only to final consumers, is sufficient proof of input VAT even without the buyer's name and kennitala. Escalate a missing or inconsistent control instead of substituting a bank transaction. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) and [VAT Act, Article 20](https://www.althingi.is/lagas/nuna/1988050.html)

Do **not** include input VAT for the listed blocked categories:

- staff/owner cafeteria or dining and all food purchases, except for resale;
- owner/staff living quarters;
- owner/staff perquisites;
- vacation homes, summer cottages, children's nurseries and similar facilities for owner or staff;
- entertainment and gifts (this covers restaurant meals with clients);
- acquisition, operation and rental of passenger cars, and of vans and trucks (sendi- og vörubifreiðar) with a gross authorised weight of 5,000 kg or less that do not meet the minister's cargo-capacity and cargo-length requirements.

The vehicle block has a statutory exception: a registered business that sells or rents out vehicles, and an operator of passenger cars holding a special Icelandic Transport Authority (Samgöngustofa) licence for passenger transport in tourism, may deduct input VAT on inputs for that business. Such vehicles must be marked as the regulations require, and a later change to a use with less or no deduction must be notified before the change. Do not deduct car VAT merely because the car is used mostly for business. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) and [VAT Act, Article 16](https://www.althingi.is/lagas/nuna/1988050.html)

### Mixed taxable/exempt activity and private use

**Entity-status screen first.** A VAT-registered body exempt under Income Tax Act Article 4 falls within the overriding [Input VAT Regulation 192/1993 Article 10](https://files.reglugerd.is/pdf/0192-1993/current), which permits only inputs exclusively connected with taxable sales under its general rule. Do not give such a body the ordinary shared-turnover deduction below. Article 10 separately permits qualifying public-service enterprises taxable under VAT Act Article 3(1)(4) to attribute non-property inputs to taxable operations under Article 6, provided those operations are clearly separated financially and in the accounts. Establish that status and its special method before any deduction.

For an ordinary taxpayer outside that override, use [Input VAT Regulation 192/1993, Articles 3–9](https://files.reglugerd.is/pdf/0192-1993/current), after testing invoice evidence and statutory blocks. Keep each activity identifiable in the ledger:

1. **Direct taxable use:** deduct supported VAT on inputs bought solely for the taxable part, subject to the other deduction restrictions. Zero-rated supplies remain taxable activity for input-credit purposes; do not put them in the Article 2 exempt denominator merely because output VAT is zero.
2. **Direct exempt use:** no deduction for inputs solely serving the exempt activity.
3. **Genuinely shared inputs:** multiply their otherwise-eligible VAT by annual VAT-exclusive taxable sales divided by annual total turnover. Exclude operating-asset sales and the other Article 11(3) items from this ratio. Do not apply the shared ratio to every purchase or use an asset disposal to inflate it.
4. **Provisional periods:** the preceding accounting year's ratio may be used during the year; reconcile to the actual annual ratio in the last settlement period. In the first year, calculate a provisional ratio for each period and reconcile in the last period. Use the authority's reconciliation form for that year; a historic form does not establish current box labels.
5. **Private/nonbusiness use:** Article 6 instead limits deduction to the evidenced taxable-business use. Turnover apportionment does not prove private use. Blocked inputs stay blocked even when a business-use percentage is high.

[Regulation 192/1993, Articles 3–6](https://files.reglugerd.is/pdf/0192-1993/current); [VAT Act, Articles 12 and 16](https://www.althingi.is/lagas/nuna/1988050.html)

**Buildings and vehicles have special rules.** For separately identified building parts, Article 7 uses construction-cost attribution, with floor area permitted where the parts are comparable in quality. Attribute repair/improvement work directly where possible and require the invoice to identify the worked-on part; shared exterior/services work can use the specified floor-area method. A rented building is not taxable-use property merely because the tenant is a business: establish the landlord's voluntary registration. For the same building part used for both activities, Article 8 refers to Articles 3–6 where Article 7 cannot allocate it. Owner/staff residential accommodation remains blocked. [Regulation 192/1993, Articles 2 and 7–8](https://files.reglugerd.is/pdf/0192-1993/current)

Article 9's listed vehicles have an exclusive-taxable-use acquisition rule, subject to its narrow documented commuting exception for qualifying goods vehicles and its output-tax/notification conditions. Do not claim a turnover percentage of a passenger car merely because it has some taxable business use. A final vehicle result needs the vehicle category, equipment, use, registration and applicable exception. [Regulation 192/1993, Articles 2 and 9](https://files.reglugerd.is/pdf/0192-1993/current)

**Specified blocked-input exceptions.** The regulation permits certain structural cafeteria/dining-room building inputs and fixtures, and ordinary eligible raw materials/energy/services for taxable food sales to staff; loose dining-room furniture/equipment remains blocked. It also distinguishes low-value items plainly intended for advertising from blocked gifts. Establish each exception from the actual supply rather than reclassifying restaurant entertainment as advertising. [Regulation 192/1993, Article 2](https://files.reglugerd.is/pdf/0192-1993/current)

### Capital-input adjustments when use changes

Maintain a separate asset adjustment register. [Regulation 192/1993, Articles 12–16](https://files.reglugerd.is/pdf/0192-1993/current) supplies the following method:

| Screen | Rule | Source |
| --- | --- | --- |
| Movable asset or asset group | Cost at least ISK 250,000 excluding VAT | Regulation Article 12(1)(1) |
| Building/structure works | Total relevant works at least ISK 500,000 excluding VAT | Article 12(1)(2) |
| Mixed-use ratio change | A fall of at least 10 percentage points triggers the specified clawback; a rise of at least 10 points can support an additional deduction, relative to acquisition or the previous specified adjustment | Articles 12(3), 13(3) |
| Movable change-of-use window | Five years from the end of the ordinary two-month period of acquisition | Article 14(1) |
| Property change of use | Clawback window twenty years; increased-deduction window six years, measured under the distinct Article 14 rules | Article 14(2) |
| Later-year remaining share, movables | 80% next calendar year, 60% second following year, falling by 20 percentage points per year | Article 14(3)(1) |
| Later-year remaining share, property | 95% next calendar year, 90% second following year, falling by 5 percentage points per year | Article 14(3)(2) |
| Same-calendar-year changes | Use Article 14's ordinary two-month factors, rather than the later-year percentages | Article 14(3) |
| Ratio-change annual correction | One fifth for movables or one twentieth for structures of the indexed VAT amount to be adjusted, under the statutory ratio-change method | Article 14(4) |

For a change within the acquisition/works settlement period, compute input VAT on the changed basis in that period. For a later change, first index the VAT under Article 14 using the construction index at the specified period ends, then apply the appropriate adjustment share. Identify a full change of use separately from an annual ratio change; the schedules are not interchangeable. Post the adjustment to the input account for the adjustment period and complete the authority's required adjustment report. Keep original VAT, original deduction ratio, dates, prior adjustments, actual new use, index values and the calculation together. [Regulation 192/1993, Article 14](https://files.reglugerd.is/pdf/0192-1993/current)

Before reversing, test Article 12's exceptions, including taxable disposals, qualifying zero-rated disposals, specified forced sales and voluntarily registered rental. For a property/business transfer, Article 15 permits assumption of adjustment obligations only to the extent of the buyer's entitlement; the seller adjusts any balance. Both parties notify Skatturinn within eight days, with the year/period amounts, proportions and the buyer's assumption statement. A sale described as “VAT-free” does not extinguish an adjustment obligation. [Regulation 192/1993, Articles 12 and 15](https://files.reglugerd.is/pdf/0192-1993/current)

This method does not establish voluntary-registration eligibility, a property's actual use or the special vehicle exception without their documents. Those determinations and the actual accepted reporting route remain for review.

Build a purchase schedule with supplier, date, invoice number, VAT-exclusive amount, VAT shown, vendor VAT status, business use, classification and deduction result. Reconcile the deductible total to the purchase ledger and evidence before netting it against output VAT.

### Foreign-service purchaser workflow

Article 35 of the VAT Act makes the Icelandic buyer pay VAT on services bought from a business domiciled or established abroad. It does not turn every foreign invoice into a VAT charge.

1. Record the foreign seller, country, invoice/contract, transaction date, service type and VAT-exclusive total consideration. Check whether the seller, its agent or representative is on the Icelandic VAT register for that activity; if so, the buyer route does not apply. [VAT Act, Article 35](https://www.althingi.is/lagas/nuna/1988050.html)
2. Find which buyer group applies:
   - **Buyer in exempt activity** (for example a bank, insurer, clinic or school): pays VAT on the full consideration of any taxable-type service bought from abroad for that activity. No threshold.
   - **VAT-registered buyer**: pays VAT only **to the extent** that VAT on the service could not be deducted if it had been bought in Iceland, for example a service used for a blocked purpose (entertainment, staff perquisites) or the exempt share of mixed activity. A registered buyer who could deduct all of it pays nothing on this route. VAT must always be paid under this article where the service is supplied or used in connection with an import of goods, even if it would otherwise be deductible; report it on RSK 10.24.
   - **Any other buyer** (for example a private person, or a business below the registration limit and not registered) who buys rights, advertising, consulting/engineering/legal/accounting and similar services, data processing, non-exempt financial services, employment agency, rental of movables (other than means of transport) or related obligations: pays only if these purchases total **ISK 10,000 or more excluding VAT in the ordinary two-month period**.
3. For a liable purchaser, calculate `foreign-service VAT = liable VAT-exclusive consideration × applicable Icelandic rate`. The Act applies domestic rules, so this is normally 24%; a service that would be 11% if bought in Iceland is self-assessed at 11%. For a registered buyer with a partly deductible service, the liable part is the non-deductible part; apply the established attribution method above and retain the non-deductible share. Hold the result if the needed attribution evidence is missing. Complete **RSK 10.24** with the service line(s), supplier and buyer details, the VAT-exclusive consideration, the VAT, and the stated use purpose (the form prints 24%; show a lower applicable rate separately). Submit with payment by the fifth day of the second month after the ordinary two-month period in which the purchase falls. Late payment carries the same 1% daily surcharge, up to 10%, as domestic VAT. Retain the form, invoice and input-credit analysis.

This is a purchaser-liability payment route. Do not also claim the same amount as ordinary input VAT. [VAT Act, Article 35](https://www.althingi.is/lagas/nuna/1988050.html) and [RSK 10.24](https://www.skatturinn.is/media/rsk10/rsk_1024.is.pdf)

## Deadlines and filing

The ordinary settlement periods are Jan–Feb, Mar–Apr, May–Jun, Jul–Aug, Sep–Oct and Nov–Dec. The electronic VAT statement and payment are due **one month and five days after period end**: for example, Jan–Feb is due 5 April, moved to the next business day if the date is a weekend or Icelandic public holiday. A registered person must file electronically even with no sales; otherwise Skatturinn estimates the VAT. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

The return requires total VAT-exclusive sales by tax rate, zero-rate sales, and total output and input VAT. Do not reproduce historic, unlabeled return-field letters: use the current Skatturinn filing screen and match each value to the schedules. After filing, payment can be made through Icelandic online banking. A foreign-bank payment must use the current official instructions and identify the VAT registration number, year and period. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/)

Use this working sequence:

1. Lock the legal entity and settlement period; check whether the business is registered and whether a special period applies.
2. Reconcile invoices, credit notes, import documents and payment records to a sales and purchase schedule. Do not record gross bank deposits as sales without the underlying evidence.
3. Classify each sale as 24%, 11%, zero-rated, exempt or unresolved; total each group excluding VAT.
4. Compute output VAT for confirmed taxable sales. Keep zero-rated and exempt values visible even where output VAT is zero.
5. Test each purchase for a valid VAT invoice or Customs document, registered vendor, VAT-liable business use and blocked/mixed-use status; total only supported deductible input VAT.
6. Compute `net VSK = total output VAT − deductible input VAT`. A positive difference is payable. A negative difference is refundable: file the credit statement by the same deadline. If the statement is filed on time and accepted, the refund is paid within twenty-one days after the filing deadline. Unpaid public charges and taxes are set off against it first, and no refund is paid while an earlier period's VAT rests on an estimate. [VAT Act, Articles 15, 24 and 25](https://www.althingi.is/lagas/nuna/1988050.html)
7. Enter the totals in the live electronic statement, review the confirmation, pay any stated liability or record the refund, and archive the submission, ledger and support.

### Period choices, amendments and record controls

A taxpayer with taxable sales below **ISK 4,000,000 in a whole calendar year** may request annual settlement for the following year; apply before 15 February for that year. The annual due date is 5 February. Six-month settlement is available only to agriculture, with due dates of 1 September (January–June) and 1 March (July–December). Monthly settlement can be available where input VAT is generally higher than output VAT because a major share of turnover is exempt, or where reduced-rate sales dominate but standard-rate input VAT dominates; apply at least one month before the next period. A changed settlement period must start at the beginning of a two-month period and applies for at least two years. These are application-based alternatives, not automatic selections. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/), [Skatturinn VAT-register guidance](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/virdisaukaskattsskra/) and [VAT Act, Article 24](https://www.althingi.is/lagas/nuna/1988050.html)

A business re-registered after Skatturinn removed it from the VAT register must use **monthly** periods for at least two years, with the due date 15 days after each month ends. The same applies on registration where the individual, or an owner, board member or manager of the company, was bankrupt, or was involved in a company that went bankrupt, within the previous five years (the Act sets the exact tests). Confirm the period on the registration record before applying the ordinary timetable. [VAT Act, Article 24](https://www.althingi.is/lagas/nuna/1988050.html)

Notify Skatturinn of a post-registration change in operations, including a different activity or VAT-taxable cessation, within eight days. Keep VAT accounts, sales documents and vouchers available to the authority. Every taxable person must keep the books, settlements and documents behind its VAT returns for seven years from the end of the accounting year. For a foreign company using an Icelandic representative, the representative must keep the complete VAT accounts and supporting documents in Iceland for at least seven years after the accounting year. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) and [VAT Act, Article 17](https://www.althingi.is/lagas/nuna/1988050.html)

### Correct a filed ordinary statement

1. Identify the exact settlement period, original filing/assessment status, the omitted or wrong record, and the schedules that change. Preserve the original statement, correction calculation and evidence.
2. Before assessment for that period is complete, the taxpayer can correct the submitted statement electronically. Skatturinn states that assessment is completed one month after the due date. Use the live service rather than a paper workaround unless the authority's stated exception applies.
3. Under-claimed input VAT of up to ISK 100,000 may instead be included in the statement for the period in which it is discovered, but no later than the statement for the last period of the same operating year. Larger or later input corrections go through the formal correction route.
4. After the annual reconciliation identifies a difference between the returns and annual accounts, use **RSK 10.26**. A taxpayer with a settlement period shorter than two months cannot use RSK 10.26 for after-year corrections and instead files one RSK 10.01 statement for each affected period. Do not apply either correction route to a mixed-activity allocation or capital-use adjustment without the applicable specialised method.

[Skatturinn VAT-register correction guidance](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/virdisaukaskattsskra/) and [VAT Act, Article 26](https://www.althingi.is/lagas/nuna/1988050.html)

## Penalties and interest

Failure to file permits an estimated assessment. Filing a statement after an estimate adds an ISK 5,000 charge for each statement not filed on time. Late payment has a 1% penalty for each started day after the due date, up to 10%; the same penalty applies to estimated VAT and to an excessive refund. If the VAT is still unpaid one month after the due date, late-payment interest is also charged, and the interest runs from the original due date. Sufficient cause can support cancellation of the penalty. An appeal to the Director of Internal Revenue is generally due within 30 days of the decision; a further written appeal to the Internal Revenue Board is due within three months of the decision letter. Use the live account/notice and current procedural instructions for an actual dispute. [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/) and [VAT Act, Articles 27 to 29](https://www.althingi.is/lagas/nuna/1988050.html)

## Cross-border points

Classify outbound services using the current Article 12 business/nonbusiness tests in the base section; a customer's foreign address alone does not prove zero rating. For foreign purchases use the Article 35 purchaser workflow above, including registration, credit entitlement, service class and the specific 10,000-per-period test where applicable. A foreign seller must establish whether ordinary registration, a representative or VOES applies before filing. Imports require Customs evidence and the import-base rule, separately from services. [VAT Act, Articles 4, 12 and 35–36](https://www.althingi.is/lagas/nuna/1988050.html)

## Worked examples that recompute

These cases are arithmetic illustrations from the cited rules, not filing results. They assume the evidence and eligibility stated in each case; they do not establish VAT treatment for a different supply. Rules applied: [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/), [VAT Act No. 50/1988](https://www.althingi.is/lagas/nuna/1988050.html) and [RSK 10.24](https://www.skatturinn.is/media/rsk10/rsk_1024.is.pdf).

| Case | Facts and calculation | Expected VSK result |
| --- | --- | --- |
| Standard domestic sale with supported input | Registered Icelandic business sells a confirmed 24% domestic service for ISK 100,000 excluding VAT: output `100,000 × 24% = 24,000`. It has a valid invoice for a wholly taxable-business purchase of ISK 20,000 plus ISK 4,800 VAT: deductible input 4,800. | **ISK 19,200 payable** (`24,000 − 4,800`). |
| Reduced-rate sale | Registered business lets a hotel room (a stay of less than one month) for ISK 50,000 excluding VAT. | **ISK 5,500 output VAT** (`50,000 × 11 ÷ 100`); input VAT depends on separately tested purchases. |
| Zero-rated export | Registered seller has a documented qualifying export of goods for ISK 250,000 and a valid input-VAT invoice for ISK 4,800 used in the taxable/zero-rated activity. | **No output VAT** on the export and **ISK 4,800 refundable**. File the credit statement by the normal deadline; if filed on time and accepted, the refund is due within twenty-one days after the deadline, less any set-off for unpaid taxes. |
| Input is blocked | Registered business buys owner/staff food for ISK 10,000 plus ISK 2,400 VAT. | **No deductible input VAT** for that purchase. |
| Registration screen | A new business has ISK 1,950,000 of taxable sales (excluding VAT) in the relevant 12-month period and it is **not** yet clear that sales will reach ISK 2,000,000. | Within the ISK 2,000,000-or-less exemption. As soon as it becomes clear sales will reach ISK 2,000,000 in a 12-month period, it must notify and register. Do not issue/collect VAT without first resolving registration status. |
| Missed ordinary return | A registered business makes no sales in Mar–Apr. | It still files the electronic return by **5 June** unless that day moves to the next business day. |
| Foreign specialist service used in exempt activity | An exempt Icelandic business buys a foreign specialist service (standard-rated, 24%, if bought in Iceland) for ISK 100,000 from a supplier with no Iceland VAT registration/agent. | Complete RSK 10.24 with the buyer/supplier, date, service, ISK 100,000 VAT-exclusive consideration and **ISK 24,000 VAT** (`100,000 × 24 ÷ 100`); pay by the form's stated deadline. |
| Foreign service used by a registered buyer for a blocked purpose | A fully taxable registered business buys ISK 50,000 of foreign consultancy (standard-rated, 24%, if bought in Iceland) used wholly for staff perquisites, from a supplier with no Iceland VAT registration/agent. | VAT would not be deductible if bought in Iceland, so the buyer pays **ISK 12,000 VAT** (`50,000 × 24 ÷ 100`) on RSK 10.24 and claims no input VAT. If the same service were used wholly in taxable activity, nothing would be payable on this route. |
| Small foreign purchase by a non-registered buyer | An unregistered sole trader below the registration limit buys ISK 8,000 of foreign advertising in Jan–Feb and nothing else from abroad in that period. | Below the ISK 10,000 per-period threshold: **no RSK 10.24 payment**. At ISK 10,000 or more in the period, VAT at the applicable rate (24% for advertising) on the whole amount would be due. |
| Consultancy sold to a foreign business | An Icelandic registered consultant sells ISK 300,000 of advice to a Norwegian company with no domicile or fixed establishment in Iceland; the advice does not relate to property or structures in Iceland. | **0%, no output VAT**; input VAT on related costs stays deductible. If the same customer instead bought hotel rooms in Iceland, 11% would apply. |
| Temporary fuel rate | A registered fuel retailer sells diesel under tariff number 2710.1930 for ISK 100,000 excluding VAT in July 2026, and the same again in September 2026. | July sale: **ISK 11,000 output VAT** (`100,000 × 11 ÷ 100`). September sale: **ISK 24,000** (`100,000 × 24 ÷ 100`). A registered buyer deducts the VAT actually invoiced, subject to the usual conditions. |
| Correction before assessment | A Mar–Apr electronic statement omitted a supported ISK 100,000 standard-rate domestic sale. The period's assessment is not complete. | Preserve the correction schedule and submit the electronic correction for that period. The missing **ISK 24,000 output VAT** (`100,000 × 24 ÷ 100`) is included in the revised period data; do not invent a separate delta box. |

### Recomputable arithmetic controls

The blocks below test the stated ordinary sale, reduced-rate room, supported zero-rated refund, foreign-service boundary and dated fuel cases. Inputs require the eligibility/evidence in the corresponding table row. A passing block does not establish that eligibility.

```oa-check
name: Iceland standard sale less supported input VAT
inputs:
  net_sale: 100000
  supported_purchase_net: 20000
steps:
  - output_vat: net_sale * 0.24
  - deductible_input: supported_purchase_net * 0.24
  - net_payable: output_vat - deductible_input
expected:
  output_vat: 24000
  deductible_input: 4800
  net_payable: 19200
```

```oa-check
name: Iceland qualifying reduced-rate room and zero-rated export
inputs:
  room_net: 50000
  export_net: 250000
  export_supported_input: 4800
steps:
  - room_output: room_net * 0.11
  - export_output: export_net * 0
  - export_net_payable: export_output - export_supported_input
expected:
  room_output: 5500
  export_output: 0
  export_net_payable: -4800
```

```oa-check
name: Iceland foreign service, confirmed blocked purpose
inputs:
  foreign_service_net: 50000
  allowed_input: 0
steps:
  - buyer_vat: foreign_service_net * 0.24
  - liability: buyer_vat - allowed_input
expected:
  buyer_vat: 12000
  liability: 12000
```

The statutory non-registered-buyer threshold is 10,000 or more, with VAT on the whole qualifying consideration. The following block assumes that exact boundary has already been met; it does not replace the purchaser/status/service tests.

```oa-check
name: Iceland qualifying foreign advertising at exact threshold
inputs:
  period_net_consideration: 10000
steps:
  - vat_on_whole_consideration: period_net_consideration * 0.24
expected:
  vat_on_whole_consideration: 2400
```

```oa-check
name: Iceland listed fuel, July and September 2026
inputs:
  july_net_sale: 100000
  september_net_sale: 100000
steps:
  - july_output: july_net_sale * 0.11
  - september_output: september_net_sale * 0.24
  - combined_output: july_output + september_output
expected:
  july_output: 11000
  september_output: 24000
  combined_output: 35000
```

### Mixed-activity annual reconciliation

Assume an ordinary taxpayer outside the Article 10 exempt-body override, taxable turnover 12 million and exempt turnover 8 million, excluding a separate 2 million operating-asset sale from the ratio. Supported direct taxable input VAT is 120,000, direct exempt VAT 48,000, genuinely shared VAT 240,000 and separately blocked VAT 24,000. The annual ratio is **60%** and total allowable input is **264,000**. If provisional deductions already claimed in earlier periods total 280,000 and there are no other annual inputs, the final-period reconciliation reverses **16,000**. Map the reconciliation to the current form rather than inventing a delta box. [Regulation 192/1993, Articles 2–5](https://files.reglugerd.is/pdf/0192-1993/current)

```oa-check
name: Iceland mixed VAT direct attribution and annual shared-cost reconciliation
inputs:
  taxable_turnover: 12000000
  exempt_turnover: 8000000
  operating_asset_sale_excluded_from_ratio: 2000000
  direct_taxable_vat: 120000
  direct_exempt_vat: 48000
  shared_vat: 240000
  blocked_vat: 24000
  earlier_provisional_claims: 280000
steps:
  - annual_ratio: taxable_turnover / (taxable_turnover + exempt_turnover)
  - shared_deduction: shared_vat * annual_ratio
  - direct_exempt_deduction: direct_exempt_vat * 0
  - blocked_deduction: blocked_vat * 0
  - annual_allowed: direct_taxable_vat + shared_deduction + direct_exempt_deduction + blocked_deduction
  - final_period_reconciliation: annual_allowed - earlier_provisional_claims
expected:
  annual_ratio: 0.60
  shared_deduction: 144000
  annual_allowed: 264000
  final_period_reconciliation: -16000
```

### Partly creditable foreign service

Assume an ordinary shared foreign consultancy service with VAT-exclusive consideration 100,000, applicable rate 24%, an established **60%** deductible share under the above method, and no import-of-goods override or seller Icelandic registration. Article 35 purchaser liability applies to the 40% non-deductible part: **9,600**. Do not also deduct that amount as ordinary input VAT. The supported split and Article 35 eligibility must precede this calculation. [VAT Act, Article 35](https://www.althingi.is/lagas/nuna/1988050.html), [Regulation 192/1993, Article 5](https://files.reglugerd.is/pdf/0192-1993/current)

```oa-check
name: Iceland foreign service purchaser liability for an established exempt share
inputs:
  foreign_service_net: 100000
  rate: 0.24
  established_deductible_share: 0.60
steps:
  - nondeductible_share: 1 - established_deductible_share
  - buyer_liability: foreign_service_net * rate * nondeductible_share
expected:
  nondeductible_share: 0.40
  buyer_liability: 9600
```

### Private use is a separate test

An otherwise eligible purchase carries VAT 120,000. Evidence establishes 75% taxable-business use and 25% private use, without a category-specific block. Deduct **90,000**, under the actual-use test rather than an assumed turnover ratio. [Regulation 192/1993, Article 6](https://files.reglugerd.is/pdf/0192-1993/current)

```oa-check
name: Iceland VAT private-use attribution on otherwise eligible input
inputs:
  input_vat: 120000
  evidenced_taxable_business_share: 0.75
steps:
  - deductible: input_vat * evidenced_taxable_business_share
  - nondeductible: input_vat - deductible
expected:
  deductible: 90000
  nondeductible: 30000
```

### Movable asset changes wholly to non-creditable use

Assume a qualifying movable asset acquired in 2024 with original deductible VAT 240,000, full original credit, and a full change to non-creditable use in 2026, with no Article 12 exception. Established construction-index values for the relevant period ends are 100 and 120. The indexed VAT is **288,000**; the second-following-calendar-year remaining share is 60%, so clawback is **172,800**. The index inputs are hypothetical, not published index figures. This is a full change-of-use case, not the distinct annual ratio-change computation. [Regulation 192/1993, Articles 12 and 14](https://files.reglugerd.is/pdf/0192-1993/current)

```oa-check
name: Iceland movable capital input full change of use, indexed remaining share
inputs:
  original_deductible_vat: 240000
  original_index: 100
  adjustment_index: 120
  established_remaining_share: 0.60
steps:
  - indexed_vat: original_deductible_vat * adjustment_index / original_index
  - clawback: indexed_vat * established_remaining_share
expected:
  indexed_vat: 288000
  clawback: 172800
```

## Ask the client first

- What do the Icelandic VAT registration record and current settlement period say? Has the business ever been removed from the VAT register and re-registered?
- What invoice, supplier/customer status, business use and rate/exemption facts support each transaction?
- Are imports, foreign services, VOES, mixed exempt activity, property, vehicles or a correction involved?
- Has a statement already been filed or an assessment/penalty notice been issued?

## When to refuse or refer

- Registration, rate, exemption, place, Customs or input-VAT evidence is missing.
- VOES eligibility, a special scheme, property/vehicle legal classification or an attribution/adjustment input is unresolved. The ordinary mixed-activity method above requires source documents and a supported allocation.
- A required invoice, vendor-registration check, Customs document, prior statement or assessment notice is unavailable.
- The business was re-registered after removal, or is under the bankruptcy-linked monthly regime, and the settlement period on the registration record is not available.

### Stop conditions

Use a separate sourced method or professional review for disputed mixed-use attribution, voluntary real-property registration, imported goods/customs valuation and import-VAT deferral, VOES eligibility, foreign representative arrangements, special investment/fishing schemes, vehicle-resale margin rules, a missing VAT invoice, a supplier that was not registered, and an estimated assessment or appeal. The method above includes ordinary direct/shared attribution, annual reconciliation and the stated capital-adjustment rules, alongside confirmed domestic taxable rates, zero-rated evidence (including services to foreign businesses under current Article 12), exempt outputs, supported input VAT, invoice controls, the Article 35 foreign-service purchaser route, refunds of excess input VAT, corrections before assessment and the ordinary return timetable.

Original editorial source record: [Skatturinn: Value Added Tax](https://www.skatturinn.is/english/companies/value-added-tax/); [VAT Act No. 50/1988, current consolidated text](https://www.althingi.is/lagas/nuna/1988050.html); [RSK 10.24 foreign-service purchase report](https://www.skatturinn.is/media/rsk10/rsk_1024.is.pdf); [Skatturinn VAT-register guidance](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/virdisaukaskattsskra/). Source snapshots, evidence ledger and cases are retained in the controlled editorial packet.

<!-- openaccountants-cta-block -->

## Talk to an accountant

For advice on your facts, [contact OpenAccountants](https://www.openaccountants.com/contact).

## Sources

The following primary sources were accessed on 23 October 2026. This pass checked the current rate provisions, foreign-service boundary, campground wording, mixed input attribution/capital adjustments and example inputs; it does not attest to all remaining scope or operational questions. The earlier September research record above is preserved.

| Official source | Read on |
| --- | --- |
| [VAT Act 50/1988, current 1 October 2026 compilation](https://www.althingi.is/lagas/nuna/1988050.html) | 2026-10-23 |
| [VAT administrative guidance](https://www.skatturinn.is/english/companies/value-added-tax/) | 2026-10-23 |
| [Registration, periods and corrections](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/virdisaukaskattsskra/) | 2026-10-23 |
| [RSK 10.24 foreign-service report](https://www.skatturinn.is/media/rsk10/rsk_1024.is.pdf) | 2026-10-23 |
| [Input VAT Regulation 192/1993, Articles 2–16, current PDF](https://files.reglugerd.is/pdf/0192-1993/current) | 2026-10-23 |
| [Skatturinn, VAT overview and mixed activity](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/almennt-um-vsk/) | 2026-10-23 |
