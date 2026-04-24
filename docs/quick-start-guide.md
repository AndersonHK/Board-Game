# Quick Start Guide

This guide is the current player-facing baseline for teaching and simulating the fantasy vertical slice. It is written for play at the table, not for internal design discussion. Future simulations should use this guide as their default teaching sheet unless a quest or later canon rule explicitly overrides it.

## What You Need On The Table

- `1` quest sheet or quest card
- `1` escalation tracker from `0` to `10`
- a marker for escalation
- a red `d20` to track party HP at the quest's starting value
- the encounter deck
- the resource / action deck
- the creature deck
- the secret agenda deck
- tiny red circular damage tokens for tracking damage on monsters and other damageable hurdles
- blue shield tokens
- `1` d6

## Before You Start

### 1. Pick A Quest

Choose a quest and place it where everyone can read it.

The quest should tell the table:

- the quest name and theme
- the starting party HP
- any special setup rule
- what happens at important escalation thresholds
- what the final ordeal is at escalation `10`

### 2. Build The Play Area

Set up the shared table like this:

- place the quest in the center
- set the escalation marker to `0`
- set the party HP marker to the quest's starting HP
- shuffle the encounter deck and place it face down
- shuffle the resource / action deck and place it face down
- shuffle the creature deck and place it face down
- shuffle the secret agenda deck and place it face down
- place the red damage tokens where all players can reach them
- place the blue shield tokens where all players can reach them
- leave room for encounter cards, spawned monsters, persistent obstacles, and discard piles

### 3. Choose A Class

Each player chooses one class:

- `Warrior`
- `Wizard`
- `Cleric`

Classes are not unique. In a `4`-player game, more than one player may choose the same class.

Each class has one passive trait and one active trait.

### 4. Take A Secret Agenda

After choosing a class, each player draws `1` secret agenda card and keeps it hidden.

You are all on the same side for survival, but each player is still trying to finish the game with the most prestige, credit, or hidden agenda value.

### 5. Draw Your Starting Hand

Each player draws `3` cards from the resource / action deck.

Starting hand size is always `3`.

Hand limits:

- `Warrior`: `6`
- `Cleric`: `6`
- `Wizard`: `12`

Players only discard down to hand limit during cleanup, not in the middle of a scene unless an effect tells them to.

## Three-Player Setup

If you are playing with `3` players instead of `4`:

- start party HP at `18`
- each player draws `4` starting cards instead of `3`

## Your Class Traits

## Warrior

The Warrior is the aggressive class. It wants to strike first, finish monsters, and profit from decisive kills.

### Warrior Passive

Whenever you deal the final point of damage to a monster with your own:

- action card
- creature card
- Warrior trait damage

roll `1d6`.

You draw `1` card if the result is less than or equal to:

`monster threat x rarity multiplier`

Use these rarity multipliers:

- `Common = 1`
- `Elite = 2`

Use these threat tiers:

- `Threat 1`
- `Threat 2`
- `Threat 3`

That means the Warrior kill reward works like this:

- `Threat 1 Common`: draw on `1`
- `Threat 2 Common`: draw on `1-2`
- `Threat 3 Common`: draw on `1-3`
- `Threat 1 Elite`: draw on `1-2`
- `Threat 2 Elite`: draw on `1-4`
- `Threat 3 Elite`: draw on `1-6`

The strongest elite monsters therefore guarantee the draw.

This passive only cares about monster kills. It does not trigger from clearing a bargain, opening a door, or resolving a hazard unless that card is explicitly a monster.

### Warrior Active

Once per turn, the Warrior may deal `2` damage.

Use this as a normal attack line. If that damage deals the final point of damage to a monster, it can trigger the Warrior passive.

## Wizard

The Wizard is the defensive late-game class. It survives by keeping more options in hand and spending cards carefully.

### Wizard Passive

Your hand limit is `12` instead of `6`.

This does not give you extra draws. It only changes how many cards you may keep at cleanup.

### Wizard Active

Once per scene, place `2` blue shield tokens on either:

- the party
- any creature on the field

Shield tokens prevent damage `1` for `1`.

Remove shield tokens before adding damage tokens or reducing party HP.

Unused shield tokens from this active do not carry into the next scene.

