# Quest 007 Findings

Evidence files: [simulation log](./07-simulation-log.txt), [rulings log](./08-rulings-log.txt), [source map](./00-source-map.md)

## What Held Up

- The current quickstart now carries the core loop well: setup, saves, basic attacks, class actives, claims, ownership, current claimant, active player, exhaust refresh, and final-ordeal continuation were all executable.
- The hazard/trader-heavy sequence still produced a full story arc. The game did not need constant combat to create pressure.
- Friendly creature targeting is doing useful work. Cinder Familiar and Tin Golem created memorable protection moments without needing a separate tanking subsystem.
- The Warrior and Wizard scoring routes were both live. Merek built a huge Glory pile, while Selene still won narrowly through retained Treasure and owned permanents.
- The threshold package continued to work. Threshold 5 created a real question around reward greed, threshold 8 made late hostile attacks matter, and escalation 10 produced a tense but survivable climax.

## What Stayed Undefined For Real Players

- The escalation-0 prep scene still needs a printed procedure or card. The quest says it exists, but not exactly what players may do or when it clears.
- Smoke-Flood Gallery uses `graveyard`, while the quickstart teaches discard language.
- Ashen Depths' threshold-5 tax needs a clearer scope. Players will ask whether Shrine bargains, Trader Haggle, Hidden Stash, Warrior passive draws, and encounter rewards are all the same kind of extra draw.
- Shrine of Echoes has a real rules knot: Ash Miasma both blocks clearing and has text about remaining for the next scene.
- By My Grace uses `shared-success moments`, which is evocative but not mechanically defined enough for scoring.
- Post-clear reward timing is playable, but repeated reward text would benefit from one default sentence about whether rewards resolve immediately or at end of round.
- Excess damage against friendly creature targets should be clarified if the design wants any spillover or no spillover.

## What This Run Suggests Should Be Adjusted Or Defined Next

- Add a tiny prep-scene rule or actual prep encounter card for Ashen Depths.
- Replace `graveyard` with `discard pile` on Smoke-Flood Gallery.
- Clarify the threshold-5 tax as either:
  - only encounter Reward Text draws, or
  - every extra draw except the mandatory standard draw.
- Rewrite Shrine of Echoes so its carry-over mode explicitly overrides normal scene clearing, or make Ash Miasma remain only after the scene is otherwise cleared.
- Rewrite By My Grace with concrete countable triggers, such as "support effects that change a failed save to success, add the final needed damage, prevent lethal party damage, or clear the final blocking test."
- Consider adding a default reward timing sentence to the quickstart: when a reward condition is met, resolve the reward immediately unless the card says otherwise.
- Add one creature-damage example that says whether excess damage to a friendly creature carries over to the party.

## Balance And Feel Notes

- Selene's Wizard route may be slightly too efficient when `12` hand limit, Greedfire Vow, and post-clear action windows all line up. It was fun here, but it nearly beat a Warrior who claimed the dragon and multiple elites.
- Merek's Warrior passive felt exciting without dominating because Selene and Oren could still take important final hits.
- Oren's support identity felt good during play, but his agenda scoring required designer interpretation. That is the biggest gap for his route.
- The party finished with `10` HP, so this encounter order was less lethal than Quest 006 despite several errors and greedy choices. More red-zone pressure may be needed if human players optimize even mildly.

## Promotion Call

- Strong candidate for player-facing canon: prep-scene procedure for escalation `0`.
- Strong candidate for card cleanup: `graveyard` -> `discard pile`.
- Strong candidate for quest wording: threshold-5 reward-draw tax scope.
- Strong candidate for encounter rewrite: Shrine of Echoes carry-over timing.
- Strong candidate for agenda rewrite: By My Grace `shared-success moments`.
- Worth another human or simulated test before numeric adjustment: Wizard Treasure scoring versus Warrior Glory scoring under the current hand limit and post-clear action rule.
