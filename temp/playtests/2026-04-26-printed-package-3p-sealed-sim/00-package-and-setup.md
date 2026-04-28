# Printed-Package-Only 3P Sealed Simulation

Date: 2026-04-26

Scope: Simulated 3-player playtest using only the printed-material files named by the test request. No canonical files were edited.

Players:

| Seat | Imaginary player | Class | Secret agenda |
| --- | --- | --- | --- |
| 1 | Mira | Warrior | First Name in the Ballad |
| 2 | Sol | Wizard | Prepared Beyond Reason |
| 3 | Brann | Cleric | By My Grace |

Initial state:

- Quest: Ashen Depths
- Player count: 3
- Party HP: 18
- Escalation: 0
- Starting hand size: 4 cards each
- Fixed order: Mira, Sol, Brann

## Deterministic Package

The table treated the printed decks as shuffled before play. This log uses a deterministic order so the run is reproducible.

Random encounter order:

1. Soot-Stall Trader
2. Cracked Causeway
3. Kennel Vault
4. Reliquary of Cinders
5. Ember-Bell Nursery
6. Smoke-Flood Gallery
7. Kennel Break
8. Bound Pilgrim
9. Shrine of Echoes

Scripted ordeals:

1. Furnace Warden Rises at threshold 5
2. Dragon in the Deep at threshold 10

Starting hands:

| Player | Cards |
| --- | --- |
| Mira | Quick Slash, Quick Slash, Chain Cutter, Summon Grave Hound |
| Sol | Warding Circle, Arc Bolt, Hidden Stash, Dispel Draft |
| Brann | Battle Prayer, Field Bandage, Mercy Prayer, Lockpick Kit |

Important early resource draws and trader stock:

| Window | Cards |
| --- | --- |
| Prep standard draw | Mira: Last Step; Sol: Prepared Ground; Brann: Arc Bolt |
| Trader stock | Chain Cutter, Quick Slash, Summon Cinder Familiar, Blood Price Burst, Field Bandage |
| Trader round standard draw | Mira: Shield Breaker; Sol: Study the Signs; Brann: Smoke Route |
| Later key draws | Bonefuel Volley, Quick Slash, Battle Prayer, Hidden Stash, Blood Price Burst, Field Bandage, Arc Bolt |

Creature-deck criteria order used by Kennel Vault:

1. Cinder Knight
2. Orc Raider
3. Gray Wolf
4. Furnace Hound
5. Ember Bat

Kennel Vault took Orc Raider as the first Threat 2 humanoid, then Gray Wolf and Ember Bat as the first two Threat 1 beasts.

## Temporary Printed-Table Ruling Policy

When the printed quickstart or cards did not define a rule, the table used the smallest ruling that let play continue:

- If a card named a non-combat test and no number was printed, roll d6 and succeed on 4+.
- If a card granted a test bonus against a named kind of obstacle, success removed or cleared the obstacle and let the acting player claim it if it was a hostile or blocking card.
- If multiple players could choose an undefined target or discard, the fixed player order was used unless the card gave another clear selector.
- Party HP could not exceed the 3-player starting value of 18.
- The first qualifying threshold-5 reward tax in a scene was assigned in fixed player order when rewards were simultaneous.
- Final-ordeal extra turns meant each player got one extra action, then enemies acted once; no additional standard draw happened.
