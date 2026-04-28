# Board Layout Definition

This document defines the generated Edition 0 table-state board. The board is not a map; it is a large organizer for decks, widgets, and shared party cards.

## Page Decision

The board uses `3` portrait US letter sheets side by side.

Two portrait sheets side by side would create a `17 in x 11 in` board. After printer-safe margins, that leaves about `168 sq in` of usable space. The required board zones need about `230 sq in` once real card piles, the four-slot quest reference, six shared-party card slots, token bank, party HP, and escalation are given readable spacing. That is too compressed for a table aid.

Three portrait sheets side by side create a `25.5 in x 11 in` board. After margins, that leaves about `255 sq in` of usable space, which is enough for the current Edition 0 board with modest breathing room. Trader stock and personal score piles are handled off-board instead of reserving printed board slots.

## Physical Size

- Page size: `8.5 in x 11 in`
- Page orientation: portrait
- Page count: `3`
- Full assembled board: `25.5 in x 11 in`
- Print DPI: `288`
- Full generated PNG size: `7344 x 3168 px`
- Per-page PNG size: `2448 x 3168 px`
- Standard deck slot guide: `2.125 in x 3.6667 in`
- Quest reference slot guide: `4.25 in x 7.3334 in`

Print each page at `100%` scale, then place them left to right:

1. `BOARD-PAGE-01-left.png`
2. `BOARD-PAGE-02-center.png`
3. `BOARD-PAGE-03-right.png`

Each connecting edge has corner labels and a center seam sigil. The sigil completes only when the matching pages are placed side by side in the correct order.

## Required Zones

The generated board includes these labeled zones:

| Zone | Purpose |
| --- | --- |
| Quest Reference | Current quest card, currently `Ashen Depths` |
| Escalation Meter | Large vertical printed `0-10` escalation track |
| Party HP | Red `d20` party HP tracker plus space for party shield tokens |
| Current Encounter | Single revealed encounter, prep scene, trader scene, or scripted ordeal |
| Encounter Deck | Shuffled encounter cards |
| Scripted Ordeals | Scripted encounter cards kept out of the random deck |
| Resource Deck | Shuffled resource/action cards |
| Entity Deck | Shuffled creature/entity cards |
| Secret Agenda Deck | Face-down secret agenda cards before dealing |
| Token Bank | Damage, shield, used, and reminder tokens |
| Shared Party Cards | Six full-size standard-card slots for party-controlled permanents and shared supports |
| Fixed Player Order | Seating or turn-order reminder |

Current Encounter, Encounter Deck, Scripted Ordeals, Resource Deck, Entity Deck, Secret Agenda Deck, and each Shared Party Cards slot all draw the same standard-card footprint inside their labeled board zones. Current Encounter draws one standard-card slot; deck zones draw stacked card guides. The surrounding labeled rectangles may include title and reminder space, but the card placement guide itself stays at `2.125 in x 3.6667 in`.

Ordinary discard piles, trader stock, and player score piles are not board zones. Put spent resource cards, defeated cards that are not scored, temporary discard piles, and revealed trader stock on the table beside the relevant deck or player area. Cards claimed from kills stay in that player's personal score pile beside their own play area so each player can track their own kills.

## Generated Files

Run:

```powershell
python .\assets\scripts\generate_table_board.py
```

Outputs:

- `assets/generated/board/table-board-full.png`
- `assets/generated/board/BOARD-PAGE-01-left.png`
- `assets/generated/board/BOARD-PAGE-02-center.png`
- `assets/generated/board/BOARD-PAGE-03-right.png`
- `assets/generated/print/table-board-pages.pdf`
