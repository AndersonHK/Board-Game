# Quest 002 Findings

Evidence files: [simulation log](./07-simulation-log.txt), [rulings log](./08-rulings-log.txt)

## What Improved

- The prep round was a clear win. It gave players a chance to declare personality through setup choices before the dungeon started hurting them ([round-structure](../../../docs/design/round-structure.md), RUL-03, ROUND-01).
- Event scenes felt much more correct than fixed threat encounters. Merchant, causeway, shrine, rescue, ambush, vault, and boss all created different kinds of tension without needing every round to be "bigger combat math" ([core-concept](../../../docs/design/core-concept.md), [deck-architecture](../../../docs/design/deck-architecture.md), ROUND-02 through ROUND-10).
- Shared battle and non-battle action cards worked. Brin repeatedly spent scenes on future value instead of immediate help, and that generated real resentment instead of dead turns ([core-concept](../../../docs/design/core-concept.md), ROUND-03, ROUND-05, ROUND-08).
- The support save-flip rule was the standout mechanic. It created gratitude, embarrassment, debt, and card flow all at once ([class-archetypes](../../../docs/design/class-archetypes.md), RUL-05, ROUND-04, ROUND-08).
- A shared monster-and-ally entity grammar made the world feel more alive and easier to imagine ([deck-architecture](../../../docs/design/deck-architecture.md), RUL-02, ROUND-03, ROUND-09).
- Persistent cards like Clinging Miasma and Heavy Door made the dungeon feel like a place rather than a chain of sealed-off tests ([core-concept](../../../docs/design/core-concept.md), RUL-08, ROUND-05, ROUND-06, ROUND-08).
- The same event blurb scaling into different enemy cards by escalation band felt right and reusable ([round-structure](../../../docs/design/round-structure.md), ROUND-07, RUL-07).

## Recommendations

- Keep the prep round at tension 0.
  It improved pacing immediately and let personalities show up before the first punishment scene ([round-structure](../../../docs/design/round-structure.md), ROUND-01, RUL-03).

- Keep the action deck shared across battle and non-battle scenes.
  This created better selfish decisions than a simple help-or-pass model because players could invest in future glory or resources while others carried the present scene ([core-concept](../../../docs/design/core-concept.md), ROUND-03, ROUND-05, ROUND-08).

- Retire the old idea that encounter cards should have assigned threat values.
  The event-scene model produced more story, more variety, and more room for class expression than the earlier flat challenge-number approach ([deck-architecture](../../../docs/design/deck-architecture.md), [round-structure](../../../docs/design/round-structure.md), ROUND-02 through ROUND-10).

- Keep shared party HP at 12 for now.
  This run still had room for danger but no longer felt as forgiving as the 14-HP pass ([07-simulation-log.txt](./07-simulation-log.txt), ROUND-09, ROUND-10).

- Keep a hand limit.
  The cap of 6 stopped pure hoarding from taking over while still letting greedy draw lines matter ([08-rulings-log.txt](./08-rulings-log.txt), RUL-06, ROUND-05, ROUND-08).

- Bosses should use phases or separate entity stages.
  The dragon scene was more memorable the moment it stopped being one roll and became a two-beat showdown ([deck-architecture](../../../docs/design/deck-architecture.md), RUL-09, ROUND-10).

- Support should lean harder into rescue and relationship manipulation.
  The class became dramatically central whenever it changed another player's fate instead of merely adding generic efficiency ([class-archetypes](../../../docs/design/class-archetypes.md), ROUND-04, ROUND-06, ROUND-08, RUL-05).

- Design toward an auxiliary enemy or entity reserve.
  Between monsters, persistent obstacles, and enchantments, the game now wants a shared place to hold spawned scene cards without overloading the encounter deck or action deck text ([core-concept](../../../docs/design/core-concept.md), [deck-architecture](../../../docs/design/deck-architecture.md), ROUND-05, ROUND-07, ROUND-08, RUL-02, RUL-08).

## Suggested Next Pass

- Keep prep round
- Keep shared action deck
- Keep event-driven encounters
- Keep shared party HP at 12
- Keep hand limit 6
- Keep two-stage bosses
- Add one clearer rule for how Spotlight is awarded when several players contributed equally
- Prototype a small enemy or entity reserve with:
  - low / mid / high ambush enemies
  - one persistent obstacle
  - one persistent enchantment
  - two allied summons
