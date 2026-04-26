# Print And Bundle Package

This manifest defines the complete physical package for the Edition 0 vertical-demo bundle. It is the production checklist for what must be printed, cut, sleeved or bundled, and placed on the table so the game can be played from the quick-start guide and cards.

Printed player-facing rules live in [../docs/quick-start-guide.md](../docs/quick-start-guide.md). Printed card data lives in [../defines/cards/](../defines/cards/). For printed-materials-only playtests, use [printed-materials-index.md](./printed-materials-index.md) as the read list and defer non-printed rule references until after the run.

## Production Target

- Format: classroom-printable physical prototype.
- Paper target: US letter-size sheets.
- Card target: letter-size printable atlases using the card size and sheet assignments in [card-atlas-definition.md](./card-atlas-definition.md).
- Rules target: ten letter-size quick-start sheets from [../docs/quick-start-guide.md](../docs/quick-start-guide.md).
- Board target: three portrait letter-size board pages placed side by side into one `25.5 in x 11 in` table organizer.
- Widget target: printed vertical escalation meter and printed token sheets.
- Non-paper components: `1` red `d20`, `1` d6, and `1` guitar pick for the escalation arrow.

Player-facing widget and token definitions live in [widget-and-token-definitions.md](./widget-and-token-definitions.md).

## Card Package

Generated card print assets:

- Front atlas PNGs: `assets/generated/atlases/fronts/`
- Back atlas PNGs: `assets/generated/atlases/backs/`
- Duplex card atlas PDF: `assets/generated/print/card-atlases-duplex.pdf`
- Individual back textures: `assets/generated/card-backs/`

Back identity policy:

- Ashen Depths quest card, scripted ordeals, and quest-triggered unique creatures use `ASHEN DEPTHS` backs so they are easy to separate from generic pools.
- Random encounter cards use `ENCOUNTER` backs even when they are bundled with the current quest.
- Resource/action cards use `RESOURCE` backs. They belong to the same broad fantasy setting as the class cards, but their back identity stays resource-first for sorting.
- Class reference cards use `FANTASY PACK` backs because they are broad-setting hero/class references, not Ashen Depths-specific cards.
- Generic creature/entity cards use `ENTITY` backs.
- Secret agenda cards use `AGENDA` backs.

### Quest Deck

Print `1` four-slot quest reference card.

| Card | Copies |
| --- | ---: |
| Ashen Depths | `1` |

The quest card must be readable from the table because it owns starting HP, starting hand size, threshold events, loss condition, and win condition.

### Encounter Deck

Print `12` encounter cards.

Random encounters are shuffled into the encounter deck. Scripted ordeals are held outside the encounter deck until the quest calls for them.

| Encounter | Type | Copies |
| --- | --- | ---: |
| Bound Pilgrim | Random | `1` |
| Cracked Causeway | Random | `1` |
| Ember Tax Patrol | Random | `1` |
| Ember-Bell Nursery | Random | `1` |
| Kennel Break | Random | `1` |
| Kennel Vault | Random | `1` |
| Reliquary of Cinders | Random | `1` |
| Shrine of Echoes | Random | `1` |
| Smoke-Flood Gallery | Random | `1` |
| Soot-Stall Trader | Random | `1` |
| Furnace Warden Rises | Scripted Ordeal | `1` |
| Dragon in the Deep | Scripted Ordeal | `1` |

Production note: the encounter deck currently has `10` random encounters, which is above the original minimum of `8`.

### Resource / Action Deck

Print `80` resource cards.

| Card | Copies |
| --- | ---: |
| Arc Bolt | `4` |
| Battle Prayer | `4` |
| Blood Price Burst | `2` |
| Bonefuel Volley | `2` |
| Borrowed Time | `2` |
| Brace Together | `4` |
| Chain Cutter | `4` |
| Dispel Draft | `4` |
| Field Bandage | `4` |
| Greedfire Vow | `2` |
| Hidden Stash | `4` |
| Last Step | `2` |
| Lockpick Kit | `4` |
| Mercy Prayer | `4` |
| Oathbound Strike | `2` |
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

### Entity Deck

Print `84` creature/entity cards.

