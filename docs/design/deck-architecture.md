# Deck Architecture

This file defines the current four-deck structure. The broader design brief lives in [core-concept.md](./core-concept.md). Round timing lives in [round-structure.md](./round-structure.md). Research that informs quest escalation and secret objectives lives in [../research/stellaris-crises.md](../research/stellaris-crises.md) and [../research/secret-objectives-risk-ticket-to-ride.md](../research/secret-objectives-risk-ticket-to-ride.md).

## Overview

The game currently has four deck systems:

1. world / quest system
2. encounter deck
3. resource / artifact / action deck
4. secret agenda deck

These four layers appear to divide responsibilities cleanly:

- quest sets the scenario spine
- encounter sets the current problem or opportunity
- resource-action cards give players their tools
- secret agendas create private incentives

## World / Quest System

### Role

This is not necessarily a normal shuffled deck. It defines the overarching story frame of the game.

### Current Responsibilities

- establish the theme context, such as dungeon crawl or ring-destruction quest
- define what happens at key escalation thresholds
- slightly nudge the rules with a scenario trait
- frame the start state at tension 0 and the climax at tension 10

### Example

For a D&D-style quest:

- tension 0: players begin outside or near the top of the dungeon
- tension 10: players face the dragon
- scenario trait example: each player may take 1 additional action each round

### Design Notes

- This system is the main bridge between theme packs and the shared rules engine.
- It should probably be compact: one quest card, sheet, or board insert may be enough.
- The strongest adaptation lesson from [Stellaris crisis structure](../research/stellaris-crises.md) is to make the midpoint and endpoint feel like actual phase changes in pressure, not just bigger numbers.

## Encounter Deck

### Role

Each round, the party draws an encounter card representing what the group discovered or must deal with that round.

### Current Example Space

- ambush
- mysterious room
- trader

### Design Notes

- Encounters appear to be the main source of short-term threats and opportunities.
- They should force meaningful decisions about whether to spend strong action cards now or save them.
- Different escalation bands may cause the same encounter to behave differently.

## Resource / Artifact / Action Deck

### Role

This is the shared action-economy deck, closest to the "cards in hand" layer of the game.

### Current Function

- players collect these cards over time
- these cards represent equipment, spells, or actions
- players use them to solve encounters and pursue their own incentives
- players want to acquire more of them and save their best ones

### Design Notes

- This deck appears to be the main economic engine of the game.
- It is where class identities may become most legible.
- The user's current intuition is:
  - support gains more through team play
  - defensive gains more through independent slow play and preservation
  - aggressive wants to spike, rush, and claim credit

### Tension Scaling Idea

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

### Design Notes

- The most relevant lesson from [Risk and Ticket to Ride objective research](../research/secret-objectives-risk-ticket-to-ride.md) is that secret goals work best when they are legible enough to matter but hidden enough to create uncertainty.
- These agendas should create selfish play, but not sabotage so strong that the party cannot realistically survive.

## Design Tension Summary

The four systems currently imply this layered structure:

- public scenario pressure from the quest
- public round pressure from encounters
- private tactical options from hand cards
- private strategic incentives from agendas

That is a strong shape for a short game.
