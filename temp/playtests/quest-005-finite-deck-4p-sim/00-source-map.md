# Quest 005 Source Map

This file records the exact rules stack used for the fifth simulation pass. It is a working session document, not canon.

Evidence files: [quest frame](./01-quest-frame.txt), [roster](./02-player-roster.txt), [agendas](./03-agendas.txt), [resource deck](./04-resource-deck.txt), [encounter deck](./05-encounter-deck.txt), [creature reserve](./06-creature-deck.txt), [simulation log](./07-simulation-log.txt), [rulings log](./08-rulings-log.txt), [findings](./09-findings.md)

Historical note:
- This run predates the later canon clarification that the standard draw is mandatory once per round and that every player and enemy monster acts in each turn if able.
- Read this package as evidence from an older timing model, not as the current round-sequencing template.

## Rule Priority Used For This Run

1. `defines/` is the highest-priority canon.
2. If `defines/` is silent or player execution would clearly depend on a visible teaching document, defer next to the [quick start guide](../../../docs/quick-start-guide.md) because real players only have that sheet plus cards and widgets.
3. If both are silent, use current design docs for the smallest intent-bridge needed to continue.
4. Prior playtests are used for package structure and precedent, not to override the current docs.

## Canon Used Directly

- Baseline hand rules, turn structure, basic attacks, shield timing, stacking-passive rule, escalation timing, and prestige structure came from [defines/core-rules.md](../../../defines/core-rules.md).
- Creature-deck role and criteria-spawn procedure came from [defines/creature-deck.md](../../../defines/creature-deck.md).
- Quest, encounter, resource, creature, and agenda card text came from the card files under [defines/cards/](../../../defines/cards/README.md).
- The player-facing execution layer came from [docs/quick-start-guide.md](../../../docs/quick-start-guide.md).

## Session-Build Conflicts Found Inside The Live Docs

- The resource-deck README says the deck is `64` cards, but the explicit `Copies In Deck` values in the resource card files sum to `72`.
- The encounter-deck README and quest card say the quest uses `8` random encounters, but the encounter card files currently contain `9` random encounter definitions.
- The creature card files define unique cards, but at least one encounter (`Ember-Bell Nursery`) requires duplicate named spawns, so creature copy counts are still not fully specified by canon.

## Conflict Handling Used For This Run

- The resource deck for this session uses the concrete `72` cards implied by the card-file copy counts because those are the most specific printable values currently present.
- The encounter deck for this session uses `8` random encounters to match the quest card, leaving one legal random encounter file unused in this run.
- The creature reserve for this session uses one copy of each unique definition plus one extra `Ember Bat` instance because a live encounter explicitly asks for two of them.

## Quickstart-First Execution Lens

This run was written from the perspective of what a real four-player table could execute with:

- the quick-start sheet
- the printed card text
- the quest/session sheet for this playtest
- the table widgets

Any procedure a human table would still need but could not learn from those materials was logged in [08-rulings-log.txt](./08-rulings-log.txt).

## Run-Only Assumptions

- Draw order for simultaneous card draws uses seat order: `Kael -> Brin -> Mira -> Tamsin`.
- Once a scene is fully cleared, the scene ends immediately and any unused later steps in that round are skipped.
- Non-combat tests without printed target numbers use the quick-start default success number of `4+` on a `d6`.
- Hostile and blocking cards are claimed for `Glory Points` when a player delivers the final damage or performs the final clearing action needed to remove them.
- The final ordeal begins only after the current scene fully ends if escalation reaches `10` mid-scene.

## What This Run Was Stress Testing

1. Whether the current canon can support a real finite-deck session instead of the older prototype action catalog.
2. Whether quick-start-only players could actually execute score-pile, claim, scene-ending, and non-combat-test procedures without hidden designer knowledge.
3. Whether the current quest and deck files are internally consistent enough to assemble one printable session package without guessing at counts.
4. Whether the midpoint and final fights still function when the resource deck is treated as a real shuffled deck with visible scarcity.
5. Whether the current agenda set produces mixed success rates once real score piles and on-card Treasure Value are used.
