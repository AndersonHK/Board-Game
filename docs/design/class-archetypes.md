# Class Archetypes

This file captures the stable class identities that should survive across theme packs. The broader concept brief lives in [core-concept.md](./core-concept.md). Long-term project memory lives in [../project-memory.md](../project-memory.md). Research shaping this file lives in [../research/hearthstone-hero-powers.md](../research/hearthstone-hero-powers.md), [../research/civilization-traits-and-unique-abilities.md](../research/civilization-traits-and-unique-abilities.md), and [../research/yugioh-tribute-and-mtg-discard-costs.md](../research/yugioh-tribute-and-mtg-discard-costs.md).

## Design Goal

The class system should create major strategic divergence from very small rules text. Ideally each class can be explained in under a minute, likely through one passive trait and one active trait, while still pulling players toward meaningfully different play patterns.

## Shared Rule

Class names and flavor change with the theme pack, but class mechanics stay the same.

## 2026-04-21 Working Labels

These are the current working labels for the underlying archetypes.

The user wanted labels that describe player personality and play style more than abstract mechanical taxonomy.

### Style-Forward Archetype Labels

- `Bold` / `Guarded` / `Guiding`
- `Daring` / `Patient` / `Nurturing`
- `Greedy` / `Careful` / `Devoted`
- `Gambler` / `Keeper` / `Caretaker`

### Vertical-Slice Fantasy Mapping

- `Warrior` maps to the aggressive archetype
- `Wizard` maps to the defensive storage archetype
- `Cleric` maps to the support rescue archetype

### Current Working Set

The current accepted trio is:

- `Daring` for the aggressive archetype
- `Patient` for the late-game storage archetype
- `Nurturing` for the cooperation archetype

For fantasy presentation in the first playable slice, those map cleanly to:

- `Warrior`
- `Wizard`
- `Cleric`

This split is currently preferred over forcing one set of names to do both jobs.

## Archetype 1: Aggressive

### User Description

- damage focus
- high risk, high reward
- glass cannon
- all or nothing
- joker
- daring

### Theme Mappings

- fantasy: rogue, barbarian, warrior
- strategy-language mapping: "play wide"
- prisoner-dilemma framing: low trust, greedy

### Design Identity

This class should convert volatility into upside. It wants explosive turns, sharp tempo swings, and strong benefits for taking risks early or striking when the table is unstable.

### Mechanical Signals To Preserve

- reward for acting first, acting boldly, or overextending successfully
- weak protection against retaliation or attrition
- better burst than sustainability
- incentives to escalate the table state rather than stabilize it
- incentives to claim visible credit for decisive moments, especially on spawned enemies or dramatic scene turns

### Ability Design Direction

- passive should reward aggression, expansion, or opportunism
- active should create a short pressure spike or high-variance play
- avoid giving it simply "bigger numbers" with no tradeoff

### 2026-04-21 Draft Rule Direction

- user-requested passive direction: this archetype should have a chance to gain a normal draw when it scores the last hit on a monster
- the chance should scale using both monster strength and rarity
- the user wants this available on every monster kill, not capped once per round
- the kill must come from that player's own action card, creature card, or class trait damage
- this is promising because Quest 003 already proved that kill credit creates drama
- this is also dangerous because Quest 003 showed that an aggressive player may delay honest contribution while waiting for a safe finishing window

### 2026-04-21 Draft Active Direction

- all classes should have a baseline `1`-damage basic attack as a normal action
- the aggressive class active should sit above that baseline and deal `2` damage once per turn
- this keeps the Warrior clearly more explosive than the shared fallback line
- this also increases the need to define the last-hit passive carefully, because the active makes kill stealing easier by design

### Questions Before Canonization

1. Do summoned allied creatures or borrowed damage effects count for the kill if they were controlled by the aggressive player?
2. Are there any monster exceptions, such as bosses with special defeat text, that should not trigger the passive?

## Archetype 2: Defensive / Cautious

### User Description

- slow
- late-game focused
- slowly builds up
- protects resources
- hoards resources
- focuses on long-term passive build up
- focused on not losing rather than winning
- crowd-control flavored in D&D mapping

### Theme Mappings

- fantasy: wizard, sorcerer
- strategy-language mapping: "play tall"
- prisoner-dilemma framing: low trust, loss averse

### Design Identity

This class should convert patience and restraint into compounding value. It wants insulation, storage, delayed power, and long-horizon advantages that become obvious only after several rounds.

### Mechanical Signals To Preserve

- rewards for saving, stockpiling, or preserving assets
- strong protection against loss, theft, or waste
- slower access to peak power
- preference for predictable gains over swingy spikes
- strength in discard-heavy, hazard-heavy, or save-heavy scenes, not only straightforward combat

