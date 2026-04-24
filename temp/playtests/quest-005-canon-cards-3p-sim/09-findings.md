# Quest 005 Findings

Evidence files: [simulation log](./07-simulation-log.txt), [rulings log](./08-rulings-log.txt), [source map](./00-source-map.md)

## What Held Up

- The three-player quickstart setup is now real. Unique-class `Warrior` / `Wizard` / `Cleric` play needed no duplicate-class patch and produced a coherent full run.
- The canonical card files are strong enough to replace the old prototype action catalog. This session mostly ran from actual quest, encounter, resource, creature, and agenda cards.
- The escalation arc felt good in practice: prep -> trader -> hazard -> carry-over curse -> rescue -> scripted boss -> hostile pressure -> final ordeal.
- Threshold 5's reward-draw tax did useful work. It made reward timing matter without adding much rules weight.
- Threshold 8's hostile-attack bump was simple but readable, and it made Kennel Vault feel meaningfully sharper than the earlier scenes.
- The Cleric passive still creates the best table drama in the system. The Causeway save flip was both tactically useful and emotionally legible.
- Dragon in the Deep again proved that the escalation-10 exception is worth keeping. The ordeal needed the third turn.

## What Broke Or Stayed Ambiguous

- Non-combat tests still lack a default target number in the player-facing rules, even though multiple cards and encounters rely on them.
- The actual agenda cards now require a clear hostile-claim procedure, but the quick start still does not teach who claims defeated hostile cards or what a claimed score pile is.
- `Current claimant` is still undefined for real humans, even though live cards already use the term.
- Summons and enchantments now need a scoring example. Without one, a table could reasonably double-count both the spell card and the resulting permanent.
- The Cleric active felt noticeably less important than the passive plus support cards in this particular run. It was usable, but rarely the best line.

## What Should Be Defined Next

- Add one short player-facing default for non-combat tests.
- Add one short player-facing hostile-claim and claimed-score-pile procedure.
- Add one prestige example that includes:
  - a claimed hostile card
  - a summon or enchantment permanent
  - a card sitting in graveyard
- Keep vertical-slice print minimums clearly labeled as minimums, not as full-game deck caps.

## What Should Be Adjusted

- Keep the threshold-5 reward tax. It was one of the cleanest pressure tools in the session.
- Keep testing real agenda cards instead of fallback Spotlight proxies. They now create better evidence, but they need clearer table procedure around them.
- Revisit the Cleric active after more runs. It was not bad, but it was usually less tempting than Battle Prayer, Mercy Prayer, or the passive rescue trigger.
- Consider whether `Prepared Beyond Reason` is slightly too easy in three-player mode once the Wizard starts at four cards and the session contains multiple draw spikes.

## Promotion Call

- Strong promotion candidate to player-facing canon: a default non-combat test target number.
- Strong promotion candidate to player-facing canon: a short hostile-claim / claimed-score-pile rule plus one prestige example.
- Strong promotion candidate to canonical wording cleanup: keep print-minimum language separate from runtime rules text.
- Worth another sim before canonizing: the exact `current claimant` procedure and any Cleric-active rebalance.
