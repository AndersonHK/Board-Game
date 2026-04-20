# Repository Directory

This file is the canonical map of the repository structure and the purpose of important files and folders. Long-term project context lives in [project-memory.md](./project-memory.md). Repo-wide Codex instructions live in [../CODEX.md](../CODEX.md). The user-facing entry point remains [../README.md](../README.md).

## Current Structure

```text
/
|-- assets/
|   `-- README.md
|-- CODEX.md
|-- defines/
|   `-- README.md
|-- README.md
|-- temp/
|   `-- playtests/
|       `-- quest-001-standard-10-round/
|           |-- 00-source-map.md
|           |-- 01-quest-frame.txt
|           |-- 02-player-roster.txt
|           |-- 03-agendas.txt
|           |-- 04-resource-pool.txt
|           |-- 05-encounters.txt
|           |-- 06-simulation-log.txt
|           |-- 07-rulings-log.txt
|           `-- 08-findings.md
|       `-- quest-002-event-driven-10-round/
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
    |   |-- class-archetypes.md
    |   |-- core-concept.md
    |   |-- deck-architecture.md
    |   `-- round-structure.md
    |-- project-memory.md
    |-- research/
    |   |-- betrayal-at-house-on-the-hill.md
    |   |-- civilization-traits-and-unique-abilities.md
    |   |-- hearts-of-iron-iv-world-tension.md
    |   |-- hearthstone-hero-powers.md
    |   |-- research-index.md
    |   |-- secret-objectives-risk-ticket-to-ride.md
    |   `-- stellaris-crises.md
    `-- repository-directory.md
```

## File Guide

- [../assets/README.md](../assets/README.md): notes for the future canonical art and print-asset folder.
- [../CODEX.md](../CODEX.md): root operating instructions for Codex, including how to maintain project documentation.
- [../defines/README.md](../defines/README.md): notes for the future canonical numeric and rules-define folder.
- [../README.md](../README.md): lightweight project overview and pointer hub for the repository.
- [design/core-concept.md](./design/core-concept.md): evolving design brief, current concept framing, and system-level implications.
- [design/class-archetypes.md](./design/class-archetypes.md): stable mechanical class identities, player personas, and ability design notes.
- [design/deck-architecture.md](./design/deck-architecture.md): current definition of the four deck systems and how each one shapes play.
- [design/round-structure.md](./design/round-structure.md): current round order, escalation flow, and timing assumptions.
- [project-memory.md](./project-memory.md): long-term project memory, including goals, constraints, principles, decisions, and open questions.
- [research/research-index.md](./research/research-index.md): index of topic research notes and their design relevance.
- [research/betrayal-at-house-on-the-hill.md](./research/betrayal-at-house-on-the-hill.md): notes on modular exploration, phase shift, and traitor-reveal structure.
- [research/hearts-of-iron-iv-world-tension.md](./research/hearts-of-iron-iv-world-tension.md): notes on shared escalation tracks and threshold-based unlocking.
- [research/hearthstone-hero-powers.md](./research/hearthstone-hero-powers.md): notes on compact, repeatable hero asymmetry.
- [research/civilization-traits-and-unique-abilities.md](./research/civilization-traits-and-unique-abilities.md): notes on small rule changes with compounding strategic impact.
- [research/stellaris-crises.md](./research/stellaris-crises.md): notes on midgame and endgame crisis structure for escalation milestones.
- [research/secret-objectives-risk-ticket-to-ride.md](./research/secret-objectives-risk-ticket-to-ride.md): notes on hidden objectives, secrecy, and endgame scoring tension.
- [repository-directory.md](./repository-directory.md): this file; the current repository map and documentation conventions.
- [../temp/playtests/quest-001-standard-10-round/](../temp/playtests/quest-001-standard-10-round/): temporary first-pass simulation package for a 10-round fantasy quest, including source extraction, mock content, a full roleplayed run, live rulings, and recommendations.
- [../temp/playtests/quest-002-event-driven-10-round/](../temp/playtests/quest-002-event-driven-10-round/): temporary second-pass simulation package built around scene events, spawned entities, non-combat pacing, and stronger relationship drama.

## Documentation Conventions

1. Use markdown links when referring to canonical docs, relevant files, or important folders.
2. Keep this file updated when major files or folders are added.
3. Keep [project-memory.md](./project-memory.md) updated when the project's durable understanding changes.
4. Keep [../README.md](../README.md) concise and oriented toward human navigation.
5. Keep [../CODEX.md](../CODEX.md) as the standing instruction set for Codex behavior in this repo.

## Planned Growth

These areas are likely to appear later once the game concept is defined:

- more design documents for rules, mechanics, and components
- art references and generated assets
- printable production files
- playtest notes and iteration logs

When those folders or files are created, add them here with a short purpose statement and links.
