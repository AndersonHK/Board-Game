# FedEx Printing Plan

Research date: 2026-04-26

This plan is for producing the current Edition 0 physical prototype at FedEx Office using US letter-size color prints.

## Short Answer

FedEx Office can print the prototype assets as letter-size color documents. The supported path is `Copies & Custom Documents`, using `8.5 in x 11 in`, `Full Color`, `Single-Sided`, and a selected paper stock.

FedEx's own pages confirm:

- `Copies & Custom Documents` supports `8.5 in x 11 in`, full-color printing, single- or double-sided printing, and multiple paper types.
- Available paper options shown for this product include `Laser (24 lb.)`, `Laser (32 lb.)`, `Laser Recycled (28 lb.)`, `30% Recycled (20 lb.)`, `Laser (60 lb.)`, `Laser (80 lb.)`, `Gloss Text (32 lb.)`, `Matte Cover (100 lb.)`, `Water Resistant (7.7 Mil)`, and several color papers.
- FedEx supports double-sided custom documents by uploading a 2-page PDF or separate front/back files and assigning the first file/page as front and second as back.
- FedEx offers cutting as a finishing option for `Copies & Custom Documents`, with half, thirds, and quarter cuts listed publicly.
- FedEx accepts PDF as the preferred print format and also accepts common image formats including PNG and JPG.
- FedEx recommends 300 DPI for most prints.
- `Copies & Custom Documents` are not full-bleed; they print with a small margin.

Sources:

- FedEx Office Copies & Custom Documents: https://www.office.fedex.com/copies.html
- FedEx Office document printing overview: https://www.office.fedex.com/default/document-printing
- FedEx Office FAQ: https://www.office.fedex.com/default/faq.html
- FedEx Office self-service copy and print overview: https://www.office.fedex.com/default/copy-and-print-services

## Current FedEx Price Notes

FedEx's official pages publish product starting prices, but not a full per-paper, per-page public price table for every local store and stock. The official document printing page lists:

- `Copies & Custom Documents`: starting at `$0.24 each`
- `Certificates`: starting at `$0.71 each`, `8.5 in x 11 in`, full color
- `Letterhead`: starting at `$0.70 each`, `8.5 in x 11 in`, full color

For practical budget planning, use the following working estimate until the actual order is uploaded and quoted by the selected store:

| Print Type | Working Color Cost | Confidence | Notes |
| --- | ---: | --- | --- |
| Letter color, standard paper | `$0.71-$0.89/page` | Medium | Current 2026 third-party price guides cluster around this range; FedEx's official full-color letter products start around `$0.70-$0.71`. |
| Letter color, heavier/premium stock | `+$0.10-$0.50/page` | Low-medium | Paper-stock premiums vary by store and stock. Confirm in the FedEx cart or by phone. |
| Letter color on `Matte Cover (100 lb.)` | about `$0.81-$1.39/page` | Low | Best planning range for card sheets; must be confirmed during upload because FedEx does not publish this exact table publicly. |
| Letter color, double-sided | about `$1.00-$1.10/sheet` standard paper | Low-medium | Useful if testing backs, but duplex alignment should be proofed before printing the full set. |
| Letter color, double-sided on heavier/premium stock | about `$1.10-$1.60/sheet` | Low | Working estimate for front/back card sheets. FedEx does not publish the exact `Matte Cover (100 lb.)` duplex price table publicly. |

Supplemental pricing source used only for estimation: https://cheapfastprinting.com/news/fedex-kinkos-color-printing-cost-guide/

## Local Asset Quality

The generated prototype assets already match FedEx's recommended print quality closely enough. Do not upsample beyond the current files.

| Asset Group | Current Pixels | Intended Physical Size | Effective Resolution |
| --- | ---: | ---: | ---: |
| Card atlas sheets | `2448 x 3168 px` | `8.5 x 11 in` | `288 DPI` |
| Board pages | `2448 x 3168 px` | `8.5 x 11 in` | `288 DPI` |
| Full board image | `7344 x 3168 px` | `25.5 x 11 in` | `288 DPI` |
| Quick-start guide pages | `2448 x 3168 px` | `8.5 x 11 in` | `288 DPI` |
| Standard card fronts/backs | `612 x 1056 px` | `2.125 x 3.6667 in` | `288 DPI` |
| Quest reference card | `1224 x 2112 px` | `4.25 x 7.3334 in` | `288 DPI` |
| Class reference cards | `1224 x 1056 px` | `4.25 x 3.6667 in` | `288 DPI` |

