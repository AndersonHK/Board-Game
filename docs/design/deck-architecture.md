# Deck Architecture

This file defines the current deck structure. The broader design brief lives in [core-concept.md](./core-concept.md). Round timing lives in [round-structure.md](./round-structure.md). Canonical baseline rules live in [../../defines/core-rules.md](../../defines/core-rules.md) and [../../defines/creature-deck.md](../../defines/creature-deck.md). Research that informs quest escalation and secret objectives lives in [../research/stellaris-crises.md](../research/stellaris-crises.md) and [../research/secret-objectives-risk-ticket-to-ride.md](../research/secret-objectives-risk-ticket-to-ride.md). Current cost and rarity direction lives in [card-economy-and-rarity.md](./card-economy-and-rarity.md).

## Overview

The game currently has four player-facing core deck systems plus a formal creature deck:

1. world / quest system
2. encounter deck
3. resource / artifact / action deck
4. secret agenda deck
5. creature deck

These player-facing layers appear to divide responsibilities cleanly:

- quest sets the scenario spine
- encounter sets the current scene, problem, or opportunity
- resource-action cards give players their tools
- secret agendas create private incentives

The creature deck supplies the concrete monsters and creature packages that encounters put into play. Persistent obstacles and enchantments are adjacent to that layer and may continue to share its grammar even if they later become a broader entity reserve.

## World / Quest System

### Role

This is not necessarily a normal shuffled deck. It defines the overarching story frame of the game.

### Current Responsibilities

- establish the theme context, such as dungeon crawl or ring-destruction quest
- define what happens at key escalation thresholds
- slightly nudge the rules with a scenario trait
- frame the start state at escalation 0 and the climax at escalation 10

### Example

For a D&D-style quest:

- escalation 0: players begin outside or near the top of the dungeon with a prep scene
- escalation 10: players face the dragon
- scenario trait example: the first round is setup only, before the descent begins

### Design Notes

- This system is the main bridge between theme packs and the shared rules engine.
- It should probably be compact: one quest card, sheet, or board insert may be enough.
- The strongest adaptation lesson from [Stellaris crisis structure](../research/stellaris-crises.md) is to make the midpoint and endpoint feel like actual phase changes in pressure, not just bigger numbers.

## Encounter Deck

### Role

Each round after the prep beat, the party draws an encounter card representing the scene they just entered. This is not best understood as a fixed threat number. It is the event frame for the round.

### Current Example Space

- ambush
- mysterious room
- trader
- collapsing bridge
- cursed shrine
- rescue scene
- trapped vault

### Design Notes

- Encounters are the main source of short-term threats, opportunities, and scene framing.
- An encounter may spawn monster cards, hazards, save throws, bargains, or downtime-style preparation windows.
- Different escalation bands may cause the same encounter to spawn nastier entities, harsher losses, or more tempting rewards.
- Not every encounter should be combat. Variety is part of the pacing.
- Printable encounter text should treat drawing the card as the reveal. Players immediately see all text on the encounter card, so there is no separate hidden spawn step for the template to model. Immediate scene setup, including spawned monsters, hazards, allies, and persistent cards, belongs in `Reveal Text`.
- Encounter cards should not restate rules already present on spawned entity cards. The encounter should own the scene frame and any scene-specific rule; spawned cards should own their own active abilities, round-end effects, targeting rules, and persistence.

### Important Correction

Encounters do not inherently carry a single assigned threat value.

Instead, the event text determines what mechanics matter in that scene. For example:

- "Falling Causeway" may trigger save rolls and card loss
- "Wandering Merchant" may create a bargaining and draw opportunity
- "Ashen Ambush" may spawn goblins at low escalation, orcs at mid escalation, and an ogre at high escalation

That means the encounter deck is closer to a scene-authoring system than a stack of simple challenge ratings.

### Spawned Entities

Encounter cards may create persistent or temporary scene cards such as:

- monsters
- heavy doors
- miasma or enchantments
- environmental hazards

Those entities should ideally live in a reusable reserve with one lightweight rules grammar, so the encounter deck can stay focused on authored scene blurbs instead of carrying all mechanical detail itself.

### Creature Deck Role

The creature deck is the formal source of spawned enemies and creature packages.

This lets encounters specify either:

- exact named spawns, such as `1 Goblin Chieftain and 2 Goblin Warriors`
- typed criteria, such as `1 Threat 2 humanoid and 2 Threat 1 beasts`

without bloating the encounter text itself.

When an encounter uses criteria instead of exact names, players go through the creature deck in order and take the first cards that satisfy the instruction. That gives the encounter text some flexibility without turning spawning into a search-heavy rules mini-game.

