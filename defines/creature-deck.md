# Creature Deck Defines

This file records the existence and purpose of the creature deck.

## Status

The creature deck now exists as a formal part of the rules model.

It is separate from:

- the world / quest system
- the encounter deck
- the resource / artifact / action deck
- the secret agenda deck

## Purpose

The encounter deck authors scenes.
The creature deck supplies the concrete entities that those scenes put into play.

This deck exists so that an encounter card can say things like:

- spawn `1 Goblin Chieftain` and `2 Goblin Warriors`
- spawn `1 Orc Warrior` and `2 Gray Wolves`
- spawn `1 Strength 2 beast and 2 Strength 1 humanoids`

without forcing the encounter card itself to carry all of the enemy rules text.

## What The Creature Deck Holds

The creature deck can include:

- monsters
- allied creatures or summons, if the same grammar remains useful there
- artifacts that use the same stat line as creatures but have `Attack 0`
- enchantments that share the same file structure even when they are not combat targets

Persistent obstacles or enchantments such as `Heavy Door` or `Miasma` are closely related and may share the same reserve or card grammar, even if they are eventually separated into a broader entity layer.

## Relationship To Encounters

- Encounter cards define the scene and tell the table what to spawn.
- Creature cards provide the actual stats, attacks, defenses, and round-end effects.
- When an encounter specifies criteria instead of exact names, players go through the creature deck in order and take the first cards that fulfill the criteria.

Example:

- `Ashen Ambush`
  - low escalation: `1 Goblin Chieftain` and `2 Goblin Warriors`
  - medium escalation: `1 Strength 2 humanoid` and `2 Strength 1 beasts`
  - high escalation: `1 Ogre Brute`

## Creature Turn Rules

- Every creature gets to attack or defend once per turn.
- On its action, an enemy monster uses a named active ability instead of attacking if it has one it can legally use.
- If an enemy monster attacks and a friendly creature is a legal target, it must target a friendly creature first.
- If no friendly creature is a legal target, that enemy monster attacks the party.
- Summoned creatures cannot attack on the turn they are summoned unless a card says otherwise.
- Effects such as `silence`, target restrictions, or card text can stop an ability from being usable or can override this default behavior.
- High-threat boss cards may use a named active ability and still attack in the same turn if their card says so.