The PNG metadata currently reports `96 DPI`, but the actual pixel dimensions are correct for `288 DPI` at the intended printed sizes. The print order should therefore use exact page sizing and `100%` scale, not metadata-based auto-sizing.

## Recommended FedEx Order Setup

### Card Atlases

- Product: `Copies & Custom Documents`
- Print color: `Full Color`
- Paper size: `8.5 in x 11 in`
- Sides: `Double-Sided` for the duplex card job, or `Single-Sided` when using the front PNG atlases only
- Paper: `Matte Cover (100 lb.)`
- Fallback paper: `Laser (80 lb.)`
- File format: combined PDF preferred, using one `8.5 x 11 in` page per atlas side
- Scale: `100%`
- Quantity: `1` of each atlas sheet

Files:

- Duplex print document: `assets/generated/print/card-atlases-duplex.pdf`
- `assets/generated/atlases/fronts/ATLAS-REF-01.png`
- `assets/generated/atlases/fronts/ATLAS-REF-02.png`
- `assets/generated/atlases/fronts/ATLAS-ENC-01.png`
- `assets/generated/atlases/fronts/ATLAS-RES-01.png` through `ATLAS-RES-06.png`
- `assets/generated/atlases/fronts/ATLAS-CRE-01.png` through `ATLAS-CRE-07.png`
- `assets/generated/atlases/backs/ATLAS-REF-01.png`
- `assets/generated/atlases/backs/ATLAS-REF-02.png`
- `assets/generated/atlases/backs/ATLAS-ENC-01.png`
- `assets/generated/atlases/backs/ATLAS-RES-01.png` through `ATLAS-RES-06.png`
- `assets/generated/atlases/backs/ATLAS-CRE-01.png` through `ATLAS-CRE-07.png`

Count: `16` letter-size card-atlas sheets.

Keep the PNG atlases for design inspection and single-sheet proofs. Use the duplex PDF for the full double-sided card print job; its back pages are horizontally mirrored for portrait long-edge duplex printing. Print one duplex test sheet first because small front/back alignment errors matter after cutting.

### Card Backs

FedEx can print backs through the same `Copies & Custom Documents` product by selecting `Double-Sided`. Their FAQ says PDFs can be uploaded as a 2-page PDF, or images/PDFs can be uploaded as separate front and back files.

Card backs are not expected to be the same price as single-sided fronts. FedEx treats double-sided printing as a different side option, and available public pricing examples show double-sided color costing more than single-sided color, though usually less than buying two separate single-sided sheets.

Recommended first-pass approach:

1. Print one duplex proof using the `ATLAS-ENC-01` front/back page pair from `assets/generated/print/card-atlases-duplex.pdf`.
2. Use `Matte Cover (100 lb.)` if available for duplex. If the store cannot duplex that stock reliably, use single-sided fronts with opaque sleeves.
3. Confirm long-edge vs short-edge flip direction before printing the remaining decks.
4. Check front/back alignment after cutting one card.

Budget options:

| Backing Method | Added / Changed Cost For 16 Card Sheets | Estimate | Notes |
| --- | ---: | ---: | --- |
| Fronts only | baseline | `$12.96-$22.24` | Current card-atlas budget. |
| Duplex backs on same sheets | adds roughly `$4.64-$11.36` over fronts-only | `$17.60-$25.60` total card sheets | Best cost if alignment is acceptable. Based on double-sided color plus premium-stock estimates. |
| Separate one-sided back sheets | adds another 16 color card-stock sheets | `+$12.96-$22.24` | More forgiving for sleeves or manual backing, but doubles card-sheet print count. |

Question for the store: "For 16 letter-size sheets on `Matte Cover (100 lb.)`, full color, double-sided, what is the per-sheet price, and can you duplex-align a 4-by-3 card grid closely enough for cutting?"

### Board Pages

- Product: `Copies & Custom Documents`
- Print color: `Full Color`
- Paper size: `8.5 in x 11 in`
- Sides: `Single-Sided`
- Paper: `Laser (32 lb.)`, `Laser (60 lb.)`, or `Laser (80 lb.)`
- Scale: `100%`

Files:

- `assets/generated/board/BOARD-PAGE-01-left.png`
- `assets/generated/board/BOARD-PAGE-02-center.png`
- `assets/generated/board/BOARD-PAGE-03-right.png`

Count: `3` letter-size board sheets.

