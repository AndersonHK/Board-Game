# Quest 003 Findings

Evidence files: [simulation log](./07-simulation-log.txt), [rulings log](./08-rulings-log.txt)

## What Held Up

- The current hand rules still look strong. Starting at `3` and capping at `6` created pressure without starving anyone, and the default draw living inside the encounter felt better than the old end-of-round refill model.
- The canon round skeleton worked across prep, hazard, combat, rescue, and climax scenes. Using the same two-turn structure everywhere made the package easier to run.
- Exact-name spawning and criteria-based spawning both worked, and the criteria scene felt meaningfully different once creature order mattered.
- Persistent obstacles and enchantments created exactly the right kind of continuity. `Clinging Miasma` and `Heavy Door` made the dungeon feel like a place instead of isolated tests.
- Creature actions once per turn mattered most in the multi-round Caged Hunt and in the escalation-10 ordeal. That rule now has real stress evidence behind it.
- The escalation-10 exception clearly improved the climax. Letting the dragon keep going beyond turn 2 was dramatically better than forcing a hard stop.

## What Broke Or Stayed Ambiguous

- Baseline quest progression is still the biggest unresolved rules gap. `defines/core-rules.md` explains unresolved escalation, but the game still needs a separate statement for how a successful descent normally advances toward tension 10.
- Mixed criteria creature searches needed an explicit procedure. The define points in the right direction, but the exact handling is still implicit.
- Creature reserve refresh is still undefined. The run had to assume that defeated non-boss creatures reset between scenes so later criteria searches stayed legible.
- Spotlight remains usable but not fully settled. The last-hurdle tie-break was good enough for execution, yet it still feels more like a tested patch than a finished scoring rule.
- The final ordeal exposed one messy damage-window edge case. The package survived it, but the mitigation timing model is still too informal.

## What Should Be Defined Next

- Add a design-level rule for baseline quest advancement toward escalation 10.
- Clarify mixed criteria creature searches in `defines/creature-deck.md`.
- Clarify whether persistent obstacles and enchantments count as blocking hurdles for unresolved escalation in the canonical rules layer.
- Clarify whether escalation-10 extra turns preserve the once-per-encounter draw rule exactly as written.
- Clarify whether creature availability is depleted across a session or refreshed between scenes.

## What Should Be Adjusted

- Tighten secret agenda thresholds. All four agendas succeeded again, which suggests the current prototype numbers are too generous.
- Keep multi-round encounters in future tests. They are the best place to expose whether hand flow, creature cadence, and blocking-hurdle escalation actually work.
- Keep using one duplicate aggressive player in 4-player sims. The rivalry between Kael and Brin still produces the clearest credit-stealing and selfish-play pressure.

## Promotion Call

- Strong candidate for promotion soon: mixed-criteria search procedure and the rule that persistent blocking cards count for unresolved escalation.
- Strong candidate to document next in design docs, but not yet canonize: baseline quest progression cadence and creature-reserve refresh.
- Not ready to promote yet: the final ordeal damage-window interpretation and the current Spotlight rule.
- No gameplay canon was promoted directly from this run. The evidence was strong on direction, but not yet clean enough to lock every patch into `defines/`.
