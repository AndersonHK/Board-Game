# Round Structure

This file captures the current round-flow hypothesis and escalation logic. The broader concept brief lives in [core-concept.md](./core-concept.md). The deck roles live in [deck-architecture.md](./deck-architecture.md). Canonical numeric and timing baselines live in [../../defines/core-rules.md](../../defines/core-rules.md) and [../../defines/creature-deck.md](../../defines/creature-deck.md). Relevant escalation research lives in [../research/hearts-of-iron-iv-world-tension.md](../research/hearts-of-iron-iv-world-tension.md) and [../research/stellaris-crises.md](../research/stellaris-crises.md).

## Current Round Hypothesis

The older sketch of "draw encounter, solve threat, play actions, raise tension" is too flat for the current design direction.

The better working model is:

1. at tension 0, run a prep scene instead of a hostile encounter
2. reveal the next encounter event
3. resolve the event's immediate text
4. spawn any monsters, hazards, doors, enchantments, or tests created by that event
5. `Action Turn 1`: each player takes 1 action
6. mid-encounter draw: each player draws 1 card only once per encounter unless an effect says otherwise
7. `Action Turn 2`: each player takes 1 action
8. creatures attack or defend once per turn as allowed by the scene
9. resolve cleanup, unresolved hurdles, round-end card effects, and escalation

Some rounds will be battles. Some will be hazards, merchants, shrines, rescues, or pacing beats.

Unless changed by card effects, class abilities, or scene text, players get one action per turn and creatures get one attack or defense opportunity per turn.

If an encounter lasts more than one round, the default draw between turns 1 and 2 does not repeat on later rounds of that same encounter. That rule helps stop players from farming one nearly-cleared scene for free card flow before the final ordeal.

## Escalation Track

- current range: 0 to 10
- likely midpoint spike: 5 or 6
- likely climax: 10

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

## Candidate Escalation Bands

Not yet confirmed, but a clean first pass could be:

- 0 to 3: prep / opportunity-rich / lower danger
- 4 to 6: pressure / midpoint disruption / harder tradeoffs
- 7 to 9: crisis / high stakes / best cards matter
- 10: climax / boss or final ordeal

That banding is an inference, not a settled rule.

## Event Scaling Example

One useful pattern is to let the same encounter blurb spawn different entity cards by escalation band.

For example:

- `Ashen Ambush`
  - low tension: spawn 2 goblin skulkers
  - mid tension: spawn 2 orc raiders
  - high tension: spawn 1 ogre brute

This keeps encounter text reusable while letting escalation visibly change the fiction.

## Current Unknowns

- Is scene resolution simultaneous, negotiated, or turn-based?
- What exactly counts as "dealing with" an event when the scene is a trap, bargain, or rescue instead of a fight?
- Can players refuse to contribute to a group problem?
- When are agenda scoring opportunities evaluated?
- What do dice resolve: save throws, card effects, combat, or all of the above?
- How long should spawned monster cards or persistent scene cards remain in play?

## Horizontal Slice Suggestion

For the first horizontal slice, the round should probably prove only these things:

- escalation changes event pressure and card value
- class traits alter how each player contributes
- the party can survive together while still chasing hidden selfish incentives
- non-combat scenes still create real tension and memorable table politics

If the first slice proves those things, the rest of the system can grow from there.
