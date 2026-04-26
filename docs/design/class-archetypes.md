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

### Current Vertical-Slice Rule

For the vertical-slice fantasy rules, the `Warrior` has:

- a passive kill reward when the Warrior deals the final point of damage to a monster with their own action card, creature card, or Warrior trait damage
- a `1d6` reward roll that succeeds on `monster threat x rarity multiplier`
- `Common = 1` and `Elite = 2` as rarity multipliers
- `Threat 1`, `Threat 2`, and `Threat 3` as the current monster threat tiers
- no once-per-round cap on the passive in the current quickstart
- an active that deals `2` damage once per turn

The current reward ladder is:

- `Threat 1 Common`: draw on `1`
- `Threat 2 Common`: draw on `1-2`
- `Threat 3 Common`: draw on `1-3`
- `Threat 1 Elite`: draw on `1-2`
- `Threat 2 Elite`: draw on `1-4`
- `Threat 3 Elite`: draw on `1-6`

This formula is intentionally easy to compute at the table and preserves the design idea that bigger, rarer monsters create bigger personal incentives. It also makes the strongest elite kills guaranteed rewards, which is desirable for drama but still needs balance watching because kill credit can encourage sandbagging.

All classes also have the shared fallback option of a basic `1`-damage attack as a normal action. The Warrior active sits above that baseline, which makes the class visibly more explosive and makes kill stealing part of its intended tension.

### Remaining Watchpoints

1. Borrowed or support-granted damage should be watched carefully so kill credit stays legible.
2. Bosses currently can trigger the passive if they are monsters; future boss exceptions should be printed explicitly if needed.
3. Quest 003 and Quest 007 both suggest kill credit is exciting, but it can still reward waiting for safe finishing windows.

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

### Current Vertical-Slice Rule

For the vertical-slice fantasy rules, the `Wizard` has:

- a passive hand limit of `12` instead of `6`, active from the start of the game
- the normal starting hand size for the player count; the larger hand limit does not grant extra draws
- an active, once per scene, that places `2` shield tokens on the party or on any creature
- shield tokens prevent damage `1` for `1` and expire when the scene ends unless a card says otherwise

This fits the "save, stockpile, preserve, then outlast" identity cleanly. Quest 003 and Quest 007 are important context because the baseline hand limit of `6` already felt meaningful, so `12` is a dramatic asymmetry rather than a minor perk.

### Remaining Watchpoints

1. Quest 007 suggests Wizard Treasure scoring plus owned permanents can narrowly beat very high Warrior Glory scoring, which may be fun or may need later adjustment.
2. The larger hand cap may need a compensating weakness only if further tests show it outpaces the other scoring routes too reliably.

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

### Current Vertical-Slice Rule

For the vertical-slice fantasy rules, the `Cleric` has:

- a passive, once per scene, that gives another player's save `+1`
- if that `+1` turns a failure into a success, the helped player chooses `1` card they would have lost, and that card goes to the Cleric's hand instead of the discard pile
- if multiple Clerics could claim the same rescue-style transfer, only `1` transfer happens and ties are broken with a d6 roll
- an active, once per scene, that heals `1` party HP or `2` HP to any creature

This keeps the support economy distinct: the Cleric gains through intervention rather than hoarding or kill credit. Quest 003 and Quest 007 both show that this creates the desired "you helped me, but you also profited" table tension.

### Remaining Watchpoints

1. The vertical slice currently triggers the passive only when the Cleric's save modifier flips another player's failed save into a success.
2. Broader "prevented allied loss" triggers may still be useful future design space, but they are not part of the current quickstart passive.
3. The `By My Grace` agenda now needs concrete support-success examples printed on the card, because support scoring should not require designer interpretation.

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

For the vertical-slice demo, the core class rules above are now player-facing in [../quick-start-guide.md](../quick-start-guide.md). Remaining debate is mostly balance and edge-case clarity:

- whether Warrior kill credit needs future exceptions for unusual bosses or heavily support-modified damage
- whether Wizard's `12` hand limit plus owned permanents scores too efficiently
- whether future support designs should broaden rescue beyond flipped saves
