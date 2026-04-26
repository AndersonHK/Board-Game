# Round Structure

This file captures the current round-flow hypothesis and escalation logic. The broader concept brief lives in [core-concept.md](./core-concept.md). The deck roles live in [deck-architecture.md](./deck-architecture.md). Canonical numeric and timing baselines live in [../../defines/core-rules.md](../../defines/core-rules.md) and [../../defines/creature-deck.md](../../defines/creature-deck.md). Relevant escalation research lives in [../research/hearts-of-iron-iv-world-tension.md](../research/hearts-of-iron-iv-world-tension.md) and [../research/stellaris-crises.md](../research/stellaris-crises.md).

## Current Round Hypothesis

The older sketch of "draw encounter, solve threat, play actions, raise escalation" is too flat for the current design direction.

The better working model is:

1. at escalation 0, run a prep scene instead of a hostile encounter
2. reveal the next encounter event
3. resolve the event's `Reveal Text`, including any monsters, hazards, doors, enchantments, or tests created by that event
5. `Action Turn 1`: every player takes 1 action if able, in an order chosen by the players
6. `Enemy Turn 1`: every enemy monster takes 1 action if able, from strongest to weakest, with toss-ups chosen by the players
7. standard draw: each player draws 1 card once per round
8. `Action Turn 2`: every player takes 1 action if able, in an order chosen by the players
9. `Enemy Turn 2`: every enemy monster takes 1 action if able, from strongest to weakest, with toss-ups chosen by the players
10. resolve cleanup, unresolved hurdles, round-end card effects, and escalation

Some rounds will be battles. Some will be hazards, merchants, shrines, rescues, or pacing beats.

Unless changed by card effects, class abilities, or scene text, players get one action in each player action turn and enemy monsters get one action in each enemy turn.

If a round ends before the normal between-turn draw window is reached, that standard draw still happens at round end. The default draw is once per round, not once per encounter.
If a scene clears during a round, finish the current round structure unless a card or quest says the scene ends immediately.
When a scene reward condition is met, the current quickstart resolves that reward immediately unless the card says otherwise, then the table finishes the current round structure.

## Prep Scene Procedure

The current vertical slice begins at escalation `0` with a prep scene.

The working player-facing procedure is:

1. run one normal non-hostile round
2. let players use legal setup actions, card plays, class actives, and other normal action windows
3. if no hostile or blocking hurdles are created, the prep scene clears at end of round
4. the quest then raises escalation as normal for clearing a new scene

This procedure was promoted from Quest 007's ruling because the quest card states that a prep scene exists, but there is not currently a dedicated prep encounter card.

## Escalation Track

- current range: 0 to 10
- midpoint spike: 5 in the current `Ashen Depths` quest
- additional late pressure: 8 in the current `Ashen Depths` quest
- climax: 10

This suggests a short, structured arc that fits a 30 to 40 minute session.

## What Escalation Currently Does

Based on the user's intent, escalation may affect:

- quest threshold events
- action-card outcomes
- encounter event mix
- which entity cards a scene can spawn
- the severity of discard, damage, or other fallout
- class skill value
- overall stakes and survival pressure

It does not need to mean that every later round is just a larger combat number.

At escalation 10, the normal two-turn round cap stops applying. The final ordeal continues until it resolves or the party is defeated.

## Good Design Opportunity

Because the same event or card can mean different things at different escalation levels, the game can get dramatic without needing a huge deck count.

This is especially promising for a one-week project because it creates replayable tension by context instead of by content volume.

## Current Escalation Bands

The current quickstart uses:

- `0-3`: early / green
- `4-6`: mid / yellow
- `7-9`: late / red
- `10`: final ordeal / skull

This is now player-facing for the vertical slice, though future quests may rename or reinterpret the bands.

## Tracker Presentation Direction

The user wants the printed escalation meter to communicate the three main pressure bands visually:

- green for the early band
- yellow for the mid band
- red for the late band
- a skull symbol next to `10` for the final ordeal

This presentation also lines up cleanly with the current three threat tiers for monsters and Warrior reward scaling.

## Damage And Reward Timing Clarifications

The latest quickstart includes two small but important table-play defaults:

- excess damage to a single target does not carry over to the party or another target unless a card says otherwise
- rewards resolve when their condition is met unless a card says otherwise, even if the table then finishes the rest of the round

These defaults keep common play cases from needing designer interpretation, especially when friendly creatures absorb enemy attacks or a scene clears during `Action Turn 1`.

## Event Scaling Example

One useful pattern is to let the same encounter blurb spawn different entity cards by escalation band.

For example:

- `Ashen Ambush`
  - low escalation: spawn 2 goblin skulkers
  - mid escalation: spawn 2 orc raiders
  - high escalation: spawn 1 ogre brute

This keeps encounter text reusable while letting escalation visibly change the fiction.

## Remaining Future Questions

- How many different non-combat scene patterns can the game support before the quickstart needs another reference sheet?
- Should future quests add printed prep-scene cards, or is the current generic prep procedure enough?
- How often should persistent cards carry forward between scenes without making cleanup confusing?
- How much support-success tracking can agendas ask for before scoring becomes too interpretive?
- Should future combat keywords ever add damage carry-over, or should no spillover remain the default unless printed?

## Horizontal Slice Suggestion

For the first horizontal slice, the round should probably prove only these things:

- escalation changes event pressure and card value
- class traits alter how each player contributes
- the party can survive together while still chasing hidden selfish incentives
- non-combat scenes still create real tension and memorable table politics

If the first slice proves those things, the rest of the system can grow from there.
