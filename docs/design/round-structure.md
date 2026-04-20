# Round Structure

This file captures the current round-flow hypothesis and escalation logic. The broader concept brief lives in [core-concept.md](./core-concept.md). The deck roles live in [deck-architecture.md](./deck-architecture.md). Relevant escalation research lives in [../research/hearts-of-iron-iv-world-tension.md](../research/hearts-of-iron-iv-world-tension.md) and [../research/stellaris-crises.md](../research/stellaris-crises.md).

## Current Round Hypothesis

The user's current round sketch is:

1. draw or reveal the current encounter
2. the party deals with the ordeal
3. players may play action cards
4. tension rises by 1

Some cards or encounters may lower tension, and some effects may scale by current escalation level.

## Escalation Track

- current range: 0 to 10
- likely midpoint spike: 5 or 6
- likely climax: 10

This suggests a short, structured arc that fits a 30 to 40 minute session.

## What Escalation Currently Does

Based on the user's intent, escalation may affect:

- quest threshold events
- action-card outcomes
- encounter-card outcomes
- class skill value
- overall stakes and survival pressure

## Good Design Opportunity

Because the same card can mean different things at different escalation levels, the game can get dramatic without needing a huge deck count.

This is especially promising for a one-week project because it creates replayable tension by context instead of by content volume.

## Candidate Escalation Bands

Not yet confirmed, but a clean first pass could be:

- 0 to 3: setup / opportunity-rich / lower danger
- 4 to 6: pressure / midpoint disruption / harder tradeoffs
- 7 to 9: crisis / high stakes / best cards matter
- 10: climax / boss or final ordeal

That banding is an inference, not a settled rule.

## Current Unknowns

- Do players draw resources every round automatically, or only through card effects and rewards?
- Is encounter resolution simultaneous, negotiated, or turn-based?
- What exactly counts as "dealing with" an encounter?
- Can players refuse to contribute to a group problem?
- When are agenda scoring opportunities evaluated?
- What do dice resolve: encounter tests, card effects, combat, or all of the above?

## Horizontal Slice Suggestion

For the first horizontal slice, the round should probably prove only these things:

- escalation changes card and encounter value
- class traits alter how each player contributes
- the party can survive together while still chasing hidden selfish incentives

If the first slice proves those three things, the rest of the system can grow from there.
