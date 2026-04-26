# Print And Bundle Package

This manifest defines the complete physical package for the Edition 0 vertical-demo bundle. It is the production checklist for what must be printed, cut, sleeved or bundled, and placed on the table so the game can be played from the quick-start guide and cards.

Canonical rules live in [../docs/quick-start-guide.md](../docs/quick-start-guide.md), [../defines/core-rules.md](../defines/core-rules.md), and [../defines/creature-deck.md](../defines/creature-deck.md). Canonical card data lives in [../defines/cards/](../defines/cards/).

## Production Target

- Format: classroom-printable physical prototype.
- Paper target: US letter-size sheets.
- Card target: letter-size printable atlases using the card size and sheet assignments in [card-atlas-definition.md](./card-atlas-definition.md).
- Rules target: five letter-size quick-start sheets from [../docs/quick-start-guide.md](../docs/quick-start-guide.md).
- Board target: one printed table board or mat with labeled placement rectangles.
- Widget target: printed escalation meter, paper needle, and printed token sheets.
- Non-paper components: `1` red `d20`, `1` d6, and a small fastener or substitute for the escalation needle.

## Card Package

### Quest Deck

Print `1` two-slot quest reference card.

| Card | Copies |
| --- | ---: |
| Ashen Depths | `1` |

The quest card must be readable from the table because it owns starting HP, starting hand size, threshold events, loss condition, and win condition.

### Encounter Deck

Print `11` encounter cards.

Random encounters are shuffled together. Scripted ordeals are held outside the random encounter deck until the quest calls for them.

| Encounter | Type | Copies |
| --- | --- | ---: |
| Bound Pilgrim | Random | `1` |
| Cracked Causeway | Random | `1` |
| Ember-Bell Nursery | Random | `1` |
| Kennel Break | Random | `1` |
| Kennel Vault | Random | `1` |
| Reliquary of Cinders | Random | `1` |
| Shrine of Echoes | Random | `1` |
| Smoke-Flood Gallery | Random | `1` |
| Soot-Stall Trader | Random | `1` |
| Furnace Warden Rises | Scripted Ordeal | `1` |
| Dragon in the Deep | Scripted Ordeal | `1` |

Production note: the encounter deck currently has `9` random encounters, which is above the original minimum of `8`.

### Resource / Action Deck

Print `72` resource cards.

| Card | Copies |
| --- | ---: |
| Arc Bolt | `4` |
| Battle Prayer | `4` |
| Blood Price Burst | `2` |
| Bonefuel Volley | `2` |
| Chain Cutter | `4` |
| Dispel Draft | `4` |
| Field Bandage | `4` |
| Greedfire Vow | `2` |
| Hidden Stash | `4` |
| Last Step | `2` |
| Lockpick Kit | `4` |
| Mercy Prayer | `4` |
| Prepared Ground | `4` |
| Quick Slash | `4` |
| Rally Push | `2` |
| Shield Breaker | `2` |
| Smoke Route | `4` |
| Study the Signs | `4` |
| Summon Cinder Familiar | `4` |
| Summon Grave Hound | `2` |
| Summon Tin Golem | `2` |
| Warding Circle | `4` |

### Creature / Entity Deck

Print `73` creature/entity cards.

Common cards use `4` copies. Elite cards use `2` copies, except quest-unique scripted bosses and boss stages, which use `1` copy.

| Card | Subtype | Copies |
| --- | --- | ---: |
| Ash Cultist | Enemy | `4` |
| Ash Miasma | Enchantment | `2` |
| Ash Ogre | Enemy | `2` |
| Ashen Warden | Boss | `1` |
| Blessing Brazier | Artifact | `2` |
| Chainbound Head | Boss | `1` |
| Cinder Familiar | Ally | `2` |
| Cinder Knight | Enemy | `2` |
| Dire Wolf | Enemy | `2` |
| Ember Bat | Enemy | `4` |
| Furnace Hound | Enemy | `4` |
| Goblin Bruiser | Enemy | `4` |
| Goblin Chieftain | Enemy | `2` |
| Goblin Cutthroat | Enemy | `4` |
| Grave Hound | Ally | `2` |
| Gray Wolf | Enemy | `4` |
| Greedfire Vow | Enchantment | `2` |
| Heartfire Dragon | Boss | `1` |
| Heavy Door | Artifact | `4` |
| Iron Gate | Artifact | `4` |
| Orc Raider | Enemy | `4` |
| Rusted Chains | Artifact | `4` |
| Skeletal Porter | Enemy | `4` |
| Smoke Seer | Enemy | `2` |
| Tin Golem | Ally | `2` |
| Warding Circle | Enchantment | `4` |

### Secret Agenda Deck

Print `6` agenda cards.

| Agenda | Copies |
| --- | ---: |
| Ashes to Ashes | `1` |
| By My Grace | `1` |
| First Name in the Ballad | `1` |
| Keeper of Relics | `1` |
| Prepared Beyond Reason | `1` |
| Richer Than the Ruin | `1` |

### Class Reference Cards

Print `3` class reference cards or one shared class reference panel.

| Class | Copies |
| --- | ---: |
| Warrior | `1` |
| Wizard | `1` |
| Cleric | `1` |

These can be generated from the class section of the quick-start guide. They are not currently defined as card files under [../defines/cards/](../defines/cards/), but the package should include them so players do not need to pass the rules sheet around constantly.

## Rules Sheets

Print [../docs/quick-start-guide.md](../docs/quick-start-guide.md) as `5` letter-size reference sheets:

1. Setup
2. Classes
3. Round And Actions
4. Cards And Scenes
5. Trader And Scoring

Layout guidance:

