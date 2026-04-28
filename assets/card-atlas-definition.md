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

Quest cards are special reference cards and may span a `2 x 2` atlas block:

- quest card width: `2.125 x 2 = 4.25 in`
- quest card height: `3.6667 x 2 = 7.3334 in`
- exact quest card size: `4 1/4 in x 7 1/3 in`

When cutting a quest card, do not cut the vertical or horizontal lines inside its four occupied slots.

Class reference cards may span `2` adjacent atlas columns:

- class reference width: `2.125 x 2 = 4.25 in`
- class reference height: `3.6667 in`
- exact class reference size: `4 1/4 in x 3 2/3 in`

When cutting a class reference card, do not cut the vertical line between its two occupied slots.

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

The front atlases below are canonical for Edition 0. The atlas pipeline generates one matching back atlas for every front atlas, using the appropriate back per occupied slot:

- `ASHEN DEPTHS` back for the quest card and quest-triggered unique cards that must stay identifiable outside the generic random decks. The back keeps the front-family color: quest cards use the quest palette, unique creatures use the creature/entity palette, and scripted encounters use the encounter palette.
- `ASHEN DEPTHS` back for quest-specific scripted encounters and quest-triggered ordeals that must stay identifiable outside the generic encounter pool.
- `ENCOUNTER` back for generic encounter cards, including random encounters used by the current quest.
- `RESOURCE` back for resource/action cards. They share the fantasy setting with the class cards, but their card-back identity stays resource-first so they remain easy to sort.
- `FANTASY PACK` back for class reference cards. These use the utility/hero grey palette.
- `ENTITY` back for generic creature/entity deck cards.
- `AGENDA` back for secret agenda cards.
- Shared reference back for dividers, proxies, and other non-deck utility cards that are not part of the broader fantasy pack.

Backs are assigned per slot, not only per atlas sheet. This matters for mixed reference sheets: class references use `FANTASY PACK`, resource overflow slots use `RESOURCE`, and secret agenda slots use `AGENDA`.

Ashen Depths-specific backs are intentional. They make quest-triggered uniques and scripted quest ordeals easy to separate from reusable random or generic cards after cutting, sorting, or playtesting. Hero/class cards are not Ashen Depths-specific; they belong to the broader fantasy setting pack.

If printing duplex, every front atlas must be paired with the matching back atlas and tested once on the target printer for flip direction. The default generated PDF uses unmirrored backs because FedEx-style duplex printing treats odd pages as fronts and the following even pages as backs. The atlas PDF builder still supports horizontally mirrored backs with `--mirror-backs` for printers or workflows that require pre-flipped back pages. If duplex alignment is unreliable, print fronts only and sleeve cards with opaque backs or blank backing paper.

## Atlas Summary

| Atlas Group | Sheets | Physical Cards Printed | Occupied Slots | Blank / Proxy Slots |
| --- | ---: | ---: | ---: | ---: |
| Reference Atlas | `2` | `18` | `24` | `0` |
| Encounter Atlas | `1` | `12` | `12` | `0` |
| Resource Atlas | `6` | `72` | `72` | `0` |
| Creature / Entity Atlas | `7` | `84` | `84` | `0` |
| Total | `16` | `186` | `192` | `0` |

All front-atlas slots are currently assigned to printable cards.

## Reference Atlas

### ATLAS-REF-01

Use this sheet for the quest, all class references, and two secret agenda cards.

| Slot | Card |
| ---: | --- |
| `01-02,05-06` | Ashen Depths, four-slot quest card |
| `03-04` | Warrior reference |
| `07-08` | Wizard reference |
| `09` | Prepared Beyond Reason |
| `10` | Richer Than the Ruin |
| `11-12` | Cleric reference |

### ATLAS-REF-02

Use this sheet for secret agenda cards and resource overflow cards.

| Slot Range | Card | Copies |
| --- | --- | ---: |
| `01` | Ashes to Ashes | `1` |
| `02` | By My Grace | `1` |
| `03` | First Name in the Ballad | `1` |
| `04` | Keeper of Relics | `1` |
| `05-06` | Oathbound Strike | `2` |
| `07-08` | Borrowed Time | `2` |
| `09-12` | Brace Together | `4` |

Production note: Secret agendas are hidden cards in play, but they fit cleanly on the mixed reference sheets for front printing. The generated back atlases give those slots the `AGENDA` back for duplex printing. Class reference slots on the same mixed sheet use the `FANTASY PACK` back.

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
| `10` | Ember Tax Patrol |
| `11` | Furnace Warden Rises |
| `12` | Dragon in the Deep |

After cutting, keep slots `11-12` outside the random encounter deck. They are scripted ordeals and use `ASHEN DEPTHS` backs. Slots `01-10` are random encounters and use `ENCOUNTER` backs.

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
| `02-05` | Ash Skulk | `4` |
| `06-09` | Cinder Sapper | `4` |
| `10-11` | Grave Knight | `2` |
| `12` | Kiln Pup | `1` |

## Cutting And Sorting Checklist

After printing and cutting:

1. Put `ATLAS-ENC-01` slots `01-10` into the random encounter deck.
2. Put `ATLAS-ENC-01` slots `11-12` into the scripted ordeal packet.
3. Shuffle all `ATLAS-RES-*` cards and `ATLAS-REF-02` slots `05-12` into the resource deck.
4. Shuffle all `ATLAS-CRE-*` cards into the creature / entity deck unless a quest setup instructs otherwise.
5. Put Secret Agenda cards from `ATLAS-REF-01` slots `09-10` and `ATLAS-REF-02` slots `01-04` into the secret agenda deck.
6. Keep `Ashen Depths` and class references from `ATLAS-REF-01` visible with the rules sheets.

## Open Production Decisions

These do not block a hand-cut prototype, but they should be resolved before generating final print PDFs.

1. Proof the generated back identities on the duplex PDF: `ASHEN DEPTHS`, `ENCOUNTER`, `RESOURCE`, `FANTASY PACK`, `ENTITY`, and `AGENDA`.
2. Test whether `2.125 in` card width is comfortable for the most text-heavy encounter cards after art is added.
3. Decide whether final atlases include crop marks, registration marks, or only the full-page grid.
