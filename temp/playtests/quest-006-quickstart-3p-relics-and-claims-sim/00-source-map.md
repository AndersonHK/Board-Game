# Quest 006 Source Map

This file captures the rules stack used for the sixth simulation pass. It is a reproducible session package, not canon.

Evidence files: [quest frame](./01-quest-frame.txt), [roster](./02-player-roster.txt), [agendas](./03-agendas.txt), [resource deck](./04-resource-deck.txt), [encounter deck](./05-encounter-deck.txt), [creature deck](./06-creature-deck.txt), [simulation log](./07-simulation-log.txt), [rulings log](./08-rulings-log.txt), [findings](./09-findings.md)

## Rule Priority Used For This Run

1. `defines/` is the highest-priority canon.
2. If `defines/` is silent, use the player-facing [quick start guide](../../../docs/quick-start-guide.md) because real table players only have that sheet plus cards and widgets.
3. If both of the above are silent, use current design docs only for the smallest bridge needed to keep the session moving.
4. Prior playtests are used for package structure and precedent, not for overriding live docs.

## Canon Used Directly

- Baseline hand rules, basic attacks, shield handling, turn cadence, unresolved-hurdle escalation, the escalation-10 exception, and prestige scoring defer to [defines/core-rules.md](../../../defines/core-rules.md).
- Creature-deck role, named-spawn grammar, criteria-spawn grammar, and enemy default behavior defer to [defines/creature-deck.md](../../../defines/creature-deck.md).
- The current printable card data for this run comes from [defines/cards/quest-deck/cards/ashen-depths.txt](../../../defines/cards/quest-deck/cards/ashen-depths.txt), the encounter cards under [defines/cards/encounter-deck/cards/](../../../defines/cards/encounter-deck/cards/), the resource cards under [defines/cards/resource-deck/cards/](../../../defines/cards/resource-deck/cards/), the creature/entity cards under [defines/cards/creature-deck/cards/](../../../defines/cards/creature-deck/cards/), and the agenda cards under [defines/cards/agenda-deck/cards/](../../../defines/cards/agenda-deck/cards/).

## Player-Facing Baseline From The Quick Start

- This run uses [docs/quick-start-guide.md](../../../docs/quick-start-guide.md) as the live execution sheet.
- Three-player setup uses `18` party HP and `4` starting cards per player.
- Standard rounds use two action turns, with the mandatory standard draw happening once per round between `Action Turn 1` and `Action Turn 2`.
- If a multi-round scene continues, that mandatory standard draw happens again in each later round of the same scene.
- If a scene clears during a round, the table still finishes the current round structure unless a card or quest says the scene ends immediately.
- Saves and non-combat tests without a printed number both succeed on `4+` on a `d6`.
- When a new scene is fully cleared, escalation rises by `1`.
- If hostile or blocking hurdles remain at end of round, escalation also rises by `1`.

## Supporting Design Intent Used Only When Needed

- The prep scene at escalation `0` follows [docs/design/round-structure.md](../../../docs/design/round-structure.md).
- The broader intent for selfish setup, ownership tension, and story-first rivalry only bridges gaps when needed from [docs/design/core-concept.md](../../../docs/design/core-concept.md), [docs/design/deck-architecture.md](../../../docs/design/deck-architecture.md), and [docs/design/class-archetypes.md](../../../docs/design/class-archetypes.md).

## Structure And Precedent Taken From Prior Playtests

- Folder numbering and the `00` through `09` package spine follow [Quest 005](../quest-005-canon-cards-3p-sim/00-source-map.md).
- This package keeps the proven layout of `source map -> quest frame -> roster -> agendas -> session resources -> simulation -> rulings -> findings`.
- Prior 3-player precedent mattered for organization only. Mechanical execution in this run uses the newer quickstart wording where it changed older assumptions.

## Session-Build Notes From The Live Files

- The resource card files currently sum to `72` deck copies through their `Copies In Deck` fields. This run uses that concrete count instead of the older vertical-slice minimum note.
- The current encounter folder contains `9` random encounters. This run uses all `9` as the legal shuffled random pool, even though the session reaches escalation `10` before seeing them all.
- The creature deck still lacks explicit copy counts, so encounters that require duplicate named spawns still need a small run-only reserve ruling.

## Run-Only Assumptions Needed To Execute

- Seat order for simultaneous draws is `Garrick -> Lyra -> Anwen`.
- A player may spend an action to claim a printed scene reward when the encounter text clearly implies a claimable reward but does not formalize the action.
- Hostile and blocking cards are claimed by the player whose damage or clearing action removed the final point of resistance from that card.
- Party-controlled permanents remain on the field, but they are not treated as player-owned for prestige unless a card explicitly gives one player control.
- `Current claimant` means the player currently closest to claiming the scene reward, tracked here as the player who most recently advanced any remaining hostile or blocking hurdle.
- `Exhaust` refreshes at the start of a new round.
- During the escalation-10 final ordeal, the table uses the normal round skeleton through `Enemy Turn 2`, then continues alternating extra player and enemy turns without another mandatory standard draw until the ordeal resolves or the round ends.

## What This Run Is Stress Testing

1. Whether the current quickstart plus canonical cards now support a full three-player session without leaning on outdated playtest habits.
2. Whether the newer "finish the round after a clear" rule creates readable table play or hidden setup exploits.
3. Whether live card text now gives enough information for hostile claims, blocking claims, party-owned permanents, and `current claimant` effects.
4. Whether the session can cleanly use Reliquary of Cinders, Bound Pilgrim, and Kennel Vault in one arc without collapsing into unteachable exceptions.
5. Whether agendas tied to claims, retained wealth, and owned field permanents create useful tension under the current canonical scoring model.

