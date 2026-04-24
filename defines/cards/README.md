# Card Defines

This folder holds the canonical first-pass card data for the printable vertical slice.

Design goals for this format:

- human-readable in a normal text editor
- machine-readable by a later Python script
- one template per deck
- one plain text file per card
- every printed field that communicates stats, costs, rules text, and flavor text must exist in the card file

## Format Rule

Every card file uses plain text `Field: Value` pairs.

Long text fields may continue on the next lines if those lines are indented by two spaces.

Required fields should remain in template order so later scripts can parse them predictably.

## Deck Folders

- [quest-deck/](./quest-deck/): quest cards and quest templates
- [encounter-deck/](./encounter-deck/): random encounters and scripted ordeal cards
- [resource-deck/](./resource-deck/): player action, summon, setup, and enchantment cards
- [creature-deck/](./creature-deck/): enemies, bosses, artifacts, enchantments, and allied summon targets
- [agenda-deck/](./agenda-deck/): secret agenda cards

## Card Writing Rules

- `Card ID` should be unique, lowercase, and dash-separated.
- `Display Name` is the printed title.
- `Treasure Value` should be present on every scored card.
- `Rules Text` should match what the player needs to execute at the table.
- `Flavor Text` is optional for execution, but should exist when it belongs on the printed card.
- `Art Brief` is not required to print the rules box, but is included so a later generation pipeline can match card data to art direction.

## Promotion Rule

- These files are canonical only because they are written here intentionally.
- No file from `temp/playtests/` should be copied into this folder as canon without explicit user approval.
