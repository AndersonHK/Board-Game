# Repository Directory

This file is the canonical map of the repository structure and the purpose of important files and folders. Long-term project context lives in [project-memory.md](./project-memory.md). Repo-wide Codex instructions live in [../CODEX.md](../CODEX.md). The user-facing entry point remains [../README.md](../README.md).

## Fast Paths

- General design or rules context: start with [../CODEX.md](../CODEX.md), [../README.md](../README.md), [project-memory.md](./project-memory.md), and this file.
- Printed-materials-only playtest: start from [../assets/printed-materials-index.md](../assets/printed-materials-index.md) and defer non-printed design context until after the run.
- Card data work: read [../defines/cards/README.md](../defines/cards/README.md), then the relevant deck README, deck `TEMPLATE.txt`, and `cards/` folder.
- Print pipeline work: start with [../assets/README.md](../assets/README.md), then [../assets/card-atlas-definition.md](../assets/card-atlas-definition.md), [../assets/board-layout-definition.md](../assets/board-layout-definition.md), and the relevant script in [../assets/scripts](../assets/scripts/).
- Playtest evidence review: use [../temp/playtests](../temp/playtests/) as evidence only; promotion into [../defines](../defines/README.md) still requires explicit user approval.

## Current Structure

```text
/
|-- assets/
|   |-- card-art/
|   |   |-- archive/
|   |   |   `-- portrait-reference/<deck-slug>/<card-art>.png
|   |   |-- final/
|   |   |   `-- <deck-slug>/<card-id>.png
|   |   |-- incoming/
|   |   |   `-- GROUP-*/<card-id>.source.png and review contact sheets
|   |   |-- session-groups/
|   |   |   `-- GROUP-*.md generation batches by deck/story group
|   |   |-- AI_ART_HANDOFF.md
|   |   `-- AI_ART_SESSION_GROUPS.md
|   |-- board-layout-definition.md
|   |-- card-atlas-definition.md
|   |-- card-text-fit-report.md
|   |-- fedex-printing-plan.md
|   |-- generated/
|   |   |-- atlases/
|   |   |   |-- fronts/ATLAS-*.png
|   |   |   `-- backs/ATLAS-*.png
|   |   |-- board/
|   |   |   `-- table-board-full.png and BOARD-PAGE-0*.png
|   |   |-- card-backs/
|   |   |   `-- <back-style>.png
|   |   |-- card-frames/
|   |   |   `-- <layout>.png plus common/rare variants
|   |   |-- card-fronts/
|   |   |   `-- <deck-slug>/<card-id>.png
|   |   |-- guide/
|   |   |   `-- quick-start-guide.pdf
|   |   `-- print/
|   |       `-- complete/split atlas PDFs and table-board-pages.pdf
|   |-- printed-materials-index.md
|   |-- print-and-bundle-package.md
|   |-- scripts/
|   |   |-- build_card_atlases.py
|   |   |-- build_duplex_card_atlas_pdf.py
|   |   |-- calculate_card_layout.py
|   |   |-- card_rendering_common.py
|   |   |-- check_card_art_integrity.py
|   |   |-- check_card_text_fit.py
|   |   |-- generate_card_backs.py
|   |   |-- generate_card_frames.py
|   |   |-- generate_printable_cards.py
|   |   |-- generate_quick_start_guide.py
|   |   |-- generate_table_board.py
|   |   `-- print_pdf_common.py
|   |-- widget-and-token-definitions.md
|   `-- README.md
|-- CODEX.md
|-- defines/
|   |-- card-layout.md
|   |-- cards/
|   |   |-- agenda-deck/
|   |   |   |-- TEMPLATE.txt
|   |   |   |-- README.md
|   |   |   `-- cards/<agenda-id>.txt
|   |   |-- creature-deck/
|   |   |   |-- TEMPLATE.txt
|   |   |   |-- README.md
|   |   |   `-- cards/<enemy-boss-artifact-summon-id>.txt
|   |   |-- encounter-deck/
|   |   |   |-- TEMPLATE.txt
|   |   |   |-- README.md
|   |   |   `-- cards/<encounter-or-ordeal-id>.txt
|   |   |-- quest-deck/
|   |   |   |-- TEMPLATE.txt
|   |   |   |-- README.md
|   |   |   `-- cards/<quest-id>.txt
|   |   |-- resource-deck/
|   |   |   |-- TEMPLATE.txt
|   |   |   |-- README.md
|   |   |   `-- cards/<resource-action-id>.txt
|   |   `-- README.md
|   |-- core-rules.md
|   |-- creature-deck.md
|   `-- README.md
|-- README.md
|-- temp/
|   `-- playtests/
|       |-- 2026-04-26-printed-only-3p-sim/
|       |   `-- README/setup, playtest log, temporary rulings, findings/deferred comparison
|       |-- 2026-04-26-printed-package-3p-sealed-sim/
|       |   `-- 00 package/setup, 01 session log, 02 package findings, 03 doc comparison
|       |-- quest-001-standard-10-round/
|       |   `-- 00 source map, 01 quest frame, 02 roster, 03 agendas, 04 resource pool, 05 encounters, 06 log, 07 rulings, 08 findings
|       |-- quest-002-event-driven-10-round/
|       |   `-- 00 source map, 01 quest frame, 02 roster, 03 agendas, 04 action pool, 05 events, 06 entities, 07 log, 08 rulings, 09 findings
|       |-- quest-003-canon-stress-test-10-round/
|       |   `-- 00 source map, 01 quest frame, 02 roster, 03 agendas, 04 action pool, 05 events, 06 entities, 07 log, 08 rulings, 09 findings
|       |-- quest-004-quickstart-4p-sim/
|       |   `-- 00 source map, 01 quest frame, 02 roster, 03 agendas, 04 action pool, 05 events, 06 entities, 07 log, 08 rulings, 09 findings
|       |-- quest-005-canon-cards-3p-sim/
|       |   `-- 00 source map, 01 quest frame, 02 roster, 03 agendas, 04 resource deck, 05 encounter deck, 06 creature deck, 07 log, 08 rulings, 09 findings
|       |-- quest-005-finite-deck-4p-sim/
|       |   `-- 00 source map, 01 quest frame, 02 roster, 03 agendas, 04 resource deck, 05 encounter deck, 06 creature deck, 07 log, 08 rulings, 09 findings
|       |-- quest-006-quickstart-3p-relics-and-claims-sim/
|       |   `-- 00 source map, 01 quest frame, 02 roster, 03 agendas, 04 resource deck, 05 encounter deck, 06 creature deck, 07 log, 08 rulings, 09 findings
|       `-- quest-007-quickstart-3p-hazard-trader-finale-sim/
|           `-- 00 source map, 01 quest frame, 02 roster, 03 agendas, 04 resource deck, 05 encounter deck, 06 creature deck, 07 log, 08 rulings, 09 findings
`-- docs/
    |-- design/
    |   |-- card-economy-and-rarity.md
    |   |-- class-archetypes.md
    |   |-- core-concept.md
    |   |-- deck-architecture.md
    |   `-- round-structure.md
    |-- project-memory.md
    |-- quick-start-guide.md
    |-- research/
    |   |-- betrayal-at-house-on-the-hill.md
    |   |-- civilization-traits-and-unique-abilities.md
    |   |-- hearts-of-iron-iv-world-tension.md
    |   |-- hearthstone-hero-powers.md
    |   |-- research-index.md
    |   |-- secret-objectives-risk-ticket-to-ride.md
    |   |-- stellaris-crises.md
    |   `-- yugioh-tribute-and-mtg-discard-costs.md
    `-- repository-directory.md
```

