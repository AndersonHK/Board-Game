# Creature Deck Defines

This file records canonical creature deck rules for table play.

## Deck Role

Use a separate creature deck for spawned entities.

It is separate from:

- the world / quest system
- the encounter deck
- the resource / artifact / action deck
- the secret agenda deck

## What The Creature Deck Holds

The creature deck can include:

- monsters
- allied creatures or summons, if the same grammar remains useful there
- artifacts that use the same stat line as creatures but have `Attack 0`
- enchantments that share the same file structure even when they are not combat targets

Persistent obstacles or enchantments such as `Heavy Door` or `Miasma` can use the same card grammar.

## Copy Counts And Proxies

- Common cards have `4` copies in the creature deck.
- Elite and Rare cards have `2` copies in the creature deck unless a card says otherwise.
- Quest-unique scripted cards have `1` copy.
- Quest-unique scripted cards include unique bosses and ordeal stages such as `Ashen Warden`, `Chainbound Head`, and `Heartfire Dragon`.
- If an encounter requires more copies than are physically available, use coins or other ad-hoc tokens as extra copies.
- A proxy token uses the original card's name, stats, rules text, and Treasure Value.

## Relationship To Encounters

- Encounter cards define the scene and tell the table what to spawn.
- Creature cards provide the actual stats, attacks, defenses, and round-end effects.
- Exact-name spawns search the reserve for the named card.
- When an encounter specifies criteria instead of exact names, players go through the creature deck in order and take the first cards that fulfill the criteria.
- Criteria searches use one top-to-bottom pass through the creature deck unless a card says otherwise.

Example:

- `Ashen Ambush`
  - low escalation: `1 Goblin Chieftain` and `2 Goblin Warriors`
  - medium escalation: `1 Strength 2 humanoid` and `2 Strength 1 beasts`
  - high escalation: `1 Ogre Brute`

## Creature Turn Rules

- On its action, an enemy monster uses a named active ability instead of attacking if it has one it can legally use.
- If an enemy monster attacks and a friendly creature is a legal target, it must target a friendly creature first.
- If no friendly creature is a legal target, that enemy monster attacks the party.
- Friendly summoned creatures do not take independent full turns unless a card says otherwise.
- A player may spend an action to attack with one friendly creature they control if that creature can attack.
- A player may use a friendly creature's printed exhaust ability at its allowed timing. If no timing is printed, use it during that player's action.
- Summoned creatures cannot attack on the turn they are summoned unless a card says otherwise.
- Effects such as `silence`, target restrictions, or card text can stop an ability from being usable or can override this default behavior.
- High-threat boss cards may use a named active ability and still attack in the same turn if their card says so.

## Exhaust

- To exhaust a creature or other entity, rotate or mark that card after using its exhaust ability.
- Exhausted cards ready at the start of each new round.
- An exhausted card cannot use another exhaust ability until it readies.
