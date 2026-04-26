# Deferred Doc Comparison

This pass happened only after the printed-materials simulation and findings were complete.

Deferred materials inspected:

- `defines/core-rules.md`
- `defines/creature-deck.md`
- `defines/cards/README.md`
- `defines/card-layout.md`
- `docs/project-memory.md`
- `docs/repository-directory.md`
- `docs/design/`
- `docs/research/`
- prior folders under `temp/playtests/`

## Already Defined Outside The Printed Package

- Default non-combat tests: `defines/core-rules.md` already says saves and non-combat tests with no number succeed on 4+.
- Claiming: `defines/core-rules.md` already says the player whose action removes the final HP, resistance, or blocking condition from a hostile or blocking card claims it.
- Rewards with no timing: `defines/core-rules.md` already says any player may spend an action to claim a reward after all blocking hurdles are gone.
- Criteria spawns: `defines/creature-deck.md` already defines one top-to-bottom creature-deck pass and proxy behavior.
- Enemy active abilities: `defines/creature-deck.md` already says enemies use legal named active abilities and high-threat bosses may use an active and still attack when their card says so.
- Friendly creature targeting: `defines/creature-deck.md` already says enemies attack legal friendly creatures before the party.
- Exhaust refresh: `defines/core-rules.md` and `defines/creature-deck.md` already say exhausted cards ready at the start of each new round.
- Final ordeal cadence: `defines/core-rules.md` already defines the normal round through Enemy Turn 2, then alternating extra player turns and enemy turns with no additional standard draw.
- Prep scene procedure: `docs/design/round-structure.md` defines the procedure the table improvised: run one normal non-hostile round, allow legal setup actions, clear at end of round if no hurdles appear, then raise escalation.

## Defined Outside Print In A Way That Would Change This Run

- Shield persistence: `defines/core-rules.md` says shield tokens do not persist between scenes unless a card or quest says otherwise. The printed quickstart only says this for the Wizard active, so the table inferred that `Warding Circle` shields could accumulate across scenes. That inflated party durability in this simulation.

## Still Missing Or Unclear After Deferred Reading

- d3 conversion is still not defined, despite Heartfire Dragon using `1d3`.
- Party HP maximum is still not in the core rules or quickstart. The print manifest flags it as a package gap and recommends capping at starting HP.
- Enemy target choice among multiple legal friendly creatures is still not explicit.
- Starting hand dealing order is still not explicit.
- Trader interaction timing is still not explicit: action or free scene interaction.
- Discard selectors are still inconsistent: many effects say discard or lose cards without saying who chooses.
- Obstacles need a clearer printed grammar for when players use HP damage, automatic actions, or non-combat tests.
- Threshold 5 is mostly defined, but simultaneous encounter reward draws still need a printed example or tie rule.
- `Current claimant` exists, but multi-hurdle scenes still make it easy to lose track without stronger physical instructions.

## Prior Playtest Alignment

- Prior Quest 006 and Quest 007 already identified much of the same teachability pressure: prep scene procedure, threshold-5 scope, Shrine/Miasma carry-over, final-ordeal sequencing, current claimant tracking, reward timing, and support-agenda examples.
- The earlier `2026-04-26-printed-only-3p-sim` folder independently reached many of the same printed-package conclusions, including d3, shield persistence, enemy target choice, reward recipient language, and threshold timing.
- Several prior issues have since been promoted into the quickstart, but this run shows that rules can still fail at the table when they are split between quickstart, card text, widget notes, and non-printed defines.

## Final Takeaway

The printed package is enough to finish a 3-player game with a cooperative, rules-literate table that is willing to make small rulings. It is not yet enough for a clean unsupervised printed-materials-only playtest. The remaining fixes should focus less on adding new systems and more on relocating existing rulings into the quickstart or onto the cards that trigger them.