Common cards use `4` copies. Elite and Rare cards use `2` copies, except quest-unique scripted bosses and boss stages, which use `1` copy.

| Card | Subtype | Copies |
| --- | --- | ---: |
| Ash Cultist | Enemy | `4` |
| Ash Miasma | Enchantment | `2` |
| Ash Ogre | Enemy | `2` |
| Ash Skulk | Enemy | `4` |
| Ashen Warden | Boss | `1` |
| Blessing Brazier | Artifact | `2` |
| Chainbound Head | Boss | `1` |
| Cinder Familiar | Ally | `2` |
| Cinder Knight | Enemy | `2` |
| Cinder Sapper | Enemy | `4` |
| Dire Wolf | Enemy | `2` |
| Ember Bat | Enemy | `4` |
| Furnace Hound | Enemy | `4` |
| Goblin Bruiser | Enemy | `4` |
| Goblin Chieftain | Enemy | `2` |
| Goblin Cutthroat | Enemy | `4` |
| Grave Hound | Ally | `2` |
| Grave Knight | Enemy | `2` |
| Gray Wolf | Enemy | `4` |
| Greedfire Vow | Enchantment | `2` |
| Heartfire Dragon | Boss | `1` |
| Heavy Door | Artifact | `4` |
| Iron Gate | Artifact | `4` |
| Kiln Pup | Enemy | `1` |
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

Print `3` two-slot class reference cards.

| Class | Copies |
| --- | ---: |
| Warrior | `1` |
| Wizard | `1` |
| Cleric | `1` |

These are generated from the class section of the quick-start guide as two-slot reference cards, so players do not need to pass the rules sheet around constantly.

## Rules Sheets

Print [../docs/quick-start-guide.md](../docs/quick-start-guide.md) as `10` letter-size reference sheets:

1. Setup
2. Classes
3. Round And Actions
4. Cards And Scenes
5. Trader And Scoring

The generated print asset is `assets/generated/guide/quick-start-guide.pdf`, with `10` letter-size pages.

Layout guidance:

- Use a readable body font at roughly `10 pt` or larger after final layout.
- Use fantasy or gothic display fonts for titles and major headings only.
- Keep body text high-contrast over any generated background texture.
- Keep enough margin for classroom printers.

## Paper Widgets

See [widget-and-token-definitions.md](./widget-and-token-definitions.md) for the player-facing physical-state definitions of these widgets.

### Background Table Board

Print `3` portrait letter-size table board pages and place them side by side from left to right.

Generated board files:

- `assets/generated/board/table-board-full.png`
- `assets/generated/board/BOARD-PAGE-01-left.png`
- `assets/generated/board/BOARD-PAGE-02-center.png`
- `assets/generated/board/BOARD-PAGE-03-right.png`

The assembled board is `25.5 in x 11 in`. A two-page board was rejected because the safe printable area is too tight for the quest reference, all deck zones, escalation, tokens, and six shared-card slots.

Deck, current-scene, and shared-party placement guides should match the physical standard card size, `2.125 in x 3.6667 in`. The quest reference guide should match the four-slot quest card size, `4.25 in x 7.3334 in`.

It should contain titled rectangles for:

- Quest
- Escalation Meter
- Party HP
- Current Encounter
- Encounter Deck
- Scripted Ordeals
- Resource Deck
- Entity Deck
- Secret Agenda Deck
- Token Bank
- Shared Party-Controlled Cards, as six full-size standard-card slots
- Fixed Player Order

The board is not a spatial map. It is an organizer for the card-table state.

Ordinary discard piles, trader stock, and player score piles are not printed board zones. Place spent resource cards, defeated unclaimed cards, revealed trader stock, unused trader stock, and other temporary discards on the table beside the relevant deck or player area. Cards claimed from kills go into the claiming player's personal score pile beside their own play area so each player's kills remain trackable.

### Escalation Meter

Print `1` large vertical escalation meter from `0` to `10`.

Required features:

- `0-3`: green early zone
- `4-6`: yellow mid zone
- `7-9`: red late zone
- `10`: printed `10`, skull, or final-ordeal marker
- enough side space for a guitar pick used as the escalation arrow

Do not print or bundle a paper needle. Use the guitar pick beside the current number as the escalation arrow.

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