## File Guide

- [../assets/README.md](../assets/README.md): notes for the canonical art and print-asset folder.
- [../assets/card-art/AI_ART_HANDOFF.md](../assets/card-art/AI_ART_HANDOFF.md): generated art checklist listing card IDs, prompts, and final destination paths.
- [../assets/card-art/AI_ART_SESSION_GROUPS.md](../assets/card-art/AI_ART_SESSION_GROUPS.md): grouped AI-art generation session plan.
- [../assets/board-layout-definition.md](../assets/board-layout-definition.md): generated three-page table-board layout, page assembly order, and board footprint rationale.
- [../assets/card-atlas-definition.md](../assets/card-atlas-definition.md): Edition 0 card atlas plan for letter-size printing and cutting, including the exact card grid, cut marks, sheet IDs, and per-sheet card assignments.
- [../assets/card-text-fit-report.md](../assets/card-text-fit-report.md): generated report checking all current card definitions against the standard layout.
- [../assets/fedex-printing-plan.md](../assets/fedex-printing-plan.md): FedEx-oriented print setup, proofing notes, and current atlas PDF filenames.
- [../assets/generated/](../assets/generated/): reproducible PNG and PDF outputs from the rendering pipeline, including card fronts, frames, backs, atlases, board pages, quick-start guide, and print PDFs.
- [../assets/printed-materials-index.md](../assets/printed-materials-index.md): exact read list for printed-materials-only playtests and a list of non-printed docs to defer until after the run.
- [../assets/print-and-bundle-package.md](../assets/print-and-bundle-package.md): Edition 0 physical production manifest covering cards, rules sheets, board widgets, tokens, dice, bundling groups, and remaining playability gaps.
- [../assets/scripts/build_card_atlases.py](../assets/scripts/build_card_atlases.py): script that merges rendered card fronts and generated backs into printable atlas PNGs according to [../assets/card-atlas-definition.md](../assets/card-atlas-definition.md).
- [../assets/scripts/build_duplex_card_atlas_pdf.py](../assets/scripts/build_duplex_card_atlas_pdf.py): script that builds the complete duplex atlas PDF plus two email-sized split PDFs; backs are unmirrored by default, with `--mirror-backs` preserving the old pre-flipped workflow.
- [../assets/scripts/calculate_card_layout.py](../assets/scripts/calculate_card_layout.py): script that derives [../defines/card-layout.md](../defines/card-layout.md) from the card atlas size.
- [../assets/scripts/card_rendering_common.py](../assets/scripts/card_rendering_common.py): shared card parser, layout loader, font helpers, and drawing utilities for the PNG card pipeline.
- [../assets/scripts/check_card_art_integrity.py](../assets/scripts/check_card_art_integrity.py): script that scans final card art for exact and near-duplicate images.
- [../assets/scripts/check_card_text_fit.py](../assets/scripts/check_card_text_fit.py): script that checks card `.txt` files against [../defines/card-layout.md](../defines/card-layout.md).
- [../assets/scripts/generate_card_backs.py](../assets/scripts/generate_card_backs.py): script that creates generated card-back texture PNGs.
- [../assets/scripts/generate_card_frames.py](../assets/scripts/generate_card_frames.py): script that creates reusable deck-specific frame PNGs.
- [../assets/scripts/generate_printable_cards.py](../assets/scripts/generate_printable_cards.py): script that renders individual printable card-front PNGs and refreshes the AI art handoff.
- [../assets/scripts/generate_quick_start_guide.py](../assets/scripts/generate_quick_start_guide.py): script that renders [quick-start-guide.md](./quick-start-guide.md) as the generated guide PDF.
- [../assets/scripts/generate_table_board.py](../assets/scripts/generate_table_board.py): script that renders the full table-board PNG, three printable board page slices, and `assets/generated/print/table-board-pages.pdf`.
- [../assets/scripts/print_pdf_common.py](../assets/scripts/print_pdf_common.py): shared multipage-PDF writer used by the atlas and board print generators.
- [../assets/widget-and-token-definitions.md](../assets/widget-and-token-definitions.md): player-facing definitions for printed widgets, dice, tokens, table-board rectangles, and open widget production gaps.
- [../defines/card-layout.md](../defines/card-layout.md): generated standard Edition 0 card-front layout and machine-readable layout spec.
- [../CODEX.md](../CODEX.md): root operating instructions for Codex, including how to maintain project documentation.
- [../defines/README.md](../defines/README.md): index for canonical numeric and rules-define files.
- [../defines/cards/README.md](../defines/cards/README.md): canonical card-data format, folder layout, and template usage for the first printable vertical slice.
- [../defines/core-rules.md](../defines/core-rules.md): canonical baseline hand rules, round flow, and escalation timing.
- [../defines/creature-deck.md](../defines/creature-deck.md): canonical creature deck definition and its scene-spawn role.
- [../defines/cards/quest-deck/](../defines/cards/quest-deck/): the canonical quest-card template and current quest definitions.
- [../defines/cards/encounter-deck/](../defines/cards/encounter-deck/): the canonical encounter-card template plus random encounters and scripted ordeals.
- [../defines/cards/resource-deck/](../defines/cards/resource-deck/): the canonical resource-card template and the first-pass vertical-slice resource list.
- [../defines/cards/creature-deck/](../defines/cards/creature-deck/): the canonical shared entity-card template for enemies, bosses, artifacts, enchantments, and summons.
- [../defines/cards/agenda-deck/](../defines/cards/agenda-deck/): the canonical agenda-card template and current secret agendas.
- [../README.md](../README.md): lightweight project overview and pointer hub for the repository.
- [design/card-economy-and-rarity.md](./design/card-economy-and-rarity.md): draft cost philosophy, shared rarity direction, and current canonization questions around hand size, kill rewards, and expensive card play.
- [design/core-concept.md](./design/core-concept.md): evolving design brief, current concept framing, and system-level implications.
- [design/class-archetypes.md](./design/class-archetypes.md): stable mechanical class identities, player personas, and ability design notes.
- [design/deck-architecture.md](./design/deck-architecture.md): current definition of the four deck systems and how each one shapes play.
- [design/round-structure.md](./design/round-structure.md): current round order, escalation flow, and timing assumptions.
- [project-memory.md](./project-memory.md): long-term project memory, including goals, constraints, principles, decisions, and open questions.
- [quick-start-guide.md](./quick-start-guide.md): current player-facing fantasy rules sheet and the baseline teaching document for future simulations.
- [research/research-index.md](./research/research-index.md): index of topic research notes and their design relevance.
- [research/betrayal-at-house-on-the-hill.md](./research/betrayal-at-house-on-the-hill.md): notes on modular exploration, phase shift, and traitor-reveal structure.
- [research/hearts-of-iron-iv-world-tension.md](./research/hearts-of-iron-iv-world-tension.md): notes on shared escalation tracks and threshold-based unlocking.
- [research/hearthstone-hero-powers.md](./research/hearthstone-hero-powers.md): notes on compact, repeatable hero asymmetry.
- [research/civilization-traits-and-unique-abilities.md](./research/civilization-traits-and-unique-abilities.md): notes on small rule changes with compounding strategic impact.
- [research/stellaris-crises.md](./research/stellaris-crises.md): notes on midgame and endgame crisis structure for escalation milestones.
- [research/secret-objectives-risk-ticket-to-ride.md](./research/secret-objectives-risk-ticket-to-ride.md): notes on hidden objectives, secrecy, and endgame scoring tension.
- [research/yugioh-tribute-and-mtg-discard-costs.md](./research/yugioh-tribute-and-mtg-discard-costs.md): research on tribute-style commitment costs and discard-balancing lessons to guide the planned discard-and-sacrifice economy.
- [repository-directory.md](./repository-directory.md): this file; the current repository map and documentation conventions.
- [../temp/playtests/quest-001-standard-10-round/](../temp/playtests/quest-001-standard-10-round/): temporary first-pass simulation package for a 10-round fantasy quest, including source extraction, mock content, a full roleplayed run, live rulings, and recommendations.
- [../temp/playtests/quest-002-event-driven-10-round/](../temp/playtests/quest-002-event-driven-10-round/): temporary second-pass simulation package built around scene events, spawned entities, non-combat pacing, and stronger relationship drama.
- [../temp/playtests/quest-003-canon-stress-test-10-round/](../temp/playtests/quest-003-canon-stress-test-10-round/): temporary third-pass simulation package focused on stress-testing recently canonized `defines/` rules, creature-deck order, multi-round encounter flow, and escalation-10 behavior.
- [../temp/playtests/quest-004-quickstart-4p-sim/](../temp/playtests/quest-004-quickstart-4p-sim/): temporary fourth-pass simulation package focused on quick-start teachability, four-player class selection, and how much of the game a real table can run from visible materials alone.
- [../temp/playtests/quest-005-canon-cards-3p-sim/](../temp/playtests/quest-005-canon-cards-3p-sim/): temporary simulation package using current canonical card definitions.
- [../temp/playtests/quest-005-finite-deck-4p-sim/](../temp/playtests/quest-005-finite-deck-4p-sim/): temporary finite-deck simulation package.
- [../temp/playtests/quest-006-quickstart-3p-relics-and-claims-sim/](../temp/playtests/quest-006-quickstart-3p-relics-and-claims-sim/): temporary quick-start simulation focused on relics and claiming.
- [../temp/playtests/quest-007-quickstart-3p-hazard-trader-finale-sim/](../temp/playtests/quest-007-quickstart-3p-hazard-trader-finale-sim/): temporary quick-start simulation focused on hazards, trader flow, and finale pressure.
- [../temp/playtests/2026-04-26-printed-only-3p-sim/](../temp/playtests/2026-04-26-printed-only-3p-sim/): temporary printed-materials-only simulation package.
- [../temp/playtests/2026-04-26-printed-package-3p-sealed-sim/](../temp/playtests/2026-04-26-printed-package-3p-sealed-sim/): temporary sealed printed-package simulation package.

## Documentation Conventions

1. Use markdown links when referring to canonical docs, relevant files, or important folders.
2. Keep this file updated when major files or folders are added.
3. Keep [project-memory.md](./project-memory.md) updated when the project's durable understanding changes.
4. Keep [../README.md](../README.md) concise and oriented toward human navigation.
5. Keep [../CODEX.md](../CODEX.md) as the standing instruction set for Codex behavior in this repo.
6. Treat playtest packages as evidence, not canon. Promotion into [../defines](../defines/README.md) requires explicit user approval.

## Planned Growth

Likely future growth areas:

- more design documents for rules, mechanics, and components
- more final art references and generated assets
- revised printable production files after proofing
- playtest notes and iteration logs

When those folders or files are created, add them here with a short purpose statement and links.
