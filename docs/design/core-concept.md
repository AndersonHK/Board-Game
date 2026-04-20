# Core Concept

This file is the evolving design brief for the game. Durable high-level project context lives in [../project-memory.md](../project-memory.md). Class identity details live in [class-archetypes.md](./class-archetypes.md). Research references live in [../research/research-index.md](../research/research-index.md).

## Current Brief

- The game should work for the classroom use case of four players, but the system should ideally scale beyond that.
- The system should support multiple theme packs while preserving the same mechanics.
- The current component concept is four decks or deck-like systems, three classes, and some dice.
- The initial vertical-slice theme is leaning toward classic D&D-style fantasy.
- The class layer should be simple enough to explain in about a minute but meaningful enough to create a real strategic meta.
- The current target playtime is about 30 to 40 minutes.
- The game has no spatial map board, but it will use table widgets or trackers for escalation and status.

## Inspiration Frame

The user's reference triangle currently appears to be:

1. [Betrayal at House on the Hill](../research/betrayal-at-house-on-the-hill.md): useful for sudden mode shifts, scenario framing, and possibly a recontextualizing midpoint or end-state reveal.
2. [Hearts of Iron IV world tension](../research/hearts-of-iron-iv-world-tension.md): useful for a shared escalation track that unlocks stronger actions as the table becomes more unstable.
3. [Hearthstone hero powers](../research/hearthstone-hero-powers.md) and [Civilization traits and unique abilities](../research/civilization-traits-and-unique-abilities.md): useful for class asymmetry built from very small rules text with large downstream consequences.
4. [Stellaris crises](../research/stellaris-crises.md): useful for midpoint and endgame escalation beats that reshape incentives without requiring a literal traitor.
5. [Risk and Ticket to Ride secret-objective patterns](../research/secret-objectives-risk-ticket-to-ride.md): useful for private goals that create tension inside a shared game state.

## Theme-Pack Direction

The mechanical skeleton should be setting-agnostic. Theme packs change naming, flavor, art, and possibly the fictional interpretation of actions, but should not require a different rules engine.

Examples already named by the user:

- fantasy
- sci-fi
- steampunk
- grimdark

For the first vertical slice, the default mapping is likely:

- aggressive archetype -> rogue / barbarian / warrior flavor family
- defensive archetype -> wizard / sorcerer flavor family
- support archetype -> cleric / priest / healer flavor family

## Class Model

Each player starts by choosing a class. The class flavor varies by theme pack, but the mechanics remain stable.

The current intended class identities are:

- aggressive: damage-focused, high-risk, high-reward, glass-cannon, daring, joker energy
- defensive/cautious: slow build, long-term passive accumulation, resource protection, crowd-control oriented, late-game focused
- support/cooperative: thrives on communication, mutual gain, synergy, diplomacy, and win-win deals

The only player-starting differences between classes should be their class traits. Current expectation: at least one passive trait and one active trait per class.

## Cooperation Frame

There is no explicit traitor role. All players are part of the same party and share a common lose condition: if the party dies or fails to survive the ordeal sequence, everyone loses.

At the same time, each player also has a hidden personal agenda and is trying to end with the most points. This means the game is cooperative at the survival layer and competitive at the scoring layer.

## Escalation Frame

The current escalation track runs from 0 to 10.

- At 0, the players begin at the start of the quest frame, such as outside or near the top of a dungeon.
- Around 5 or 6, the quest likely introduces a major midpoint escalation.
- At 10, the quest reaches its climax, such as facing the dragon in the D&D-flavored example.

The world/quest system may also define a light ongoing rule modifier, such as "each player can take 1 additional action each round." More specific structure lives in [deck-architecture.md](./deck-architecture.md) and [round-structure.md](./round-structure.md).

## Strategic Framing

The user described the archetypes as aligning with idealized strategic personas:

- one low-trust greedy archetype
- one low-trust loss-averse archetype
- one high-trust cooperative archetype

There is also a strategy-game framing:

- aggressive -> playing wide
- defensive/cautious -> playing tall
- support/cooperative -> mutual boosting

This suggests the class layer may be less about combat roles in the RPG sense and more about incentive structures for risk, trust, tempo, and compounding growth.

## Early Design Implications

- The core system should likely create recurring opportunities for conflict, hoarding, and cooperation, or the class identities will feel decorative instead of systemic.
- A shared escalation track could help force all three archetypes to react to the same changing environment in different ways.
- If the game includes negotiation, alliance-making, or temporary cooperation, the support class will have a natural home.
- If the game includes compounding engines or protected stockpiles, the cautious class can meaningfully play for long-term value.
- If the game includes pressure windows or reward spikes, the aggressive class can live off volatility.
- Because there is no traitor, the tension must come from agenda friction, scarce action cards, encounter pressure, and timing around escalation bands.
- The quest system can act like a scenario skeleton that changes pacing and flavor without changing the core rules engine.
- Secret agendas should tug players away from perfect cooperation, but not so hard that the party self-destructs every game.

## Unknowns Blocking Rules Work

- What exact actions can players take from the resource-action deck?
- What does encounter resolution actually require?
- How are points awarded?
- What do players spend, lose, and protect?
- How do midpoint and endpoint quest escalations manifest in a single 30 to 40 minute session?

## Working Hypothesis

Current hypothesis: the game may want a central neutral system that escalates over time, while players choose between selfish extraction, cautious consolidation, and cooperative value-sharing. That is an inference from the user's inspirations and class descriptions, not a confirmed design.