- Use a readable body font at roughly `10 pt` or larger after final layout.
- Use fantasy or gothic display fonts for titles and major headings only.
- Keep body text high-contrast over any generated background texture.
- Keep enough margin for classroom printers.

## Paper Widgets

### Background Table Board

Print `1` landscape letter-size table board or mat.

It should contain titled rectangles for:

- Quest
- Escalation Meter
- Party HP
- Current Encounter / Scene
- Random Encounter Deck
- Scripted Ordeals
- Resource Deck
- Resource Discard Pile
- Creature / Entity Deck
- Creature / Entity Discard Pile
- Secret Agenda Deck
- Trader Stock
- Token Bank
- Shared Party-Controlled Cards
- Fixed Player Order
- Player Score Piles

The board is not a spatial map. It is an organizer for the card-table state.

### Escalation Meter

Print `1` escalation meter from `0` to `10`.

Required features:

- `0-3`: green early zone
- `4-6`: yellow mid zone
- `7-9`: red late zone
- `10`: skull or final-ordeal marker
- enough space for a paper needle, paperclip, coin, or small marker

Print `1` small paper needle.

Bundling note: include one small brad, paperclip, binder clip, or equivalent marker solution. If no fastener is available, use the needle as a loose pointer or replace it with a coin.

### Player Areas

Print either:

- `4` small player mats, or
- one shared table board with four player rectangles.

Each player area should have labeled spaces for:

- Class
- Hand
- Field / Owned Cards
- Claimed Glory Cards
- Secret Agenda
- Discard / temporary spent cards, if needed

Player mats are optional for playability, but they make ownership and scoring much easier to see.

## Tokens And Markers

### Required Tokens

Print and cut:

| Token | Suggested Count | Use |
| --- | ---: | --- |
| Red damage tokens | `40` | Damage already dealt to surviving damageable cards |
| Blue shield tokens | `20` | Shield tokens on party or creatures |
| Generic used markers | `16` | Once-per-scene, first-time, or used-this-round effects |
| Current claimant marker | `1` | Tracks the current claimant when the table might forget |
| Active player marker | `1` | Optional aid for larger tables or teaching |
| Threshold tax marker | `1` | Reminds the table whether Ashen Depths threshold-5 reward tax has fired this scene |
| Proxy tokens | `12` | Temporary extra copies if a required physical card runs out |

### Token Notes

- Red damage tokens should be small red circles.
- Blue shield tokens should be visually distinct from damage tokens.
- Generic used markers can be gray, black, or brass.
- Proxy tokens should have a blank line or write-in space for the copied card name.
- The current claimant marker can be a small banner, hand icon, crown, or labeled coin-sized token.

## Dice And Non-Paper Components

Bundle:

- `1` red `d20` for party HP
- `1` d6 for saves, Haggle, Warrior rewards, tie-breaks, and random effects
- `1` small fastener or substitute for the escalation needle
- optional card sleeves or small bags for deck separation

The red `d20` is specifically the party HP tracker, not a die used for rolling.

## Storage And Bundling

Bundle the package into these labeled groups:

1. Rules sheets
2. Table board and widgets
3. Tokens and dice
4. Quest card
5. Random encounter deck
6. Scripted ordeal cards
7. Resource deck
8. Creature / entity deck
9. Secret agenda deck
10. Class references

Deck dividers or rubber bands should clearly separate random encounters from scripted ordeals.

## Printability Checklist

Before final printing, confirm:

- card fronts match the atlas sheet assignments in [card-atlas-definition.md](./card-atlas-definition.md)
- every card has art, title, and readable rules text
- every card back is distinguishable by deck or intentionally shared
- quick-start sheets fit on letter paper with comfortable margins
- the escalation meter and needle are large enough to read from across the table
- red damage tokens and blue shield tokens are visually distinct in dim classroom lighting
- the background board leaves enough room for real card piles, not just labels
- player score piles are physically obvious
- the random encounter deck and scripted ordeals cannot be accidentally shuffled together

## Playability Sanity Check

With this package, the Edition 0 vertical demo should be playable from the printed materials:

- setup is covered by the quick-start, quest card, board, decks, dice, and tokens
- party HP is tracked by the red `d20`
- escalation is tracked by the printed meter and needle
- entity damage is tracked by red damage tokens
- shields are tracked by blue shield tokens
- hand size and cleanup are tracked by each player's hand and class reference
- fixed player order is tracked by seating, the board, or player mats
- claims and scoring are tracked by player score piles
- discard piles are represented on the board
- current claimant has a marker if the table needs it
- once-per-scene and first-time effects can use generic used markers
- proxy tokens cover missing physical copies

## Gaps Or Final Decisions To Close

These are not blockers for a supervised classroom prototype, but they should be decided or printed before the package is treated as fully production-ready.

1. Party HP maximum is not explicitly defined. Cards can heal party HP, but the rules do not say whether party HP can exceed its starting value. Recommended default: party HP cannot exceed the quest's starting party HP for the current player count unless a card says otherwise.
2. Once-per-scene and first-time effects need a printed tracking convention. The package includes generic used markers, but the quick-start should eventually say whether players mark the card, rotate it, or place a marker on it.
3. Class reference cards are needed physically but are not yet represented in [../defines/cards/](../defines/cards/). They can be generated from the quick-start for Edition 0.
4. The background board's exact visual layout is not yet defined as an asset file. This manifest defines the needed rectangles, but not the finished printable board art.
5. Token art and token sheet layout are not yet defined as asset files. The counts and purposes are defined here.
6. Card back art is not yet defined. The atlas assumes distinct hidden-deck backs for Encounter, Resource, Creature / Entity, and Secret Agenda cards.
7. The escalation needle attachment method should be chosen based on available materials: brad, paperclip, coin, or loose marker.
