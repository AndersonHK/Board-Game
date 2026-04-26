# Quest 007 Source Map

This file captures the rules stack used for the seventh simulation pass. It is a reproducible session package, not canon.

Evidence files: [quest frame](./01-quest-frame.txt), [roster](./02-player-roster.txt), [agendas](./03-agendas.txt), [resource deck](./04-resource-deck.txt), [encounter deck](./05-encounter-deck.txt), [creature deck](./06-creature-deck.txt), [simulation log](./07-simulation-log.txt), [rulings log](./08-rulings-log.txt), [findings](./09-findings.md)

## Rule Priority Used For This Run

1. `defines/` is the highest-priority canon.
2. If `defines/` is silent, use the player-facing [quick start guide](../../../docs/quick-start-guide.md), because real table players only have that guide plus cards and widgets.
3. If both of the above are silent, use current design docs only for the smallest bridge needed to keep the session moving.
4. Prior playtests are used for package structure and precedent, not for overriding live docs.

## Canon Used Directly

- Baseline hand rules, fixed player order, table widgets, standard round flow, claiming, scoring, `current claimant`, `active player`, `Exhaust`, escalation, saves, and final-ordeal timing defer to [defines/core-rules.md](../../../defines/core-rules.md).
- Creature-deck role, exact-name spawning, criteria spawning, enemy default behavior, friendly creature targeting, and summon sickness defer to [defines/creature-deck.md](../../../defines/creature-deck.md).
- The live printable card data comes from [defines/cards/quest-deck/cards/ashen-depths.txt](../../../defines/cards/quest-deck/cards/ashen-depths.txt), [defines/cards/encounter-deck/cards/](../../../defines/cards/encounter-deck/cards/), [defines/cards/resource-deck/cards/](../../../defines/cards/resource-deck/cards/), [defines/cards/creature-deck/cards/](../../../defines/cards/creature-deck/cards/), and [defines/cards/agenda-deck/cards/](../../../defines/cards/agenda-deck/cards/).

## Player-Facing Baseline From The Quick Start

- This run treats [docs/quick-start-guide.md](../../../docs/quick-start-guide.md) as the live teaching sheet.
- Three-player setup uses `18` party HP and `4` starting cards per player.
- Players use Warrior, Wizard, and Cleric, with their quickstart passive and active traits.
- Standard rounds use two action turns and one mandatory standard draw between `Action Turn 1` and `Action Turn 2`.
- Multi-round scenes get the mandatory standard draw once each round.
- If a scene clears during a round, finish the current round structure unless a card or quest says the scene ends immediately.
- Saves and non-combat tests without a printed number succeed on `4+` on a `d6`.
- Claiming, ownership, party-controlled cards, and prestige scoring use the quickstart's current wording.

## Supporting Design Intent Used Only When Needed

- The prep scene at escalation `0` is interpreted with help from [docs/design/round-structure.md](../../../docs/design/round-structure.md), because the quest says a prep scene happens but does not provide a dedicated prep encounter card.
- The broader intent for selfish setup, ownership tension, and story-first rivalry only bridges gaps when needed from [docs/design/core-concept.md](../../../docs/design/core-concept.md), [docs/design/deck-architecture.md](../../../docs/design/deck-architecture.md), and [docs/design/class-archetypes.md](../../../docs/design/class-archetypes.md).

## Structure And Precedent Taken From Prior Playtests

- Folder numbering and package spine follow [Quest 006](../quest-006-quickstart-3p-relics-and-claims-sim/00-source-map.md).
- This package keeps the proven layout of `source map -> quest frame -> roster -> agendas -> session resources -> simulation -> rulings -> findings`.
- Prior playtests inform formatting and logging discipline only. Mechanical execution uses the current defines and quickstart.

## Session-Build Notes From The Live Files

- The resource card files sum to `72` deck copies through their `Copies In Deck` fields. This run uses that concrete count.
- The random encounter folder contains `9` random encounters. This run scripts a plausible shuffled order from that pool to stress hazards, trader timing, carried enchantments, criteria spawning, and the finale.
- The creature deck copy-count rule now exists canonically, so duplicate named spawns use the common/elite copy-count baseline rather than an ad-hoc reserve.

## Run-Only Assumptions Needed To Execute

- Fixed player order is `Merek -> Selene -> Oren`.
- The escalation-0 prep scene is one normal round with no hostile or blocking hurdles; it clears at end of round.
- `Graveyard` on Smoke-Flood Gallery means the discard pile.
- The threshold-5 tax applies only to extra draws from encounter Reward Text, not to normal resource-card draws, trader exchanges, or Shrine of Echoes bargain draws.
- Shrine of Echoes can end with Ash Miasma carried into the next scene when its bargain is resolved and Ash Miasma remains, because the card's failure text explicitly describes that carry-over behavior.
- The agenda phrase `shared-success moments` means a support effect that directly changes or enables a successful save, kill, clear, or survival result.

## What This Run Is Stress Testing

1. Whether the current quickstart plus canonical cards can run a three-player session when the encounter order leans into hazards and social scenes instead of mostly combat.
2. Whether real players can understand prep, trader, reward-draw tax, and carried-over Ash Miasma from the quickstart and cards alone.
3. Whether the Warrior still finds enough claims when friendly summons absorb enemy attacks and non-combat scenes occupy multiple rounds.
4. Whether the Wizard's hand limit and owned permanents remain a strong but teachable scoring route.
5. Whether the Cleric agenda and support moments are concrete enough to evaluate without designer interpretation.
