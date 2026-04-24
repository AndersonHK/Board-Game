# Quest 005 Source Map

This file captures the rules stack used for the fifth simulation pass. It is a working extraction for one reproducible session, not a canonical rules file.

## Rule Priority Used For This Run

1. `defines/` is the highest-priority canon.
2. If `defines/` is silent, use the player-facing [quick start guide](../../../docs/quick-start-guide.md) because real table players only have that sheet plus cards and widgets.
3. If both of the above are silent, use current design docs only for the smallest bridge needed to keep the session moving.
4. Prior playtests are used for package structure and precedent, not for overriding live docs.

## Canon From `defines/`

- Baseline hand rules, basic attacks, shield handling, unresolved-hurdle escalation, the escalation-10 exception, and prestige scoring all defer first to [defines/core-rules.md](../../../defines/core-rules.md).
- The creature-deck layer, named-spawn grammar, criteria-spawn grammar, and creature-turn cadence defer to [defines/creature-deck.md](../../../defines/creature-deck.md).
- The canonical printable card data for this run comes from [defines/cards/quest-deck/cards/ashen-depths.txt](../../../defines/cards/quest-deck/cards/ashen-depths.txt), the encounter cards under [defines/cards/encounter-deck/cards/](../../../defines/cards/encounter-deck/cards/), the resource cards under [defines/cards/resource-deck/cards/](../../../defines/cards/resource-deck/cards/), the creature/entity cards under [defines/cards/creature-deck/cards/](../../../defines/cards/creature-deck/cards/), and the agenda cards under [defines/cards/agenda-deck/cards/](../../../defines/cards/agenda-deck/cards/).

## Player-Facing Baseline From The Quick Start

- This run uses the player-facing teach sheet in [docs/quick-start-guide.md](../../../docs/quick-start-guide.md) as the default execution surface.
- Three-player setup uses `18` party HP and `4` starting cards per player.
- The live class text is the quick-start wording for `Warrior`, `Wizard`, and `Cleric`, including:
  - `Warrior` active deals `2` damage once per turn.
  - `Wizard` active places `2` shield tokens once per scene.
  - `Cleric` active heals `1` party HP or `2` HP to any creature once per scene.
- Standard rounds still use two action turns with one default mid-encounter draw only once per encounter.
- Clearing a new scene raises escalation by `1`.
- Leaving hostile or blocking hurdles unresolved at end of round also raises escalation by `1`.

## Supporting Design Intent Used Only When Needed

- The prep scene at escalation `0` follows the design intent in [docs/design/round-structure.md](../../../docs/design/round-structure.md).
- Scene authorship, selfish setup, and support-for-profit behavior defer only when needed to [docs/design/core-concept.md](../../../docs/design/core-concept.md) and [docs/design/deck-architecture.md](../../../docs/design/deck-architecture.md).

## Structure And Precedent Taken From Prior Playtests

- Folder numbering and the `00` through `09` package spine follow [Quest 004](../quest-004-quickstart-4p-sim/00-source-map.md).
- This run keeps the older simulation format of `source map -> quest frame -> roster -> agendas -> session resources -> simulation -> rulings -> findings`, but it replaces the older prototype action catalog with concrete session deck resources because the repo now has canonical card files.

## Vertical-Slice Scope Note Clarified After This Run

- The earlier apparent count mismatches were a scope-language problem, not a mechanical rules conflict.
- `8` random encounters and `64` action cards are vertical-slice printable minimums.
- The full game's encounter deck can be larger, and the full action deck may eventually grow much larger as well.

## Run-Only Assumptions Needed To Execute

- This run uses an `8`-encounter random stack as one legal vertical-slice session build, not as a claim that the final full encounter library is capped at `8`.
- Resource-deck copy counts in the live card files are treated as this session's working build, while the older `64`-card note is treated as a vertical-slice print minimum rather than a full-deck ceiling.
- Action order inside each action turn is chosen by the table.
- If a non-combat test is required and no target number is printed, succeed on `4+` on a `d6`.
- Exact-name creature spawns search the creature reserve for the named cards without changing the ordered criteria-spawn pass used later in the same session.
- When a hostile card is defeated, the player who dealt the final point of damage claims it into a personal score pile.
- For scorekeeping, a summon or enchantment resource card that creates a matching entity is treated as that entity for endgame counting so the session does not score both the spent spell card and the spawned permanent.
- If a scene effect refers to the `current claimant`, use the player currently closest to the scene reward, defined for this run as the player who most recently advanced the last remaining hostile or blocking hurdle.
- For the threshold-5 smoke rule, if multiple reward draws would happen together, the player who triggered or cleared the reward is treated as the first player to gain that extra reward draw.

## What This Run Is Stress Testing

1. Whether the current quickstart plus canonical cards are enough to run a real three-player session without hidden design memory.
2. Whether the newly canonical card files are usable enough to replace the older prototype action pool during simulation.
3. Whether the actual agenda cards can now support a prestige-scored session instead of the older Spotlight proxy.
4. Whether claim-based hostile scoring, summoned permanents, and reward-draw taxes are understandable from player-visible materials.
5. Whether the three-player setup remains stable once the run uses the actual Ashen Depths card suite rather than the older provisional package.
