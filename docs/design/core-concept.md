# Core Concept

This file is the evolving design brief for the game. Durable high-level project context lives in [../project-memory.md](../project-memory.md). Class identity details live in [class-archetypes.md](./class-archetypes.md). Current cost and rarity direction lives in [card-economy-and-rarity.md](./card-economy-and-rarity.md). Research references live in [../research/research-index.md](../research/research-index.md).

## Current Brief

- The game should work for the classroom use case of four players, but the system should ideally scale beyond that.
- The system should support multiple theme packs while preserving the same mechanics.
- The current component concept is four player-facing decks or deck-like systems, a formal creature deck, three classes, and some dice.
- The initial vertical-slice theme is leaning toward classic D&D-style fantasy.
- The class layer should be simple enough to explain in about a minute but meaningful enough to create a real strategic meta.
- The current target playtime is about 30 to 40 minutes.
- The game has no spatial map board, but it will use table widgets or trackers for escalation and status.
- The guiding principle is emergent relationship storytelling: players should feel like competing heroes in the same tale, sometimes grateful to one another and sometimes resentful.
- The current component direction also includes tiny red damage tokens for tracking entity HP and a printed escalation meter with clear early, mid, and late danger zones.
- The future Quick Start Guide should stay fully inside the fantasy presentation and teach the game in player-facing language rather than internal design terminology.

## Inspiration Frame

The user's reference triangle currently appears to be:

1. [Betrayal at House on the Hill](../research/betrayal-at-house-on-the-hill.md): useful for sudden mode shifts, scenario framing, and recontextualized scenes.
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

The desired emotional output is not clean optimization. It is bitter-sweet heroism, negotiation, credit-stealing, rescue, and lingering table memory about who helped whom and who chose greed at the wrong moment.

## Escalation Frame

The current escalation track runs from 0 to 10.

- At 0, the players begin with a prep scene outside or near the top of the dungeon.
- Around 5 or 6, the quest likely introduces a major midpoint escalation.
- At 10, the quest reaches its climax, such as facing the dragon in the D&D-flavored example.

The world/quest system may also define a light ongoing rule modifier or a scene mix shift. More specific structure lives in [deck-architecture.md](./deck-architecture.md) and [round-structure.md](./round-structure.md).

## Encounter Model Correction

The encounter deck should not be understood as a stack of fixed numeric threat cards.

Instead, each encounter card is better framed as an event or scene prompt. An event may:

- spawn one or more monster or hazard cards
- force save throws, discards, or other tests
- create a social bargain, merchant beat, or moral choice
- offer a preparation or engine-building window instead of immediate combat
- change what players are incentivized to do in that scene

This means the "problem" of a round is authored first by the event text, and only then expressed mechanically through whatever entities, rolls, losses, choices, or opportunities that event creates.

The same event can also scale by escalation band. For example, an ambush scene might spawn goblins at low tension, orcs at mid tension, and an ogre at high tension. That sort of blurb-driven escalation currently feels more correct than assigning the event one fixed challenge number.

## Entity Layer Direction

The creature deck now exists as a formal support deck for spawned enemies and creature packages.

The broader entity layer may still want a shared reserve to hold:

- monsters
- persistent obstacles such as heavy doors
- persistent scene effects such as miasma or enchantments
- player-controlled allies such as familiars or golems

That layer should ideally share one lightweight grammar so the game does not splinter into too many separate micro-systems.

## Action Economy Direction

The resource / artifact / action deck should include both immediate conflict tools and selfish long-term setup cards.

The current draft cost philosophy now also points toward stronger cards being paid for through discards and sacrifices rather than through a separate mana-style economy. The more detailed discussion of that direction lives in [card-economy-and-rarity.md](./card-economy-and-rarity.md).

That matters because a greedy player should be able to spend a scene making themselves stronger, drawing deeper, or setting up future dominance instead of merely "passing" while others do the hard work. That choice is part of the drama.

Examples of the kind of effects now in scope:

- increase this player's future damage
- improve later draw odds or scouting
- summon a persistent ally
- protect cards from discard or loss
- steal or redirect value created by another player's success
- dispel or counter persistent scene effects

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
- Because there is no traitor, the tension must come from agenda friction, scarce action cards, scene pressure, and timing around escalation bands.
- The quest system can act like a scenario skeleton that changes pacing and flavor without changing the core rules engine.
- Secret agendas should tug players away from perfect cooperation, but not so hard that the party self-destructs every game.
- Prep beats and non-combat beats are important. If every round is a fight with a bigger number, the story will feel mechanical instead of lived-in.
- Persistent entities such as monsters, familiars, doors, and miasma may be one of the best places to create memory and attachment in a short session.

## Unknowns Blocking Rules Work

- What exact actions can players take from the resource-action deck?
- What exact grammar should monster cards, persistent scene cards, and player-controlled ally cards share?
- Does the game need a formal enemy or entity reserve in addition to the four core decks?
- What does scene resolution actually require when the scene is not combat?
- How are points or spotlight awarded?
- What do players spend, lose, and protect?
- How do midpoint and endpoint quest escalations manifest in a single 30 to 40 minute session?

## Working Hypothesis

Current hypothesis: the game wants event-authored scenes, a shared escalation track, small class asymmetries, and an action deck that lets players choose between selfish setup and collective problem-solving. The resulting friction should feel like a story about several people all trying to become the remembered hero.