### Quick-Start Guide

- Product: `Copies & Custom Documents`
- Print color: `Full Color`
- Paper size: `8.5 in x 11 in`
- Sides: `Single-Sided` for easy table reference, or `Double-Sided` if compactness matters
- Paper: `Laser (24 lb.)` or `Laser (32 lb.)`
- File format: `assets/generated/guide/quick-start-guide.pdf`
- Scale: `100%`

Current generated count: `10` letter-size pages.

## Cutting Plan

FedEx publicly lists cutting as a `Copies & Custom Documents` finishing option. Their listed standard cuts are:

- half cut, vertical or horizontal
- thirds cut, vertical or horizontal
- quarter cut

That is promising for this prototype because the card atlases use a `4 x 3` letter-sheet grid:

- vertical quarter cuts at `2.125 in`, `4.25 in`, and `6.375 in`
- horizontal third cuts at `3.6667 in` and `7.3333 in`

Do not assume self-service staff will cut arbitrary sheets for free. Treat cutting as a full-service finishing request and get it quoted with the order. FedEx says full-service printing includes team-member support for custom print projects, but their FAQ also notes that in-store prices may vary and additional fees can apply.

Practical expectation:

- A full-service FedEx Office location should have proper paper-cutting equipment because cutting is a listed finishing option.
- The publicly listed options match the atlas grid closely enough to ask for machine cutting instead of scissors.
- The online menu may not expose a single "4 columns by 3 rows" option, so call or ask at the counter before printing the full deck.
- Self-service is mainly for printing; if you want the clerk to cut, order through full-service or add finishing.

Question for the store: "Can you cut 16 letter-size card-stock sheets into a 4-by-3 grid, using quarter cuts vertically and thirds horizontally? What is the cutting charge, and can you keep each sheet's cards bundled by sheet?"

## Working Budget

Front-only prototype, using current generated counts and no cutting:

| Component | Pages | Paper Assumption | Estimate |
| --- | ---: | --- | ---: |
| Card atlases | `16` | Color on `Matte Cover (100 lb.)` | `$12.96-$22.24` |
| Board pages | `3` | Color on standard/premium text paper | `$2.13-$4.17` |
| Quick-start guide | `10` | Color on standard text paper | `$7.10-$8.90` |
| Total before tax/fees | `29` | No finishing | `$22.19-$35.31` |

Possible additions:

| Addition | Estimate | Notes |
| --- | ---: | --- |
| Duplex card backs | `+$4.64-$11.36` | Increment over front-only card sheets if FedEx can duplex the selected card stock. |
| Separate one-sided back sheets | `+$12.96-$22.24` | If printed as separate sheets instead of duplex. |
| Cutting / trimming | Store quote needed | FedEx lists cutting, but does not publish a universal cutting price for this job. |

## Print Settings To Ask For

- `100%` scale / actual size.
- No fit-to-page.
- No automatic enlargement.
- No borderless expectation; FedEx custom documents include a small margin.
- Keep page orientation portrait.
- Use `PDF` when possible so page size stays fixed.
- Use `288-300 DPI`; do not request higher resolution.
- Export CMYK only if the tool can do it without resampling or changing layout. Otherwise, use the current RGB assets and order a proof sheet.

## Proof Sheet

Before the full print:

1. Print `ATLAS-REF-01` on the intended card stock.
2. Confirm the `4 x 3` card grid still measures `8.5 x 11 in` overall at the cut boundaries.
3. Cut one standard card and check that it measures `2.125 x 3.6667 in`.
4. Check rules text on the smallest cards under normal classroom lighting.
5. If printing backs, run one duplex proof and check flip direction and alignment before printing all decks.
6. Ask FedEx to cut the proof sheet before the full job if using their cutting service.

## Known Risks

- FedEx pricing varies by store, and exact paper-stock costs may only appear after upload/customization.
- Self-service printing may be limited to standard paper; heavier approved paper may need counter help.
- FedEx custom documents are not full-bleed, so any edge-critical art needs internal safe margins.
- Double-sided card backs are technically supported, but duplex alignment may not be good enough for small cards without a proof.
- Cutting is officially listed, but the exact `4 x 3` card grid and cutting fee should be confirmed with the local store before placing the whole order.
- The generated PNG files are physically correct, but their embedded `96 DPI` metadata can confuse upload tools if they infer size from metadata instead of page dimensions. Prefer PDF wrappers or verify `8.5 x 11 in` after upload.
