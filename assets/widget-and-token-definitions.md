# Widget And Token Definitions

This file defines the physical widgets and tracking aids included in the Edition 0 vertical-demo package. It is player-facing production support: it tells a table what each printed widget is for, but it should not introduce hidden rules that are absent from the quick-start guide or cards.

The full bundle checklist lives in [print-and-bundle-package.md](./print-and-bundle-package.md). The printed rules live in [../docs/quick-start-guide.md](../docs/quick-start-guide.md).

## Background Table Board

Print `3` portrait letter-size organizer board pages and place them side by side from left to right.

The board is not a map. It is a table-state organizer with titled rectangles for the physical components players need to see.

The generated board is `25.5 in x 11 in` when assembled. It uses three portrait pages because a two-page board would leave about `168 sq in` of safe space after margins, while the current deck, widget, and six-slot shared-party zones need about `230 sq in` to avoid cramped play. Three pages leave about `255 sq in` and fit the current layout. Trader stock and personal score piles are handled off-board instead of printed board rectangles.

Generated board files:

- `assets/generated/print/table-board-pages.pdf`
- `assets/generated/board/table-board-full.png`
- `assets/generated/board/BOARD-PAGE-01-left.png`
- `assets/generated/board/BOARD-PAGE-02-center.png`
- `assets/generated/board/BOARD-PAGE-03-right.png`

Each connecting edge has corner labels showing the adjacent page and a center seam symbol that completes when the pages are assembled in the correct order.

Deck, current-scene, and shared-party placement guides use the actual standard card footprint, `2.125 in x 3.6667 in`, regardless of deck. The quest reference guide uses the current four-slot quest card footprint, `4.25 in x 7.3334 in`.

Required rectangles:

| Rectangle | What Goes There |
| --- | --- |
| Quest | The current quest card, currently `Ashen Depths` |
| Escalation Meter | The large vertical printed escalation meter from `0` to `10` |
| Party HP | The red `d20` used as the party HP tracker, plus party shield tokens |
| Current Encounter | The revealed encounter, prep scene note, trader scene, or scripted ordeal |
| Encounter Deck | Shuffled random encounter cards |
| Scripted Ordeals | Scripted encounter cards kept outside the random deck |
| Resource Deck | Shuffled player resource/action deck |
| Entity Deck | Shuffled creature/entity deck |
| Secret Agenda Deck | Face-down secret agenda cards before dealing |
| Token Bank | Unused damage, shield, used, and reminder tokens |
| Shared Party-Controlled Cards | Six full-size standard-card slots for party-controlled permanents such as `Blessing Brazier` |
| Fixed Player Order | A visible list, seating marker, or player order row |

Ordinary discard piles, trader stock, and player score piles do not need printed rectangles. Put spent, defeated, unused, temporary discards, and revealed trader stock on the table in small piles beside the relevant deck or player area. Cards claimed from kills stay in that player's personal score pile beside their own play area so kills remain trackable by player.

## Player Areas

Use either `4` small player mats or one shared table board with four player rectangles.

Each player area should contain:

- class reference
- hand
- field / owned cards
- claimed glory cards
- secret agenda
- discard or temporary spent area, if needed

For a `3`-player game, leave the fourth player area unused.

## Escalation Meter

Print `1` large vertical escalation meter from `0` to `10`.

Required markings:

| Range | Printed Treatment |
| --- | --- |
| `0-3` | green early zone |
| `4-6` | yellow middle zone |
| `7-9` | red late zone |
| `10` | printed `10`, skull, final-ordeal, or crisis marker |

Use `1` guitar pick beside the current number as the escalation arrow. Do not print or bundle a paper needle for the escalation widget.

## Party HP Tracker

Use `1` red `d20` as the party HP tracker.

The red `d20` is not the normal rolling die. It is a visible shared health counter. Use the separate `d6` for rolls.

Place party shield tokens in the Party HP box so they are visually distinct from shields on specific creatures.

The Party HP board zone prints only the tracker title, the red `d20` reminder, and the party shield-token area. Do not duplicate the shield-token instruction outside the shield-token area.

## Dice

Bundle:

- `1` d6 for saves, Haggle, Warrior rewards, tie-breaks, and random card effects
- `1` red `d20` for party HP tracking only
- `1` guitar pick for the escalation arrow

## Tokens

The physical prototype uses the hand2mind plastic bingo chips in four colors: red, yellow, blue, and green. Each chip is `7/8 in` diameter, and the board's token-bank circles are drawn at that physical size for scale.

| Token | Count | Physical Look | Tracks |
| --- | ---: | --- | --- |
| Damage token | `40` | red chip | damage already dealt to surviving damageable cards |
| Shield token | `20` | blue chip | shield points on party or creatures |
| Used marker | `16` | yellow chip | once-per-scene, first-time, exhausted, or used-this-round effects |
| Reminder marker | `12` | green chip | claimant, threshold tax, active player, or other temporary reminder when memory is uncertain |

## Token Use Notes

- Put damage tokens on a damageable card only if it survives the damage.
- Remove shield tokens before adding damage tokens or reducing party HP.
- Put used markers on or beside cards with once-per-scene or first-time effects when the table needs a reminder.
- Use a reminder marker only when the table might forget a transient state, such as current claimant, active player, or whether `Ashen Depths` threshold `5` has taxed the first qualifying reward draw this scene.
- Use printed proxy cards, not plastic chips, when the physical package runs out of a needed printed card copy; write the copied card name on the proxy card.

## Open Widget Gaps

These are production gaps, not hidden play rules:

1. No open widget gaps for Edition 0. Bring the guitar pick as the escalation arrow.
