# Quest 001 Findings

Evidence files: [simulation log](./06-simulation-log.txt), [rulings log](./07-rulings-log.txt)

## What This Run Clarified

- The current high-level shape works: public encounter pressure, a shared survival track, small class powers, and hidden agendas all interacted cleanly in one 10-round arc ([core-concept](../../../docs/design/core-concept.md), [deck-architecture](../../../docs/design/deck-architecture.md), [round-structure](../../../docs/design/round-structure.md), ROUND-01 through ROUND-10).
- The midpoint escalation also did real work. Rounds 6 through 10 immediately felt sharper once the quest threshold turned on, which matches the intent of the tension-band and crisis notes ([round-structure](../../../docs/design/round-structure.md), [stellaris-crises research](../../../docs/research/stellaris-crises.md), RUL-03, ROUND-06).
- The biggest unresolved gap is boss structure. The dragon was numerically tense for one roll, but dramatically thin because it had no persistence beyond a single threat check ([deck-architecture](../../../docs/design/deck-architecture.md), RUL-09, ROUND-10).

## Recommendations

- Starting hand size: keep it at 3 for v1.
  The players never felt empty-handed for long, and by the midpoint the table was already floating spare options and hoarding utility. Moving straight to 4 would likely flatten early pressure too much ([class-archetypes](../../../docs/design/class-archetypes.md), ROUND-01, ROUND-02, ROUND-04, RUL-08).

- Baseline draw per round: keep 1 as the default baseline.
  One draw each round was enough to maintain agency, especially once support effects and loot cards started compounding. The real pressure problem was not starvation; it was that there was no hand cap and too many extra draws stacked on top of the baseline ([deck-architecture](../../../docs/design/deck-architecture.md), ROUND-03, ROUND-05, ROUND-09, RUL-01, RUL-08).

- HP model: use shared party HP, not per-player HP, for the first playable slice.
  Shared HP was easier to read, kept the table arguing over common risk, and made support and defensive mitigation immediately legible. It also fit the repo's stated shared survival frame better than individual health would ([core-concept](../../../docs/design/core-concept.md), ROUND-04, ROUND-06, RUL-05, RUL-06).

- Shared HP amount: lower the starting shared HP from 14 to 12 for the next pass.
  This run ended at 13 despite two failed encounters, which suggests the current buffer is too generous if cards and mitigation stay close to this strength ([round-structure](../../../docs/design/round-structure.md), ROUND-04, ROUND-06, ROUND-10, RUL-05).

- Encounter shortfall damage: keep damage equal to shortfall.
  That rule was intuitive, easy to narrate, and gave defensive play a clean job. The tuning issue looked like total party HP and mitigation volume, not the shortfall formula itself ([round-structure](../../../docs/design/round-structure.md), ROUND-04, ROUND-06, RUL-05).

- Monster HP: ordinary encounters do not need separate HP, but bosses probably do.
  Regular encounters were fine as one-number problems. The dragon was the clearest place where that model felt too flat. For the next pass, give bosses either 6 to 8 HP after the first clear or a two-stage threshold so the climax lasts at least two beats ([deck-architecture](../../../docs/design/deck-architecture.md), [stellaris-crises research](../../../docs/research/stellaris-crises.md), ROUND-10, RUL-09).

- Class powers by round 2 or 3:
  Aggressive was already loud by round 1 and slightly overtuned by round 2. Support was online by round 3 and felt healthy. Defensive mattered once damage started landing, but it was not equally visible by round 2 or 3. For the next pass, keep the aggressive passive, consider reducing Overextend from +2 to +1, keep the support kit close to this, and seed the defensive class with 1 starting Ward or an easier early trigger ([class-archetypes](../../../docs/design/class-archetypes.md), [hearthstone-hero-powers research](../../../docs/research/hearthstone-hero-powers.md), [civilization-traits research](../../../docs/research/civilization-traits-and-unique-abilities.md), ROUND-02, ROUND-03, ROUND-06, RUL-06).

## Suggested Next Numeric Pass

- Shared party HP: 12
- Starting hand: 3
- Baseline draw: 1 each round
- No per-player HP in the base mode
- Shortfall damage: unchanged
- Aggressive active: test +1 instead of +2
- Defensive class: start with 1 Ward
- Bosses: add a second phase or separate HP track

That next pass should keep the same quest skeleton and only change the numbers above, so the comparison stays clean.
