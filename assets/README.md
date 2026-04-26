# Assets

This folder is reserved for canonical art, print-ready components, and other real production assets once the prototype starts locking.

For now, experimental or one-off material should stay out of this folder unless it is intended to become part of the actual shipped prototype.

Current production files:

- [card-text-fit-report.md](./card-text-fit-report.md): generated report checking current card text against the standard layout in `defines/card-layout.md`.
- [card-atlas-definition.md](./card-atlas-definition.md): letter-size atlas plan for printing and cutting Edition 0 cards, including card size, cut grid, sheet IDs, and per-sheet card assignments.
- [print-and-bundle-package.md](./print-and-bundle-package.md): complete Edition 0 physical package checklist, including cards, rules sheets, paper widgets, tokens, dice, bundling groups, and playability gaps.

Production scripts:

- [scripts/calculate_card_layout.py](./scripts/calculate_card_layout.py): reads the atlas definition and regenerates `defines/card-layout.md`.
- [scripts/check_card_text_fit.py](./scripts/check_card_text_fit.py): reads `defines/card-layout.md` and the card `.txt` files, then regenerates `card-text-fit-report.md`.
