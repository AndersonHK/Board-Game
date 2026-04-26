# Card Atlas Definition

This document defines the printable card atlases for the Edition 0 vertical demo. An atlas is one US letter-size sheet containing a fixed grid of cards. The sheet is printed, then cut into individual cards.

Canonical card contents live in [../defines/cards/](../defines/cards/). The complete physical bundle is tracked in [print-and-bundle-package.md](./print-and-bundle-package.md).

## Sheet And Card Size

Use US letter paper: `8.5 in x 11 in`.

Edition 0 cards use a `4 x 3` portrait grid:

- columns: `4`
- rows: `3`
- cards per sheet: `12`
- card width: `8.5 / 4 = 2.125 in`
- card height: `11 / 3 = 3.6667 in`
- exact card size: `2 1/8 in x 3 2/3 in`

This is intentionally not poker-card size. It is an atlas-first prototype size chosen because each card is an exact integer-factor slice of a letter-size sheet. It minimizes wasted paper, creates simple straight cuts, and gives encounter cards more vertical text space than a standard playing card.

Quest cards are special reference cards and may span `2` adjacent atlas columns:

- quest card width: `2.125 x 2 = 4.25 in`
- quest card height: `3.6667 in`
- exact quest card size: `4 1/4 in x 3 2/3 in`

When cutting a quest card, do not cut the vertical line between its two occupied slots.

Print at `100%` scale. Do not use fit-to-page scaling unless the whole atlas is being rederived from the new printed dimensions.

## Card Safe Area

Each card slot should reserve:

- outer bleed/cut tolerance: `0.0625 in`
- inner safe margin for title, art, and rules: at least `0.125 in`
- preferred title band: top `0.28 in`
- preferred art band: about `1.15-1.35 in`
- preferred rules band: remaining lower area

Cards may use full-slot art or background texture, but all rules text must stay inside the safe margin.

## Cut Grid

For portrait letter sheets, cut at these coordinates from the top-left corner:

Vertical cuts:

- `2.125 in`
- `4.25 in`
- `6.375 in`

Horizontal cuts:

- `3.6667 in`
- `7.3333 in`

Recommended physical cut order:

1. Trim vertical columns.
2. Stack each column carefully.
3. Cut horizontal rows.
4. Sort by atlas ID and slot order.

## Slot Numbering

Slots are numbered row-major from top-left to bottom-right.

```text
01  02  03  04
05  06  07  08
09  10  11  12
```

When a card has multiple copies on a sheet, place identical copies in consecutive slots unless a later automated renderer needs a different imposition order.

## Backing Policy

The front atlases below are canonical for Edition 0. Back art is not yet finalized, but the atlas system should assume one matching back atlas per hidden deck group:

- Encounter back
- Resource back
- Creature / Entity back
- Secret Agenda back

Quest and class reference cards may be single-sided for Edition 0. If they receive backs, use a visible reference back rather than a hidden-deck back.

If printing duplex, every front atlas must be paired with the matching back atlas and tested once on the target printer for flip direction. If duplex alignment is unreliable, print fronts only and sleeve cards with opaque backs or blank backing paper.

## Atlas Summary

| Atlas Group | Sheets | Physical Cards Printed | Occupied Slots | Blank / Proxy Slots |
| --- | ---: | ---: | ---: | ---: |
| Reference Atlas | `1` | `10` | `11` | `1` |
| Encounter Atlas | `1` | `11` | `11` | `1` |
| Resource Atlas | `6` | `72` | `72` | `0` |
| Creature / Entity Atlas | `7` | `73` | `73` | `11` |
| Total | `15` | `166` | `167` | `13` |

Blank slots should become named proxy blanks, rules reminders, or spare damage/shield token art before final layout.

## Reference Atlas

### ATLAS-REF-01

Use this sheet for cards that do not belong in a shuffled deck.

| Slot | Card |
| ---: | --- |
| `01-02` | Ashen Depths, two-slot quest card |
| `03` | Ashes to Ashes |
| `04` | By My Grace |
| `05` | First Name in the Ballad |
| `06` | Keeper of Relics |
| `07` | Prepared Beyond Reason |
| `08` | Richer Than the Ruin |
| `09` | Warrior reference |
| `10` | Wizard reference |
| `11` | Cleric reference |
| `12` | Blank proxy |

Production note: Secret agendas are hidden cards in play, but they fit cleanly on this mixed reference sheet for front printing. They still need the Secret Agenda back if printed duplex.

## Encounter Atlas

### ATLAS-ENC-01

