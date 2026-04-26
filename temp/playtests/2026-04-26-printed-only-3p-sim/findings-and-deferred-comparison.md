# Findings And Deferred Comparison

Status: playtest completed from printed materials first. Deferred-doc comparison completed afterward.

## Printed Package Taught Well

- Setup components were easy to identify: quest, decks, HP die, escalation meter, dice, tokens, score piles, and player areas.
- The 3-player HP and hand adjustments were visible on both the quick-start and quest card.
- The round structure was strong enough to run scenes, standard draws, enemy turns, and end-of-round escalation.
- Damage, shields, defeat, claiming, hand limit, and final scoring were mostly discoverable from the quick-start.
- Card text generally carried scene-specific play well, especially exact spawns and simple rewards.
- The final ordeal rule was enough to keep the endgame moving after the normal two action turns.

## Printed Package Failed Or Struggled To Teach

- The prep scene is referenced but not physically defined. Players had to invent what they could do and when it cleared.
- Starting hand dealing order is not specified.
- Enemy targeting says enemies target legal friendly creatures first, but does not say who chooses among multiple legal friendly creatures.
- Shield persistence is not fully explicit except for the Wizard active, which creates uncertainty for `Warding Circle` shields.
- Multiple ongoing prevention effects, especially `Prepared Ground`, need an explicit stacking rule.
- Rewards that say `active player`, `resolver`, or no recipient at all are inconsistent. `Smoke-Flood Gallery` and `Shrine of Echoes` required table rulings.
- `Current claimant` is defined, but it is still hard to maintain during multi-hurdle scenes with damage, tests, claims, and enemy-triggered discards.
- Threshold 5 needs a clearer timing example. It was unclear whether `Furnace Warden Rises` is the first taxed scene.
- `Ash Miasma` has both scene-end text and hostile/enchantment behavior, but its claimability and carry-forward cleanup are unclear.
- `d3` is printed on `Heartfire Dragon`, but the package only gives the table a d6 and does not define d3 conversion.
- `Dragon in the Deep` says to ignore the two-turn round cap, while the quick-start says resolve the normal round first and then alternate extra player/enemy turns. The latter worked, but the encounter card alone is less specific.
- Summon resources outnumber matching creature cards. The package says proxies may be used, but the moment of proxy use is still awkward for players.

## Suggested Later Adjustments

- Add a printed prep scene card or a concise prep-scene box to the quest.
- Add a small `Table Defaults` box: dealing order, enemy target choice, d3 conversion, shield persistence, HP maximum, and stacking.
- Normalize reward recipient language across encounters.
- Add one printed threshold timing example for escalation 5, 8, and 10.
- Add a physical tracking convention for once-per-scene, first hostile attack each scene, threshold tax, and current claimant.
- Clarify whether removing a hostile enchantment with dispel counts as claiming it.
- Clarify whether dragons count as magical for targeting.

## Deferred-Doc Comparison

After the run, I read the deferred non-printed rules/design docs and prior playtest folders.

Already defined outside the printed package:

- Prep scene procedure: `docs/design/round-structure.md` defines the exact procedure we improvised: run one normal non-hostile round, allow legal setup actions, clear at end of round if no hurdles appear, then raise escalation. Prior Quest 007 also identified this as needing a printed procedure or card.
- Final ordeal continuation: `defines/core-rules.md` already defines the sequence we used: resolve the normal round through `Enemy Turn 2`, then alternate extra player turns and enemy turns with no additional standard draw.
- Exact and criteria spawns: `defines/creature-deck.md` defines exact-name spawns through the reserve, criteria spawns by one top-to-bottom pass, and proxy behavior when copies run out.
- Reward timing and claiming: `defines/core-rules.md` already has the broad rules for claiming hostile/blocking cards, immediate reward resolution, and reward-claim actions.
- Scoring ownership: `defines/core-rules.md` distinguishes hand Treasure, owned field Treasure, claimed Glory, and party-controlled cards.
- Exhaust refresh: `defines/core-rules.md` and `defines/creature-deck.md` both say exhausted cards ready at the start of each new round.
- HP maximum: the print bundle flags this as an open package gap and recommends party HP not exceed starting HP, but this is not yet fully promoted into the quick-start.

Defined outside print in a way that would have changed this run:

- Shield persistence: `defines/core-rules.md` says shield tokens do not persist between scenes unless a card or quest says otherwise. The printed quick-start only says the Wizard active shields do not carry, so the table inferred `Warding Circle` shields could bank across scenes. That inflated late-game shields and should be fixed in print.

Still unclear or not fully defined even after deferred reading:

- Starting hand dealing order is still not specified.
- Enemy target choice among multiple legal friendly creatures is still not explicit.
- Non-class stacking, especially multiple `Prepared Ground` copies, is not defined.
- `d3` conversion is still not defined.
- `Shrine of Echoes` still has the same carry-over/clear-condition knot noted in Quest 007.
- Reward recipients remain inconsistent on cards like `Smoke-Flood Gallery` and `Shrine of Echoes`.
- Whether removing `Ash Miasma` by dispel grants a Glory claim is inferable from the claim rule but not explicitly exampled.
- Whether dragons count as magical for `Arc Bolt` remains a judgment call under the current `magical` definition.

Prior playtest alignment:

- Quest 006 and Quest 007 already found many of the same printed-teachability issues: prep scene, threshold-5 scope, Shrine carry-over timing, final-ordeal sequencing, current claimant tracking, reward timing, and support/agenda examples.
- Some of those issues have since been promoted into the quick-start, but this printed-only run shows the remaining problem is not only absence. Some rules are present but still too distributed or too terse for a table under pressure.