## Cleric

The Cleric is the cooperative support class. It gains value by helping others survive.

### Cleric Passive

Once per scene, when another player makes a save, you may give that roll `+1`.

If that `+1` changes a failure into a success, that player chooses `1` card they would have lost from that ordeal. Put that card into your hand instead of the discard pile.

The helped player chooses the card, not the Cleric.

If more than one Cleric could claim the same one-time transfer, only `1` transfer happens.

Break that tie with a `d6` roll among the eligible Clerics.

### Cleric Active

Once per scene, heal one of the following:

- `1` party HP
- `2` HP to any creature on the field

The Cleric may heal friendly or hostile creatures if the table wants that line for the scene.

## Stacking Passives

If more than one player has the same class passive, those passives stack unless a card or quest says otherwise.

## Core Card And Table Terms

### Resource / Action Cards

These are the cards in player hands.

They may do things like:

- deal damage
- prevent damage
- force or prevent discards
- improve a roll
- summon or support creatures
- create future advantages

If a card tells you to discard cards as a cost, you must pay that discard before getting the effect.

### Creature Cards

Creature cards are spawned by encounters.

A creature may have:

- a name
- a threat tier
- a rarity
- HP
- attack or defense value
- a round-end effect

Use red damage tokens to track how much damage a creature has taken.

Damage tokens are placed only when the target survives the hit.

If a creature or artifact receives blue shield tokens, remove those first before adding damage tokens.

When damage on a creature equals or exceeds its HP, that creature is defeated and removed from the scene unless a quest or card says otherwise.

Some cards in this shared entity layer are not normal attackers:

- `Artifacts` use the same card grammar as creatures but have `Attack 0`
- `Enchantments` do not use HP and attack values by default, so they are not combat targets unless a card says otherwise
- summoned creatures cannot attack on the turn they are summoned unless a card says otherwise

Some high-threat bosses may use a named active ability and still attack on the same turn if their card says so.

Enemy-monster default behavior:

- if an enemy monster has a named active ability it can legally use, it uses that instead of attacking
- if an enemy monster attacks and a friendly creature is a legal target, it targets a friendly creature first
- if no friendly creature is a legal target, it attacks the party
- card text can override this, and future effects such as `silence` can stop an ability from being usable

### Common And Elite

Both monsters and player cards now use the same two rarity words:

- `Common`
- `Elite`

As a general rule:

- `Common` cards are simpler and weaker
- `Elite` cards are stronger and more likely to matter at round end

### Threat Tiers

For this draft baseline, monsters use three threat tiers:

- `Threat 1` for early pressure
- `Threat 2` for mid pressure
- `Threat 3` for late pressure

These tiers line up with the three major escalation zones of the game.

## The Escalation Track

Escalation runs from `0` to `10`.

The printed track should read visually like this:

- green zone: early game
- yellow zone: mid game
- red zone: late game
- skull symbol at `10` for the final ordeal

Use these draft bands:

- `0-3`: early
- `4-6`: mid
- `7-9`: late
- `10`: final ordeal

## Round Structure

At escalation `0`, the game starts with a prep scene instead of a hostile battle, but it still uses the normal round structure.

Each round follows this order:

1. Reveal the next encounter, or continue the current one if it was not cleared.
2. Resolve the encounter's immediate text.
3. Spawn any monsters, hazards, doors, enchantments, or tests created by that encounter.
4. `Action Turn 1`: every player takes `1` action if able. The players choose their own order.
5. `Enemy Turn 1`: every enemy monster takes `1` action if able. Resolve enemy monsters from strongest to weakest. If there is a toss-up, the players choose that order.
6. Standard draw: each player draws `1` card between `Action Turn 1` and `Action Turn 2`. This standard draw is mandatory once per round.
7. `Action Turn 2`: every player takes `1` action if able. The players choose their own order.
8. `Enemy Turn 2`: every enemy monster takes `1` action if able. Resolve enemy monsters from strongest to weakest. If there is a toss-up, the players choose that order.
9. Resolve cleanup, unresolved hurdles, round-end card effects, and escalation.

Unless a card, quest, or trait changes it:

- each player gets `1` action in each action turn if able
- each enemy monster gets `1` action in each enemy turn if able
- players act before enemy monsters in each half of the round
- enemy monsters use a legal named active ability before making a normal attack unless their card says they can do both
- enemy monsters attack friendly creatures first if possible, and attack the party only when no friendly creature is a legal target

If a round ends before the normal standard-draw window is reached, each player still makes that mandatory standard draw as the round ends.

## Actions

On your action, you usually do one meaningful thing, such as:

- play an action card
- make a basic attack for `1` damage
- attack with a creature or damaging effect
- use a class active trait
- solve a non-combat test
- contribute to clearing a blocking hurdle

If a card or trait deals damage, place damage tokens equal to the damage dealt.

Basic attacks may target creatures and other damageable blocking hurdles unless that card says it cannot be targeted by combat.

## Saves And Tests

If a save is required and no other number is given, succeed on `4+` on a d6.

That means:

- `4`, `5`, or `6` succeeds
- `1`, `2`, or `3` fails

If a card, class trait, or encounter gives a modifier, apply it to the roll before checking success.

## Spawning Monsters By Criteria

Some encounters name exact monsters.

Other encounters use criteria such as:

- `1 Threat 2 humanoid`
- `2 Threat 1 beasts`

When criteria are used:

1. Go through the creature deck from top to bottom once.
2. Fill the requested slots as matching cards appear.
3. Take the first legal matches you find.

Do not sort the deck or search it multiple times unless a card or quest says to.

## Clearing A Scene

A scene is fully cleared only when all hostile and blocking hurdles are gone.

Blocking hurdles can include:

- monsters
- doors
- persistent hazards
- enchantments
- other cards that still block safety, reward, or forward progress

If the scene is fully cleared, it ends after the current round structure finishes unless a card or quest says it ends immediately.

## Escalation Advancement

For this draft baseline:

- when the party fully clears a new scene, advance escalation by `1`
- if hostile or blocking hurdles remain at the end of a round, escalation also rises by `1`
- if a scene is unresolved, it does not grant the normal clear-scene advance

This means good play still moves the quest forward, while bad play makes danger rise faster.

## Multi-Round Encounters

If a scene is not cleared in one round, it continues into the next round.

Important rule:

- the standard draw happens once each round

If the same encounter lasts two or more rounds, each round still gives its own mandatory standard draw.

## Cleanup

At cleanup:

- resolve round-end card text
- check unresolved hostile or blocking hurdles
- raise escalation if required
- discard down to hand limit

Hand limits at cleanup are:

- `6` for Warrior
- `12` for Wizard
- `6` for Cleric

## Trader Scenes

If a trader encounter tells you to reveal trader cards:

- reveal the top `5` cards of the resource deck
- each player gets exactly `1` trader interaction in that scene
- on that interaction, the player chooses either a direct trade or `Haggle`

Direct trade:

- swap `1` card from your hand with `1` revealed trader card

Haggle:

- roll `1d6`
- on `1-2`, discard `1` card, then trade `1` hand card for `1` trader card
- on `3-4`, trade `1` hand card for `1` trader card
- on `5-6`, trade `1` hand card for `2` trader cards

## Escalation 10 And The Final Ordeal

When escalation reaches `10`, begin the final ordeal shown by the quest.

At escalation `10`:

- the normal two-turn round cap ends
- the final ordeal continues until the scene is resolved or the party is defeated
- the ordeal still gives the normal mandatory standard draw once each round

## Prestige Scoring

At the end of the game, total `prestige points`.

Each scored card has a `Treasure Value`.

First total your `Treasure Points`:

- the Treasure Value of cards in your hand
- the Treasure Value of cards you own on the field

Then total your `Glory Points`:

- the Treasure Value of hostile and blocking cards you claimed during the run

Then add:

- your Treasure Points
- your Glory Points
- your agenda reward

Agendas are meant to be decisive, so expect them to be worth a large share of your final score.

## Simulation Use Rule

Future simulations should use this guide as the baseline player-facing rules document.

If a simulation encounters any mechanic that is:

- ambiguous
- missing from this guide
- contradicted by another document

that ambiguity should be written into that simulation's rulings log and findings log so it can be resolved and folded back into the guide later.
