# Quest 003 Source Map

This file captures the rules stack used for the third simulation pass. It is a working extraction, not a canonical rules file.

## Canon From `defines/`

- Starting hand size: `3` ([defines/core-rules.md](../../../defines/core-rules.md)).
- Hand limit: `6` ([defines/core-rules.md](../../../defines/core-rules.md)).
- Standard rounds use two action turns with one default mid-encounter draw between `Action Turn 1` and `Action Turn 2` only once per encounter ([defines/core-rules.md](../../../defines/core-rules.md)).
- If relevant hostile or blocking hurdles remain unresolved at end of round, escalation rises by `1` ([defines/core-rules.md](../../../defines/core-rules.md)).
- At escalation `10`, the normal two-turn round cap no longer applies ([defines/core-rules.md](../../../defines/core-rules.md)).
- The creature deck is a formal rules layer separate from the encounter deck and action deck ([defines/creature-deck.md](../../../defines/creature-deck.md)).
- Encounters may spawn exact named creatures or criteria-based packages, and criteria-based spawning goes through the creature deck in order to take the first valid cards ([defines/creature-deck.md](../../../defines/creature-deck.md)).
- Every creature attacks or defends once per turn unless another effect changes that ([defines/creature-deck.md](../../../defines/creature-deck.md)).

## Current Design Hypotheses From Docs

- Tension `0` should be a prep beat rather than immediate hostility ([docs/design/round-structure.md](../../../docs/design/round-structure.md)).
- Encounters are event-authored scenes, not flat threat-value cards ([docs/design/core-concept.md](../../../docs/design/core-concept.md), [docs/design/deck-architecture.md](../../../docs/design/deck-architecture.md)).
- The game should support selfish setup, rescues, and credit-stealing inside a shared survival frame ([docs/design/core-concept.md](../../../docs/design/core-concept.md)).
- The action deck should work across both battle and non-battle scenes ([docs/design/deck-architecture.md](../../../docs/design/deck-architecture.md)).
- Persistent obstacles and enchantments are in scope and likely belong beside the creature layer, even if that broader entity reserve is not formalized yet ([docs/design/core-concept.md](../../../docs/design/core-concept.md), [docs/design/deck-architecture.md](../../../docs/design/deck-architecture.md)).
- The quest still wants midpoint and climax thresholds around escalation `5` to `6` and `10` ([docs/design/core-concept.md](../../../docs/design/core-concept.md), [docs/design/round-structure.md](../../../docs/design/round-structure.md)).

## Run-Only Assumptions Needed To Execute

- Shared party HP: `12`.
- Default save: success on `4+` on a d6 unless modified.
- Spotlight: cleared scenes award `1` Spotlight, except the final ordeal which awards `2`.
- Spotlight tie-break: the player who resolves the last blocking hurdle gets the Spotlight; if resolution is genuinely inseparable, award none.
- A fully cleared new scene advances baseline quest tension by `1`.
- If blocking or hostile hurdles remain, the canonical unresolved-hurdle escalation still adds `+1`.
- Defeated non-boss creatures return to an abstract reserve between scenes, so criteria-based spawning checks the ordered creature list fresh each time.
- Mixed criteria instructions are resolved with one top-to-bottom pass through the listed creature deck order until all requested slots are filled.
- The escalation `10` exception removes the turn cap but does not grant additional default mid-encounter draws beyond the normal once-per-encounter draw.

## What This Run Is Stress Testing

1. Whether the current hand rules still feel good when the default draw happens inside the encounter rather than at end of round.
2. Whether criteria-based spawning is usable in practice once creature order matters.
3. Whether persistent blocking cards correctly count as unresolved hurdles for escalation pressure.
4. Whether creature actions once per turn create meaningful pressure in a multi-round encounter.
5. Whether the escalation `10` exception produces a satisfying climax without extra default card flow.
