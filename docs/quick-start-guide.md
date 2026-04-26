# Quick Start Guide

<!--
Print production notes:
- Intended as 5 letter-size reference sheets.
- Use readable body text around 10 pt or larger after layout.
- Reserve gothic/fantasy display fonts for titles and major headings; use a clearer serif or sans-serif for rules text.
- Keep strong contrast against any generated parchment, stone, ash, or gothic background texture.
-->

## Sheet 1: Setup

### Goal

Survive the quest together. If party HP reaches `0`, all players lose. At the end, each player totals prestige from treasure, claimed glory, and their secret agenda.

### Table Components

- `1` quest sheet or quest card
- escalation tracker from `0` to `10`
- red `d20` for party HP
- encounter deck
- resource / action deck
- creature deck
- secret agenda deck
- red damage tokens
- blue shield tokens
- `1` d6

### Setup

1. Place the quest where everyone can read it.
2. Set escalation to `0`.
3. Set party HP to the quest's starting HP.
4. Shuffle the encounter, resource, creature, and secret agenda decks.
5. Put damage and shield tokens within reach.
6. Leave room for the current encounter, spawned cards, discard piles, and each player's score pile.
7. Choose a fixed player order. Seat order is the default.

### Players

Each player chooses a class, then draws `1` secret agenda and keeps it hidden.

Classes are not unique.

| Class | Hand Limit | Role |
| --- | ---: | --- |
| Warrior | `6` | damage and monster kills |
| Wizard | `12` | shields and long hand planning |
| Cleric | `6` | healing and rescue support |

Starting hand:

- `4` players: each player draws `3` resource cards
- `3` players: start at `18` party HP; each player draws `4` resource cards

Players discard down to hand limit only during cleanup unless a card says otherwise.

### Escalation

Escalation runs from `0` to `10`.

| Track | Meaning |
| --- | --- |
| `0-3` | early, green zone |
| `4-6` | mid, yellow zone |
| `7-9` | late, red zone |
| `10` | final ordeal, skull zone |

At escalation `0`, begin with the quest's prep scene. If no hostile or blocking hurdles appear, the prep scene clears at the end of the round.

At escalation `10`, reveal the quest's final ordeal.

<div class="page-break"></div>

## Sheet 2: Classes

### Warrior

**Passive: Kill Reward**

When you deal the final point of damage to a monster with your own action card, creature card, or Warrior trait damage, roll `1d6`.

Draw `1` card if the result is less than or equal to:

`monster threat x rarity multiplier`

| Monster | Draw On |
| --- | --- |
| Threat 1 Common | `1` |
| Threat 2 Common | `1-2` |
| Threat 3 Common | `1-3` |
| Threat 1 Elite | `1-2` |
| Threat 2 Elite | `1-4` |
| Threat 3 Elite | `1-6` |

Common multiplier is `1`. Elite multiplier is `2`.

This passive triggers only from monster kills.

**Active**

Once per turn, deal `2` damage. If this kills a monster, it can trigger Kill Reward.

### Wizard

**Passive**

Your hand limit is `12` instead of `6`.

**Active**

Once per scene, place `2` blue shield tokens on the party or any creature.

Shield tokens prevent damage `1` for `1`. Remove shields before adding damage tokens or reducing party HP. Unused shields from this active do not carry into the next scene.

### Cleric

**Passive: Rescue**

Once per scene, when another player makes a save, you may give that roll `+1`.

If your `+1` changes a failure into a success, that player chooses `1` card they would have lost. Put that card into your hand instead of the discard pile.

The helped player chooses the card.

If multiple Clerics could claim the same transfer, only `1` transfer happens. Break the tie with a d6 roll.

**Active**

Once per scene, heal one:

- `1` party HP
- `2` HP to any creature on the field

Class passives stack unless a card or quest says otherwise.

<div class="page-break"></div>

## Sheet 3: Round And Actions

### Round Order

Each round follows this order:

1. Reveal the next encounter, or continue the current scene.
2. Resolve the encounter's `Reveal Text`.
3. Put any monsters, hazards, doors, enchantments, tests, or other named setup into play.
4. `Action Turn 1`: each player takes `1` action if able. Players choose their order.
5. `Enemy Turn 1`: each enemy monster acts from strongest to weakest. Players choose ties.
6. Standard draw: each player draws `1` card. This happens once per round.
7. `Action Turn 2`: each player takes `1` action if able.
8. `Enemy Turn 2`: each enemy monster acts again if able.
9. Resolve end of round.

If the round ends before the standard draw window, each player still takes the standard draw at round end.

If a scene clears during a round, resolve any earned reward immediately unless the card says otherwise, then finish the current round structure.

Players may still use legal action windows in non-hostile rooms or after all scene hurdles are cleared.

### Player Actions

On your action, do one meaningful thing:

- play a resource / action card
- make a basic attack for `1` damage
- use your class active
- attack with one friendly creature you control
- use a friendly creature's printed exhaust ability
- solve a non-combat test
- contribute to clearing a blocking hurdle
- claim a reward when the scene allows it

Basic attacks may target creatures and damageable blocking hurdles unless a card says otherwise.

Friendly creatures act only when a player spends an action for them or a card says otherwise.

### Enemy Behavior

Enemy monsters act from strongest to weakest.

