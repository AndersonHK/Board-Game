# Quest 004 Source Map

This file captures the rules stack used for the fourth simulation pass. It is a working extraction, not a canonical rules file.

## Rule Priority Used For This Run

1. `defines/` is the highest-priority canon.
2. If `defines/` is silent, use the player-facing [quick start guide](../../../docs/quick-start-guide.md) because real table players only have that sheet plus cards and widgets.
3. If both of the above are silent, use current design docs for the smallest internal-intent bridge needed to continue.
4. Prior playtests are used for package structure and precedent, not for overriding the live docs.

## Canon From `defines/`

- Starting hand size: `3` ([defines/core-rules.md](../../../defines/core-rules.md)).
- Baseline hand limit: `6` ([defines/core-rules.md](../../../defines/core-rules.md)).
- Standard rounds use two action turns with one default mid-encounter draw between `Action Turn 1` and `Action Turn 2` only once per encounter ([defines/core-rules.md](../../../defines/core-rules.md)).
- If relevant hostile or blocking hurdles remain unresolved at end of round, escalation rises by `1` ([defines/core-rules.md](../../../defines/core-rules.md)).
- At escalation `10`, the normal two-turn round cap no longer applies ([defines/core-rules.md](../../../defines/core-rules.md)).
- The creature deck is a formal rules layer separate from the encounter deck and action deck ([defines/creature-deck.md](../../../defines/creature-deck.md)).
- Encounters may spawn exact named creatures or criteria-based packages, and criteria-based spawning goes through the creature deck in order to take the first valid cards ([defines/creature-deck.md](../../../defines/creature-deck.md)).
- Every creature attacks or defends once per turn unless another effect changes that ([defines/creature-deck.md](../../../defines/creature-deck.md)).

## Player-Facing Baseline From The Quick Start

- Table setup uses a quest sheet, escalation tracker, party HP tracker, encounter deck, resource / action deck, creature deck, secret agenda deck, damage tokens, and `1` d6 ([quick start guide](../../../docs/quick-start-guide.md)).
- The quest itself must state starting party HP, threshold events, and the escalation-`10` final ordeal ([quick start guide](../../../docs/quick-start-guide.md)).
- The available classes are `Warrior`, `Wizard`, and `Cleric`, with the quick-start trait text as the live player-facing wording ([quick start guide](../../../docs/quick-start-guide.md)).
- `Warrior` hand limit is `6`; `Wizard` hand limit is `12`; `Cleric` hand limit is `6` ([quick start guide](../../../docs/quick-start-guide.md)).
- Default saves succeed on `4+` on a d6 unless modified ([quick start guide](../../../docs/quick-start-guide.md)).
- When a new scene is fully cleared, escalation advances by `1`; unresolved scenes do not grant the normal clear-scene advance ([quick start guide](../../../docs/quick-start-guide.md)).
- Blocking hurdles include monsters, doors, persistent hazards, enchantments, and other cards that still block safety, reward, or forward progress ([quick start guide](../../../docs/quick-start-guide.md)).
- If an encounter lasts more than one round, the default mid-encounter draw does not repeat on later rounds of that encounter ([quick start guide](../../../docs/quick-start-guide.md)).

## Supporting Design Intent Used Only When Needed

- The opening escalation-`0` scene should be a prep beat rather than immediate hostility ([docs/design/round-structure.md](../../../docs/design/round-structure.md)).
- Encounter cards are scene-authored events, not flat threat-value cards ([docs/design/core-concept.md](../../../docs/design/core-concept.md), [docs/design/deck-architecture.md](../../../docs/design/deck-architecture.md)).
- The game should support selfish setup, rescue play, and credit tension inside a shared survival frame ([docs/design/core-concept.md](../../../docs/design/core-concept.md)).
- The action deck should support both battle and non-battle scenes ([docs/design/deck-architecture.md](../../../docs/design/deck-architecture.md)).
- The currently preferred four-player simulation shape still includes one duplicate aggressive player because that rivalry produces the clearest selfish-pressure evidence ([Quest 003 findings](../quest-003-canon-stress-test-10-round/09-findings.md)).

## Structure And Precedent Taken From Prior Playtests

- File naming and package layout follow [Quest 003](../quest-003-canon-stress-test-10-round/00-source-map.md).
- The scene sequence again includes prep, social, exact spawn, hazard, persistent enchantment, rescue, criteria spawn, a multi-round fight, and a final ordeal because that structure has produced the clearest evidence so far.

## Run-Only Assumptions Needed To Execute

- Shared party HP: `11`.
- This four-player run allows duplicate classes because the quick start currently lists only three classes.
- Action order inside each action turn is chosen by the table rather than fixed by seat order.
- Spotlight is still used as a temporary prestige proxy for simulation scoring because the quick start does not yet define an endgame prestige procedure.
- The prototype action pool is treated as a catalog for simulated draws rather than a finalized finite deck list.
- Defeated non-boss creatures return to an abstract reserve between scenes, so criteria-based spawning checks the listed creature order fresh each time.
- If escalation reaches `10` during a non-final scene, finish the current scene first and begin the quest's final ordeal on the next encounter reveal.

## What This Run Is Stress Testing

1. Whether the quick-start sheet is now complete enough for a four-player table to run a session without leaning on hidden internal knowledge.
2. Whether duplicate-class play needs explicit player-facing permission now that the classroom use case is four players and the quick start names only three classes.
3. Whether the quick-start class text for `Warrior`, `Wizard`, and `Cleric` is sufficient to run cleanly inside real scenes.
4. Whether the quick-start clarification on blocking hurdles and clear-scene escalation is enough to handle persistent doors and enchantments without extra canon patches.
5. Whether the current agenda and scene-credit prototypes create useful selfish pressure without all four players succeeding automatically again.
