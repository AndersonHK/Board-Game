# Repository Directory

This file is the canonical map of the repository structure and the purpose of important files and folders. Long-term project context lives in [project-memory.md](./project-memory.md). Repo-wide Codex instructions live in [../CODEX.md](../CODEX.md). The user-facing entry point remains [../README.md](../README.md).

## Current Structure

```text
/
|-- assets/
|   |-- card-atlas-definition.md
|   |-- card-text-fit-report.md
|   |-- print-and-bundle-package.md
|   |-- scripts/
|   |   |-- calculate_card_layout.py
|   |   `-- check_card_text_fit.py
|   `-- README.md
|-- CODEX.md
|-- defines/
|   |-- card-layout.md
|   |-- cards/
|   |   |-- agenda-deck/
|   |   |   |-- TEMPLATE.txt
|   |   |   `-- cards/
|   |   |-- creature-deck/
|   |   |   |-- TEMPLATE.txt
|   |   |   `-- cards/
|   |   |-- encounter-deck/
|   |   |   |-- TEMPLATE.txt
|   |   |   `-- cards/
|   |   |-- quest-deck/
|   |   |   |-- TEMPLATE.txt
|   |   |   `-- cards/
|   |   |-- resource-deck/
|   |   |   |-- TEMPLATE.txt
|   |   |   `-- cards/
|   |   `-- README.md
|   |-- core-rules.md
|   |-- creature-deck.md
|   `-- README.md
|-- README.md
|-- temp/
|   `-- playtests/
|       |-- quest-001-standard-10-round/
|           |-- 00-source-map.md
|           |-- 01-quest-frame.txt
|           |-- 02-player-roster.txt
|           |-- 03-agendas.txt
|           |-- 04-resource-pool.txt
|           |-- 05-encounters.txt
|           |-- 06-simulation-log.txt
|           |-- 07-rulings-log.txt
|           `-- 08-findings.md
|       |-- quest-002-event-driven-10-round/
|           |-- 00-source-map.md
|           |-- 01-quest-frame.txt
|           |-- 02-player-roster.txt
|           |-- 03-agendas.txt
|           |-- 04-action-pool.txt
|           |-- 05-events.txt
|           |-- 06-entities.txt
|           |-- 07-simulation-log.txt
|           |-- 08-rulings-log.txt
|           `-- 09-findings.md
|       |-- quest-003-canon-stress-test-10-round/
|           |-- 00-source-map.md
|           |-- 01-quest-frame.txt
|           |-- 02-player-roster.txt
|           |-- 03-agendas.txt
|           |-- 04-action-pool.txt
|           |-- 05-events.txt
|           |-- 06-entities.txt
|           |-- 07-simulation-log.txt
|           |-- 08-rulings-log.txt
|           `-- 09-findings.md
|       `-- quest-004-quickstart-4p-sim/
|           |-- 00-source-map.md
|           |-- 01-quest-frame.txt
|           |-- 02-player-roster.txt
|           |-- 03-agendas.txt
|           |-- 04-action-pool.txt
|           |-- 05-events.txt
|           |-- 06-entities.txt
|           |-- 07-simulation-log.txt
|           |-- 08-rulings-log.txt
|           `-- 09-findings.md
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
- [../assets/card-atlas-definition.md](../assets/card-atlas-definition.md): Edition 0 card atlas plan for letter-size printing and cutting, including the exact card grid, cut marks, sheet IDs, and per-sheet card assignments.
- [../assets/card-text-fit-report.md](../assets/card-text-fit-report.md): generated report checking all current card definitions against the standard layout.
- [../assets/print-and-bundle-package.md](../assets/print-and-bundle-package.md): Edition 0 physical production manifest covering cards, rules sheets, board widgets, tokens, dice, bundling groups, and remaining playability gaps.
- [../assets/scripts/calculate_card_layout.py](../assets/scripts/calculate_card_layout.py): script that derives [../defines/card-layout.md](../defines/card-layout.md) from the card atlas size.
- [../assets/scripts/check_card_text_fit.py](../assets/scripts/check_card_text_fit.py): script that checks card `.txt` files against [../defines/card-layout.md](../defines/card-layout.md).
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

## Documentation Conventions

1. Use markdown links when referring to canonical docs, relevant files, or important folders.
2. Keep this file updated when major files or folders are added.
3. Keep [project-memory.md](./project-memory.md) updated when the project's durable understanding changes.
4. Keep [../README.md](../README.md) concise and oriented toward human navigation.
5. Keep [../CODEX.md](../CODEX.md) as the standing instruction set for Codex behavior in this repo.
6. Treat playtest packages as evidence, not canon. Promotion into [../defines](../defines/README.md) requires explicit user approval.

## Planned Growth

These areas are likely to appear later once the game concept is defined:

- more design documents for rules, mechanics, and components
- art references and generated assets
- printable production files
- playtest notes and iteration logs

When those folders or files are created, add them here with a short purpose statement and links.
