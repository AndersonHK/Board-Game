# Quest 006 Findings

Evidence files: [simulation log](./07-simulation-log.txt), [rulings log](./08-rulings-log.txt), [source map](./00-source-map.md)

## What Held Up

- The current quickstart now carries saves, default tests, multi-round mandatory draws, and the basic enemy loop well enough for a full 3-player run.
- The "finish the round even after a clear" rule is mechanically usable and creates interesting greed windows, especially for Hidden Stash, Greedfire Vow, and other setup cards.
- Reliquary of Cinders, Shrine of Echoes, Bound Pilgrim, and Kennel Vault now form a coherent pressure arc instead of feeling like disconnected prototypes.
- The threshold package is working. Threshold 5 adds a clean tax on reward greed, threshold 8 sharpens hostile scenes without much text, and the final ordeal still feels like a real climax.
- Lyra's win was legible in table-story terms: she played long, banked permanents, stole critical last hits, and turned survival into ownership. That is good evidence for the intended "competing heroes in the same story" direction.

## What Stayed Undefined For Real Players

- The player-facing materials still do not explain who claims hostile and blocking cards for prestige.
- `Current claimant` is still undefined on live cards that already use it.
- `Active player` is still undefined in a rules set where action order is chosen by the table.
- Party-controlled versus player-owned permanents is still not taught, even though Blessing Brazier and multiple agendas make that distinction matter immediately.
- `Exhaust` still has no visible ready timing.
- Escalation 10 still lacks one explicit sequencing sentence for how the ordeal continues after the normal `Enemy Turn 2`.
- Creature copy counts are still missing from the creature layer, and Ember-Bell Nursery exposes that gap immediately.

## What This Run Suggests Should Be Adjusted Or Defined Next

- Add one short player-facing claim rule for hostile and blocking cards in the prestige section.
- Add a small glossary or wording cleanup for `current claimant` and `active player`.
- Add one prestige example that distinguishes:
  - a player-owned summon or enchantment
  - a shared party-controlled relic
  - a claimed hostile or blocking card
- Define `Exhaust` refresh timing somewhere visible to players.
- Define creature copy-count expectations or add a reserve-building note so duplicate named spawns do not require hidden assumptions.
- Clarify the escalation-10 continuation sequence with one explicit sentence so the final ordeal can be run from the quickstart alone.

## Promotion Call

- Strong candidate for player-facing canon: hostile and blocking claim procedure.
- Strong candidate for player-facing canon: ownership distinction between player-controlled and party-controlled permanents.
- Strong candidate for player-facing canon: a short glossary entry for `current claimant`, `active player`, and `Exhaust`.
- Worth another sim before promotion: whether post-clear remaining actions are producing the right amount of greed and setup value, because they were interesting here but could still skew too hard toward engine-building.

