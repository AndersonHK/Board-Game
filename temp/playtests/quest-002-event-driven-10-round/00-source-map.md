# Quest 002 Source Map

This file captures the corrected model used for the second simulation pass.

## Canonical Anchors

- The game should create emergent relationship storytelling, not just efficient optimization ([core-concept](../../../docs/design/core-concept.md)).
- Encounter cards are scene events, not fixed threat numbers ([core-concept](../../../docs/design/core-concept.md), [deck-architecture](../../../docs/design/deck-architecture.md)).
- Events may spawn monsters, hazards, bargains, rescues, or prep windows ([deck-architecture](../../../docs/design/deck-architecture.md), [round-structure](../../../docs/design/round-structure.md)).
- Monster cards, persistent scene cards, and player-controlled ally cards should aim toward one shared entity grammar ([core-concept](../../../docs/design/core-concept.md), [deck-architecture](../../../docs/design/deck-architecture.md)).
- The opening tension-0 round should be a prep beat with no monster threat ([round-structure](../../../docs/design/round-structure.md)).
- The same event can scale by escalation band by spawning different entities ([round-structure](../../../docs/design/round-structure.md)).

## Provisional Rules For This Run

- Shared party HP: 12
- Hand size at start: 3
- Baseline draw: 1 at end of each round
- Hand limit: 6 at cleanup
- Prep round: at tension 0, each player may play 1 setup card before the dungeon starts
- Default save roll: 4+ on d6
- Spotlight scoring: most story-defining player in a cleared scene gains 1 Spotlight; final boss scene awards 2
- Hidden agenda bonus: 3 Spotlight if completed

## Entity Grammar Used In This Run

All monsters, allied summons, and persistent scene cards use the same simple format:

- name
- HP or durability
- attack or support value if relevant
- one short text ability

This is not final canon. It is the smallest reusable grammar that lets event cards spawn enemies while action cards can create allied entities or answer persistent obstacles and enchantments.

## What This Run Is Trying To Learn

1. Does a prep round improve pacing?
2. Do selfish setup cards create better table drama than simple pass-or-help decisions?
3. Do event scenes feel more alive than fixed threat encounters?
4. Does escalation-band spawning make encounter blurbs feel flexible?
5. Do persistent scene cards such as miasma create useful continuity across rounds?
6. Does the design want a dedicated enemy or entity reserve?