### Ability Design Direction

- passive should reward retention, defense, or engine-building
- active should reduce downside, deny threats, or convert stored value efficiently
- avoid making it purely passive to the point of feeling inert

### 2026-04-21 Draft Rule Direction

- user-requested passive direction: this archetype's max hand size is `12` instead of `6`
- the user wants this active from the start of the game
- this fits the established "save, stockpile, preserve, then outlast" identity very cleanly
- Quest 003 is important context here because the baseline hand limit of `6` already felt good under pressure, so `12` is a dramatic asymmetry rather than a minor perk

### 2026-04-22 Draft Active Direction

- once per scene, place `2` shield tokens on the party or on any creature
- shield tokens should prevent damage `1` for `1` and expire when the scene ends
- the user explicitly wants this targeting to stay broad rather than friendly-only, because simplicity matters more than a narrow thematic restriction

### Questions Before Canonization

1. Does this archetype still begin with the normal starting hand of `3`, or should storage identity also change setup?
2. Should this archetype get any compensating weakness, such as slower draw, weaker burst, or more expensive big cards?
3. Should the support and aggressive archetypes get any way to pressure or exploit oversized hands, or is this meant to be a mostly safe privilege?
4. Do we want a printed reminder that the larger hand cap affects cleanup only and does not create extra draw windows by itself?

## Archetype 3: Support / Cooperative

### User Description

- cooperation focused
- mediator
- diplomat
- thrives on win-win cooperation and synergy
- communicates and cooperates
- all about mutual gain

### Theme Mappings

- fantasy: cleric, priest, healer, support
- strategy-language mapping: mutual boosting
- prisoner-dilemma framing: high trust

### Design Identity

This class should profit from relationships. It wants systems where helping, bargaining, enabling, or synchronizing with others creates value that would not exist in isolation.

### Mechanical Signals To Preserve

- gains value when multiple players benefit together
- can facilitate trades, pacts, or shared triggers
- strong at turning table communication into concrete advantage
- should still have a path to win, not just help others
- should be especially potent when a rescue, save modifier, or last-second intervention changes another player's fate

### Ability Design Direction

- passive should reward deals, adjacency, shared triggers, or joint actions
- active should create temporary alliances, aid, or redistribution with upside
- avoid making it feel like the "kingmaker only" class

### 2026-04-21 Draft Rule Direction

- the user's earlier cleric-style example is now the clearest support anchor:
- when this archetype turns an ally's failed save into a success, a card that ally would have lost can go to the support player's hand instead of the discard pile
- the helped player should choose the card, not the support player
- Quest 003 already stress-tested a lighter version of this pattern through Tamsin's rescue passive, and it created exactly the right kind of "you helped me, but you also profited" table tension
- this is a strong candidate for the support-side economy privilege because it gains cards through intervention rather than storage or killing blows

### 2026-04-22 Active Direction

- once per scene, heal `1` party HP or `2` HP to any creature
- the user wants the targeting to stay broad, including hostile creatures if that ever matters in a scene
- duplicate support passives should stack by default, but only one rescue-style card transfer should happen for a single saved card-loss event

### Questions Before Canonization

1. Should the support rescue passive trigger only when it flips a failed save into a success, or whenever it prevents another player's card loss by any means?
2. If an ally would lose multiple cards, should support rescue only `1`, or should stronger support effects scale that number?
3. Should this be the passive, while the active remains a once-per-scene bonus to saves or tests?
4. Should the support rescue work only on ordeal-style saves and non-combat losses, or on combat-linked discard effects too?

## Cross-Archetype Tension

The three archetypes appear designed to sit on different trust and risk axes:

- aggressive: risks loss for upside
- defensive: accepts lower tempo to reduce downside
- support: accepts interdependence to create shared upside

This is likely one of the game's most original ingredients and should remain legible in every rules iteration.

## Ability Constraints

Based on the user's intent and the relevant research:

- abilities should be short
- abilities should modify existing rules instead of adding many sub-rules
- each class should feel strategically distinct by round 2 or 3
- abilities should create meta consequences over time, not only one-off moments

## Draft Evaluation Rubric

Any class ability set should be judged by these questions:

1. Can a player explain the class in one sentence?
2. Does the class change incentives rather than only outcomes?
3. Does the class create a recognizable play pattern within the first few rounds?
4. Does the class still work if the theme art and naming change completely?
5. Does the class remain understandable in a four-player classroom teach?

## Current Debate Focus

Before any of this moves into [../../defines](../../defines/README.md), we should settle:

- any edge cases on warrior kill credit
- the exact support rescue grammar
- whether the storage archetype needs any real drawback to offset `12` hand size from setup