See [widget-and-token-definitions.md](./widget-and-token-definitions.md) for token appearance, counts, and tracking use.

### Required Tokens

Print and cut:

| Token | Suggested Count | Use |
| --- | ---: | --- |
| Red damage tokens | `40` | Damage already dealt to surviving damageable cards |
| Blue shield tokens | `20` | Shield tokens on party or creatures |
| Yellow used markers | `16` | Once-per-scene, first-time, exhausted, or used-this-round effects |
| Green reminder markers | `12` | Claimant, threshold tax, active player, or other temporary reminders |

### Token Notes

- The physical prototype uses four-color plastic bingo chips: red, blue, yellow, and green.
- The chips are `7/8 in` diameter, and the board's token-bank circles are printed at that physical size.
- Red damage tokens and blue shield tokens should remain visually distinct.
- Yellow used markers cover once-per-scene, first-time, exhausted, and used-this-round effects.
- Green reminder markers cover current claimant, threshold tax, active player, and similar temporary memory aids.
- Use printed proxy cards, not plastic tokens, if a required physical card copy runs out.

## Dice And Non-Paper Components

Bundle:

- `1` red `d20` for party HP
- `1` d6 for saves, Haggle, Warrior rewards, tie-breaks, and random effects
- `1` guitar pick for the escalation track arrow
- optional card sleeves or small bags for deck separation

The red `d20` is specifically the party HP tracker, not a die used for rolling.

## Storage And Bundling

Bundle the package into these labeled groups:

1. Rules sheets
2. Table board and widgets
3. Tokens and dice
4. Quest card
5. Encounter deck
6. Scripted ordeal cards
7. Resource deck, including overflow resource cards from `ATLAS-REF-02` slots `05-12`
8. Entity deck
9. Secret agenda deck
10. Class references

Deck dividers or rubber bands should clearly separate random encounters from scripted ordeals.

## Printability Checklist

Before final printing, confirm:

- card fronts match the atlas sheet assignments in [card-atlas-definition.md](./card-atlas-definition.md)
- every card has art, title, and readable rules text
- every card back follows the intended identity policy: `ASHEN DEPTHS` for quest-specific cards, `ENCOUNTER` for random encounters, `RESOURCE` for resource/action cards, `FANTASY PACK` for broader class references, `ENTITY` for generic entities, and `AGENDA` for secret agendas
- quick-start sheets fit on letter paper with comfortable margins
- the vertical escalation meter is large enough to read from across the table
- red damage tokens and blue shield tokens are visually distinct in dim classroom lighting
- the background board leaves enough room for real card piles, not just labels
- each player's personal score pile is physically obvious in that player's own area
- the encounter deck and scripted ordeals cannot be accidentally shuffled together

## Playability Sanity Check

With this package, the Edition 0 vertical demo should be playable from the printed materials:

- setup is covered by the quick-start, quest card, board, decks, dice, and tokens
- party HP is tracked by the red `d20`, with party shield tokens placed in the Party HP box
- escalation is tracked by the printed vertical meter and the guitar-pick arrow
- entity damage is tracked by red damage tokens
- shields are tracked by blue shield tokens
- hand size and cleanup are tracked by each player's hand and class reference
- fixed player order is tracked by seating, the board, or player mats
- claims, kills, and scoring are tracked by per-player score piles kept in each player's own area
- discard piles are placed on the table beside the relevant deck or player area
- current claimant has a marker if the table needs it
- once-per-scene and first-time effects can use generic used markers
- printed proxy cards cover missing physical copies

## Gaps Or Final Decisions To Close

These are not blockers for a supervised classroom prototype, but they should be decided or printed before the package is treated as fully production-ready.

1. Party HP maximum is not explicitly defined. Cards can heal party HP, but the rules do not say whether party HP can exceed its starting value. Recommended default: party HP cannot exceed the quest's starting party HP for the current player count unless a card says otherwise.
2. Once-per-scene and first-time effects need a printed tracking convention. The package includes generic used markers, but the quick-start should eventually say whether players mark the card, rotate it, or place a marker on it.
3. Duplex card backs should be proofed once for printer flip direction and alignment before printing the full deck.
4. Bring `1` guitar pick for the escalation arrow.