Low-complexity creatures may simply attack and defend, while tougher creatures often carry undesirable round-end text. That expressive range belongs in the creature deck and supporting design work rather than in the core rules defines.

### Creature Taxonomy Direction

The creature deck now appears to want a small amount of formal taxonomy beyond just names.

Current useful fields are:

- creature type, such as humanoid, beast, undead, or construct
- threat value, so encounters can request a rough power band without naming a specific card
- rarity, currently `Common` or `Elite`, to communicate power, copy count, and likely complexity
- a shared rarity field that can also exist on resource cards, so search criteria and effect expectations can use one common language across both systems

One promising interpretation is:

- weaker or minor creatures usually attack and defend without extra round-end text
- elite creatures at the same rough threat band are more likely to carry undesirable round-end effects

That direction is not fully formalized yet, but it already seems useful for writing encounters and organizing the creature deck.

## Shared Rarity Direction

The current vertical slice uses two main rarity bands shared by:

- monster cards
- player resource / artifact / action cards

Those bands are `Common` and `Elite`. This has clear structural benefits:

- encounter cards can search by threat plus rarity
- elite monsters can more easily imply stronger round-end consequences
- elite player cards can more easily imply heavier discard or sacrifice costs
- both sides of the game can teach one common power language instead of two unrelated labels

## Resource / Artifact / Action Deck

### Role

This is the shared action-economy deck, closest to the "cards in hand" layer of the game.

### Current Function

- players collect these cards over time
- these cards represent equipment, spells, actions, preparations, and personal engines
- players use them to solve scenes and pursue their own incentives
- players want to acquire more of them and save their best ones
- players can also use them selfishly to build future advantage instead of immediately helping the party

### Design Notes

- This deck appears to be the main economic engine of the game.
- It is where class identities may become most legible.
- It is also the layer most affected by the user's new directive that stronger cards should be paid for through discards and sacrifices rather than through a separate mana-style currency.
- The user's current intuition is:
  - support gains more through team play
  - defensive gains more through independent slow play and preservation
  - aggressive wants to spike, rush, and claim credit

### Broader Action Scope

The action deck should support both battle and non-battle scenes.

That means cards in this layer can reasonably include:

- direct attacks
- buffs to future attacks
- draw or scouting engines
- anti-discard protection
- negotiation or merchant tools
- ally summons
- setup pieces that persist across scenes
- dispels or counters for persistent obstacles and enchantments

This broader scope is important because it gives selfish players something interesting to do besides simply refusing to help.

### Trader Scene Baseline

The current vertical slice has a concrete trader pattern:

- reveal the top `5` resource cards as trader stock
- each player gets exactly `1` trader interaction
- direct trade means swapping `1` hand card with `1` revealed trader card
- `Haggle` is a `1d6` risk roll: `1-2` discard `1` then trade `1-for-1`, `3-4` trade `1-for-1`, and `5-6` trade `1` hand card for `2` trader cards

This belongs in the design docs because it is not just a card-specific rule. It is the current model for social/economic scenes that give players a selfish setup option without stopping the shared round structure.

### Current Cost Direction

The newest design push suggests this deck should divide broadly into:

- faster cards that can be used with little or no additional payment
- stronger cards that ask for discard, sacrifice, or loss of stored value

That direction appears compatible with the existing simulation evidence, but it needs more balancing discussion before becoming canonical rules text.

### Escalation Scaling Idea

The user suggested that cards may change value by escalation band. Example:

- "Hidden Door" at escalation 1 to 4: chance of 1 to 2 draws
- at escalation 5 to 7: chance of 1 to 3 draws
- at escalation 8 to 10: chance of 2 to 3 draws

This suggests the action deck can remain small while gaining contextual variety from the escalation track.

## Secret Agenda Deck

### Role

After choosing a class, each player takes a hidden agenda card.

### Current Function

- create personal scoring pressure
- tug players away from pure collective optimization
- remain secret from other players
- create traitor-like tension without an actual traitor role

### Example Direction

- collect the most cards
- do the most kills
- ensure a chosen player has the least of something
- become the most visibly heroic in the story

### Design Notes

- The most relevant lesson from [Risk and Ticket to Ride objective research](../research/secret-objectives-risk-ticket-to-ride.md) is that secret goals work best when they are legible enough to matter but hidden enough to create uncertainty.
- These agendas should create selfish play, but not sabotage so strong that the party cannot realistically survive.

## Design Tension Summary

The four systems currently imply this layered structure:

- public scenario pressure from the quest
- public round pressure from scene events
- public board-state pressure from spawned creatures and persistent scene cards
- private and public tactical options from hand cards
- private strategic incentives from agendas

That is a strong shape for a short game.
