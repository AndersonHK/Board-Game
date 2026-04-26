# Assets

This folder is reserved for canonical art, print-ready components, and other real production assets once the prototype starts locking.

For now, experimental or one-off material should stay out of this folder unless it is intended to become part of the actual shipped prototype.

Current production files:

- [card-art/AI_ART_HANDOFF.md](./card-art/AI_ART_HANDOFF.md): handoff list for generating final AI card art and moving it into the renderer's expected paths.
- [printed-materials-index.md](./printed-materials-index.md): exact read list for printed-materials-only playtests, including what to avoid until after the session.
- [widget-and-token-definitions.md](./widget-and-token-definitions.md): player-facing definitions for the table board, escalation meter, party HP tracker, dice, tokens, and open widget gaps.
- [board-layout-definition.md](./board-layout-definition.md): generated three-page table-board layout, page assembly order, and board footprint rationale.
- [card-text-fit-report.md](./card-text-fit-report.md): generated report checking current card text against the standard layout in `defines/card-layout.md`.
- [card-atlas-definition.md](./card-atlas-definition.md): letter-size atlas plan for printing and cutting Edition 0 cards, including card size, cut grid, sheet IDs, and per-sheet card assignments.
- [print-and-bundle-package.md](./print-and-bundle-package.md): complete Edition 0 physical package checklist, including cards, rules sheets, paper widgets, tokens, dice, bundling groups, and playability gaps.

Production scripts:

- [scripts/build_card_atlases.py](./scripts/build_card_atlases.py): builds front-only printable atlas PNGs from generated individual card fronts.
- [scripts/calculate_card_layout.py](./scripts/calculate_card_layout.py): reads the atlas definition and regenerates `defines/card-layout.md`.
- [scripts/card_rendering_common.py](./scripts/card_rendering_common.py): shared parser, layout, font, and drawing helpers for the card rendering pipeline.
- [scripts/check_card_text_fit.py](./scripts/check_card_text_fit.py): reads `defines/card-layout.md` and the card `.txt` files, then regenerates `card-text-fit-report.md`.
- [scripts/generate_card_backs.py](./scripts/generate_card_backs.py): creates optional generated card-back texture PNGs.
- [scripts/generate_card_frames.py](./scripts/generate_card_frames.py): creates reusable deck-specific common and rare card-frame PNGs.
- [scripts/generate_printable_cards.py](./scripts/generate_printable_cards.py): renders individual front PNGs for defined cards, class references, and utility proxy cards.
- [scripts/generate_table_board.py](./scripts/generate_table_board.py): renders the three-page printable table organizer board.

Generated outputs:

- `card-art/final/<deck-slug>/<card-id>.png`: final AI art inputs consumed by the renderer.
- `card-art/incoming/`: temporary drop zone for raw or alternate AI art before final selection.
- `generated/card-fronts/`: individual rendered card-front PNGs.
- `generated/atlases/fronts/`: front-only printable letter-size atlas PNGs.
- `generated/board/`: full table-board PNG and the three printable page slices.
- `generated/card-frames/` and `generated/card-backs/`: reproducible renderer support images; frames include common and rare variants for each card layout.
