# Core Rules Defines

This file records canonical baseline rules that are now firm enough to use outside temporary playtests.

## Hand Rules

- Starting hand size: `3` cards.
- Hand limit: `6` cards.

## Table Tracking

- Party health is tracked with a red `d20`.
- Damage tokens are small red circles placed on a creature or other damageable card when it takes damage and survives.
- Damage tokens track damage already dealt.
- Shield tokens are blue.
- Shield tokens are removed before damage tokens are added or party HP is lost.
- Shield tokens prevent damage `1` for `1` and do not persist between scenes unless a card or quest says otherwise.

## Actions

- On a normal action, a player may play a card, use a class active, take a non-combat scene action, or make a basic attack.
- Every class may make a basic attack for `1` damage instead of playing a card or using a class active.
- Basic attacks may target creatures and other damageable blocking cards unless that card says it cannot be targeted by combat.
- Enchantments are not combat targets by default because they do not use HP and attack values unless a card or quest says otherwise.

## Standard Round Structure

A standard round uses two action turns.

1. Reveal or continue the current scene.
2. `Action Turn 1`: every player takes `1` action if able, unless a card, class ability, or scene effect changes that. The players choose their own order.
3. `Enemy Turn 1`: every enemy monster takes `1` action if able. Resolve enemy monsters from strongest to weakest. If there is a toss-up, the players choose that order.
4. Standard draw: each player draws `1` card between `Action Turn 1` and `Action Turn 2`. This standard draw is mandatory once per round.
5. `Action Turn 2`: every player takes `1` action if able, unless changed by card effects, class abilities, or scene effects. The players choose their own order.
6. `Enemy Turn 2`: every enemy monster takes `1` action if able. Resolve enemy monsters from strongest to weakest. If there is a toss-up, the players choose that order.
7. End of round: resolve cleanup, unresolved hurdles, round-end card effects, and escalation.

If a round ends before the normal standard-draw window is reached, each player still makes that mandatory standard draw as the round ends.
If a scene is fully cleared during a round, finish the current round structure unless a card or quest says the scene ends immediately.

## Class Passive Stacking

- Class passives stack by default unless a card, class rule, or quest says otherwise.
- If multiple copies of the same passive could claim the same one-time card transfer or loot event, resolve only one transfer unless the effect says otherwise.
- If more than one player is eligible for that one transfer, break the tie with a `d6` roll among the eligible players.

## Escalation And Unresolved Hurdles

- If the party does not clear all relevant hostile or blocking hurdles by the end of a standard round, escalation rises by `1`.
- Round-end effects from cards are triggered.

## Escalation 10 Exception

- At escalation `10`, the normal two-turn round cap no longer applies.
- The final ordeal continues without a standard turn limit until the scene is resolved or the party is defeated.

## Prestige Scoring

- Endgame scoring uses `prestige points`.
- Each scored card has a `Treasure Value`.
- `Treasure Points` are the Treasure Value of cards in that player's hand plus the Treasure Value of cards that player owns on the field.
- `Glory Points` are the Treasure Value of hostile and blocking cards that player claimed during the run.
- A player's prestige total is the sum of:
  - that player's Treasure Points
  - that player's Glory Points
  - that player's agenda reward
- Agenda rewards should be decisive in the total score.
