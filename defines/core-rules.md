# Core Rules Defines

This file records canonical baseline rules for table play.

## Hand Rules

- Starting hand size: `3` cards.
- Hand limit: `6` cards.

## Player Order

- Before the first round, choose a fixed player order.
- Use table or seat order by default.
- If table or seat order is unclear, players choose the order once before play begins.
- Whenever rules say to resolve effects in player order, use this fixed order.

## Table Tracking

- Party health is tracked with a red `d20`.
- Damage tokens are small red circles placed on a creature or other damageable card when it takes damage and survives.
- Damage tokens track damage already dealt.
- Shield tokens are blue.
- Shield tokens are removed before damage tokens are added or party HP is lost.
- Shield tokens prevent damage `1` for `1` and do not persist between scenes unless a card or quest says otherwise.

## Core Terms

- A `scene` is the current encounter, prep room, ordeal, hazard, trader, rescue, or other room being resolved.
- A `round` is one full pass through the standard round structure.
- The `party` means all players together and the shared party HP total.
- A `hostile` card is an enemy, curse, trap, or other card opposing the party.
- A `friendly` card is controlled by a player or by the party.
- A `blocking hurdle` is any hostile or other card, test, hazard, door, restraint, enchantment, or condition that prevents the scene from being fully cleared.
- To `clear` a scene, remove or resolve every hostile and blocking hurdle required by that scene.
- To `claim` a card, place it in a personal score pile for Glory Points.
- To `own` a card or permanent means it belongs to that player for scoring.
- To `control` a card or permanent means that player or the party may use its effects.
- A `party-controlled` card is shared by the party and is not owned or scored by one player unless a card says otherwise.
- A `discarded` card is no longer in hand or on the field and is not scored unless a card says otherwise.
- The `active player` is the player currently resolving an action, card, trait, test, or effect.
- The `current claimant` is the player who most recently advanced a remaining hostile or blocking hurdle in the current scene. If no player qualifies, players choose the current claimant.
- An `extra draw` is any card draw that is not the mandatory standard draw once per round.
- A `support effect` is a card, class trait, or creature ability that helps another player, prevents or reduces a discard, grants a modifier, heals, or places shield tokens without directly dealing damage.
- A `magical` target or effect is one whose card uses the word `magical` or whose card type, creature type, or rules text clearly marks it as magical.
- `Flying` means the card is a flying target.
- To `exhaust` a card, rotate or mark it after using an exhaust ability. Exhausted cards ready at the start of each new round.

## Actions

- On a normal action, a player may play a card, use a class active, take a non-combat scene action, or make a basic attack.
- If a played card has a discard, sacrifice, HP, or other printed cost, pay that cost before resolving the card's effect.
- If a played card gives multiple options with `or`, choose one option when playing it unless the card says otherwise.
- Every class may make a basic attack for `1` damage instead of playing a card or using a class active.
- Basic attacks may target creatures and other damageable blocking cards unless that card says it cannot be targeted by combat.
- Enchantments are not combat targets by default because they do not use HP and attack values unless a card or quest says otherwise.
- A player may spend an action to attack with one friendly creature they control if that creature can attack.
- Friendly summoned creatures cannot attack on the turn they are summoned and do not take independent full turns unless a card says otherwise.
- A player may use a friendly creature's printed exhaust ability at its allowed timing. If no timing is printed, use it during that player's action.
- When a player plays a resource card that creates a permanent, discard the resource card after resolving it, then place the matching permanent under the stated control.

## Standard Round Structure

A standard round uses two action turns.

1. Reveal or continue the current scene.
2. `Action Turn 1`: every player takes `1` action if able, unless a card, class ability, or scene effect changes that. The players choose their own order.
3. `Enemy Turn 1`: every enemy monster takes `1` action if able. Resolve enemy monsters from strongest to weakest. If there is a toss-up, the players choose that order.
4. Standard draw: each player draws `1` card between `Action Turn 1` and `Action Turn 2`. This standard draw is mandatory once per round.
5. `Action Turn 2`: every player takes `1` action if able, unless changed by card effects, class abilities, or scene effects. The players choose their own order.
6. `Enemy Turn 2`: every enemy monster takes `1` action if able. Resolve enemy monsters from strongest to weakest. If there is a toss-up, the players choose that order.
7. End of round: resolve round-end effects, unresolved text, escalation, and cleanup in the end-of-round order.

If a round ends before the normal standard-draw window is reached, each player still makes that mandatory standard draw as the round ends.
If a scene is fully cleared during a round, finish the current round structure unless a card or quest says the scene ends immediately.
Players may still use action windows in non-hostile rooms or after all scene hurdles are cleared.

## End Of Round Order

1. Players resolve player-controlled round-end effects in fixed player order.
2. Monsters and hostile cards resolve round-end effects in monster order, strongest to weakest. If there is a tie, players choose the order.
3. The encounter resolves unresolved text and failure text.
4. The quest resolves escalation changes and threshold triggers.
5. Players discard down to hand limit.
6. The round ends.

## Class Passive Stacking

- Class passives stack by default unless a card, class rule, or quest says otherwise.
- If multiple copies of the same passive could claim the same one-time card transfer or loot event, resolve only one transfer unless the effect says otherwise.
- If more than one player is eligible for that one transfer, break the tie with a `d6` roll among the eligible players.

## Escalation And Unresolved Hurdles

- If the party does not clear all relevant hostile or blocking hurdles by the end of a standard round, escalation rises by `1`.
- Round-end effects from cards are triggered.
- If a scene is fully cleared, advance escalation by `1` when the quest resolves escalation changes unless a card or quest says otherwise.

## Escalation 10 Exception

- At escalation `10`, the normal two-turn round cap no longer applies.
- The final ordeal continues without a standard turn limit until the scene is resolved or the party is defeated.
- Resolve the normal round through `Enemy Turn 2`.
- If the final ordeal remains unresolved after `Enemy Turn 2`, continue alternating extra player turns and enemy turns without another standard draw until the ordeal resolves or the party is defeated.

## Saves And Tests

- If a save or non-combat test is required and no other number is given, it succeeds on `4+` on a `d6`.
- Apply modifiers before checking success.

## Claiming Cards And Rewards

- When a player's action removes the final HP, resistance, or blocking condition from a hostile or blocking card, that player claims that card.
- Claimed cards go into that player's personal score pile.
- If a scene reward is tied to clearing the last hurdle, the player who cleared that hurdle receives the reward unless the encounter says otherwise.
- If a card says a reward must be claimed but gives no timing, any player may spend an action to claim that reward once all blocking hurdles are gone.
- Party-controlled cards are not claimed or scored by one player unless a card says otherwise.

## Prestige Scoring

- Endgame scoring uses `prestige points`.
- Each scored card has a `Treasure Value`.
- `Treasure Points` are the Treasure Value of cards in that player's hand plus the Treasure Value of cards that player owns on the field.
- `Glory Points` are the Treasure Value of hostile and blocking cards that player claimed during the run.
- A resource card that created a permanent is not scored from the discard pile. Score only the resulting permanent if that player owns it on the field at the end of the game.
- Party-controlled cards do not count as one player's Treasure Points unless a card says otherwise.
- A player's prestige total is the sum of:
  - that player's Treasure Points
  - that player's Glory Points
  - that player's agenda reward