If an enemy has a legal named active ability, it uses that instead of a normal attack unless its card says it can do both.

If an enemy attacks, it targets a legal friendly creature first. If no friendly creature is legal, it attacks the party.

### End Of Round

Resolve in this order:

1. Player-controlled round-end effects in fixed player order.
2. Monster and hostile round-end effects, strongest to weakest.
3. Encounter unresolved text and failure text.
4. Quest escalation and threshold triggers.
5. Discard down to hand limit.
6. End the round.

### Escalation Advancement

- When the party fully clears a new scene, advance escalation by `1`.
- If hostile or blocking hurdles remain at round end, escalation also rises by `1`.
- If a scene is unresolved, it does not grant the normal clear-scene advance.

<div class="page-break"></div>

## Sheet 4: Cards And Scenes

### Key Terms

- `Scene`: the current encounter, room, hazard, trader, rescue, prep beat, or ordeal.
- `Party`: all players and the shared party HP.
- `Hostile`: a monster, curse, trap, or card opposing the party.
- `Friendly`: controlled by a player or the party.
- `Blocking hurdle`: anything that prevents the scene from being cleared.
- `Clear`: remove or resolve every hostile and blocking hurdle required by the scene.
- `Claim`: place a hostile or blocking card in your score pile.
- `Own`: a card belongs to you for scoring.
- `Control`: you may use that card's effects.
- `Party-controlled`: shared by the party, not owned by one player unless a card says otherwise.
- `Discard pile`: spent, discarded, defeated, or removed cards that are not scored unless a card says otherwise.
- `Active player`: the player resolving the current action, card, trait, test, or effect.
- `Current claimant`: the player who most recently advanced a remaining hostile or blocking hurdle. If nobody qualifies, players choose.
- `Extra draw`: any draw that is not the mandatory once-per-round standard draw.
- `Support effect`: a card, trait, or ability that helps another player, prevents or reduces discard, grants a modifier, heals, or places shields without directly dealing damage.
- `Magical`: a target or effect whose card uses `magical` or is clearly magical by card type, creature type, or rules text.
- `Flying`: a flying target.
- `Exhaust`: rotate or mark a card after using an exhaust ability. Ready it at the start of the next round.
- `On hit`: resolves when an attack successfully deals at least `1` damage after shields and prevention.

### Saves And Tests

If no number is given, saves and non-combat tests succeed on `4+` on a d6.

Apply modifiers before checking success.

### Resource Cards

Resource / action cards are played from hand. If a card has a discard, sacrifice, or HP cost, pay that cost before resolving the effect.

If a resource card gives multiple options with `or`, choose one option when you play it unless the card says otherwise.

To sacrifice a card, remove a friendly card you control from the field and put it in the discard pile. Sacrificed cards are not scored unless a card says otherwise.

If a resource creates a permanent, discard the resource card after resolving it, then place the matching permanent under the control named by the card.

### Creature Cards

Use red damage tokens to track damage on surviving damageable cards. Damage removes blue shield tokens first.

When damage equals or exceeds a creature's HP, that creature is defeated and removed unless a card says otherwise.

Excess damage to a single target does not carry over to the party or another target unless a card says otherwise.

Artifacts use the creature grammar but usually have `Attack 0`. Enchantments are not combat targets unless a card says otherwise.

Summoned creatures cannot attack on the turn they are summoned unless a card says otherwise.

### Spawning By Criteria

Some encounters name exact cards. Take those named cards from the creature deck or reserve. If a required physical copy is unavailable, use a token proxy with the same name, stats, rules text, and Treasure Value.

Other encounters use criteria, such as `1 Threat 2 humanoid`.

For criteria:

1. Go through the creature deck from top to bottom once.
2. Take the first legal matches.
3. Do not sort or search multiple times unless a card says otherwise.

<div class="page-break"></div>

## Sheet 5: Trader And Scoring

### Trader Scenes

If a trader encounter reveals trader stock, reveal the top `5` resource cards.

Each player gets exactly `1` trader interaction:

- **Direct trade:** swap `1` card from your hand with `1` revealed trader card.
- **Haggle:** use the Haggle rules printed on that encounter card.

Discard unused trader stock when the scene ends.

### Claiming Cards And Rewards

When your action removes the final HP, resistance, or blocking condition from a hostile or blocking card, claim that card.

Put claimed cards in your score pile. They count for Glory Points at the end of the game.

If a reward is tied to clearing the last hurdle, the player who cleared that hurdle receives the reward unless the encounter says otherwise.

If a reward must be claimed but gives no timing, any player may spend an action to claim it once all blocking hurdles are gone.

### Final Ordeal

At escalation `10`, begin the final ordeal.

The normal two-turn round cap ends. Resolve the normal round through `Enemy Turn 2`; if the ordeal is still unresolved, keep alternating extra player turns and enemy turns without another standard draw until the ordeal resolves or the party is defeated.

### Prestige Scoring

At the end, total:

`Treasure Points + Glory Points + agenda reward`

Treasure Points:

- Treasure Value of cards in your hand
- Treasure Value of cards you own on the field

Glory Points:

- Treasure Value of hostile and blocking cards you claimed

Do not score discarded cards unless a card says otherwise. Party-controlled cards do not count for one player unless a card says otherwise.
