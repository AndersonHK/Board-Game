# Deck Architecture

This file defines the current four-deck structure. The broader design brief lives in [core-concept.md](./core-concept.md). Round timing lives in [round-structure.md](./round-structure.md). Research that informs quest escalation and secret objectives lives in [../research/stellaris-crises.md](../research/stellaris-crises.md) and [../research/secret-objectives-risk-ticket-to-ride.md](../research/secret-objectives-risk-ticket-to-ride.md).

## Overview

The game currently has four core deck systems:

1. world / quest system
2. encounter deck
3. resource / artifact / action deck
4. secret agenda deck

These four layers appear to divide responsibilities cleanly:

- quest sets the scenario spine
- encounter sets the current scene, problem, or opportunity
- resource-action cards give players their tools
- secret agendas create private incentives

There may also be an auxiliary reserve of entity cards or tokens for spawned monsters, persistent obstacles, and allied summons. That reserve is not yet treated as a full fifth core deck, but the design is clearly moving in that direction.

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

- tension 0: players begin outside or near the top of the dungeon with a prep scene
- tension 10: players face the dragon
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

### Important Correction

Encounters do not inherently carry a single assigned threat value.

Instead, the event text determines what mechanics matter in that scene. For example:

- "Falling Causeway" may trigger save rolls and card loss
- "Wandering Merchant" may create a bargaining and draw opportunity
- "Ashen Ambush" may spawn goblins at low tension, orcs at mid tension, and an ogre at high tension

That means the encounter deck is closer to a scene-authoring system than a stack of simple challenge ratings.

### Spawned Entities

Encounter cards may create persistent or temporary scene cards such as:

- monsters
- heavy doors
- miasma or enchantments
- environmental hazards

Those entities should ideally live in a reusable reserve with one lightweight rules grammar, so the encounter deck can stay focused on authored scene blurbs instead of carrying all mechanical detail itself.

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
- become the most visibly heroic in the story

### Design Notes

- The most relevant lesson from [Risk and Ticket to Ride objective research](../research/secret-objectives-risk-ticket-to-ride.md) is that secret goals work best when they are legible enough to matter but hidden enough to create uncertainty.
- These agendas should create selfish play, but not sabotage so strong that the party cannot realistically survive.

## Design Tension Summary

The four systems currently imply this layered structure:

- public scenario pressure from the quest
- public round pressure from scene events
- public board-state pressure from spawned entities and persistent scene cards
- private and public tactical options from hand cards
- private strategic incentives from agendas

That is a strong shape for a short game.