| Slot | Card |
| ---: | --- |
| `01` | Bound Pilgrim |
| `02` | Cracked Causeway |
| `03` | Ember-Bell Nursery |
| `04` | Kennel Break |
| `05` | Kennel Vault |
| `06` | Reliquary of Cinders |
| `07` | Shrine of Echoes |
| `08` | Smoke-Flood Gallery |
| `09` | Soot-Stall Trader |
| `10` | Furnace Warden Rises |
| `11` | Dragon in the Deep |
| `12` | Encounter proxy / divider |

After cutting, keep slots `10-11` outside the random encounter deck. They are scripted ordeals.

## Resource Atlases

### ATLAS-RES-01

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-04` | Arc Bolt | `4` |
| `05-08` | Battle Prayer | `4` |
| `09-10` | Blood Price Burst | `2` |
| `11-12` | Bonefuel Volley | `2` |

### ATLAS-RES-02

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-04` | Chain Cutter | `4` |
| `05-08` | Dispel Draft | `4` |
| `09-12` | Field Bandage | `4` |

### ATLAS-RES-03

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-02` | Greedfire Vow | `2` |
| `03-06` | Hidden Stash | `4` |
| `07-08` | Last Step | `2` |
| `09-12` | Lockpick Kit | `4` |

### ATLAS-RES-04

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-04` | Mercy Prayer | `4` |
| `05-08` | Prepared Ground | `4` |
| `09-12` | Quick Slash | `4` |

### ATLAS-RES-05

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-02` | Rally Push | `2` |
| `03-04` | Shield Breaker | `2` |
| `05-08` | Smoke Route | `4` |
| `09-12` | Study the Signs | `4` |

### ATLAS-RES-06

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-04` | Summon Cinder Familiar | `4` |
| `05-06` | Summon Grave Hound | `2` |
| `07-08` | Summon Tin Golem | `2` |
| `09-12` | Warding Circle | `4` |

## Creature / Entity Atlases

### ATLAS-CRE-01

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-04` | Ash Cultist | `4` |
| `05-08` | Ember Bat | `4` |
| `09-12` | Furnace Hound | `4` |

### ATLAS-CRE-02

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-04` | Goblin Bruiser | `4` |
| `05-08` | Goblin Cutthroat | `4` |
| `09-12` | Gray Wolf | `4` |

### ATLAS-CRE-03

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-04` | Orc Raider | `4` |
| `05-08` | Skeletal Porter | `4` |
| `09-12` | Heavy Door | `4` |

### ATLAS-CRE-04

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-04` | Iron Gate | `4` |
| `05-08` | Rusted Chains | `4` |
| `09-12` | Warding Circle | `4` |

### ATLAS-CRE-05

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-02` | Ash Miasma | `2` |
| `03-04` | Ash Ogre | `2` |
| `05-06` | Blessing Brazier | `2` |
| `07-08` | Cinder Knight | `2` |
| `09-10` | Dire Wolf | `2` |
| `11-12` | Goblin Chieftain | `2` |

### ATLAS-CRE-06

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01-02` | Cinder Familiar | `2` |
| `03-04` | Grave Hound | `2` |
| `05-06` | Greedfire Vow | `2` |
| `07-08` | Smoke Seer | `2` |
| `09-10` | Tin Golem | `2` |
| `11` | Ashen Warden | `1` |
| `12` | Chainbound Head | `1` |

### ATLAS-CRE-07

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01` | Heartfire Dragon | `1` |
| `02-12` | Creature proxy blanks | `11` |

The creature proxy blanks are intentional. They are useful if a run temporarily needs more physical copies than the deck definition contains, or if a damaged/misprinted card needs a stand-in.

## Cutting And Sorting Checklist

After printing and cutting:

1. Put `ATLAS-ENC-01` slots `01-09` into the random encounter deck.
2. Put `ATLAS-ENC-01` slots `10-11` into the scripted ordeal packet.
3. Shuffle all `ATLAS-RES-*` cards into the resource deck.
4. Shuffle all `ATLAS-CRE-*` nonblank cards into the creature / entity deck unless a quest setup instructs otherwise.
5. Put Secret Agenda cards from `ATLAS-REF-01` slots `03-08` into the secret agenda deck.
6. Keep `Ashen Depths` and class references visible with the rules sheets.
7. Keep proxy blanks separate from the live decks until needed.

## Open Production Decisions

These do not block a hand-cut prototype, but they should be resolved before generating final print PDFs.

1. Decide whether blank atlas slots become proxy cards, divider cards, or reminder cards.
2. Finalize hidden-deck back art for Encounter, Resource, Creature / Entity, and Secret Agenda cards.
3. Test whether `2.125 in` card width is comfortable for the most text-heavy encounter cards after art is added.
4. Decide whether class references stay card-sized or become larger dashboard panels.
5. Decide whether final atlases include crop marks, registration marks, or only the full-page grid.
