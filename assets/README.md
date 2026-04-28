# Assets

This folder holds canonical art, print-ready components, generated assets, and production manifests for the Edition 0 prototype.

Experimental or one-off material should stay out of this folder unless it is intended to become part of the actual shipped prototype.

Current production files:

- [card-art/AI_ART_HANDOFF.md](./card-art/AI_ART_HANDOFF.md): handoff list for generating final AI card art and moving it into the renderer's expected paths.
- [card-art/AI_ART_SESSION_GROUPS.md](./card-art/AI_ART_SESSION_GROUPS.md): current grouped AI-art session plan.
- [fedex-printing-plan.md](./fedex-printing-plan.md): current FedEx print setup, email-size PDF split, and proofing notes.
- [printed-materials-index.md](./printed-materials-index.md): exact read list for printed-materials-only playtests, including what to avoid until after the session.
- [widget-and-token-definitions.md](./widget-and-token-definitions.md): player-facing definitions for the table board, escalation meter, party HP tracker, dice, tokens, and open widget gaps.
- [board-layout-definition.md](./board-layout-definition.md): generated three-page table-board layout, page assembly order, and board footprint rationale.
- [card-text-fit-report.md](./card-text-fit-report.md): generated report checking current card text against the standard layout in `defines/card-layout.md`.
- [card-atlas-definition.md](./card-atlas-definition.md): letter-size atlas plan for printing and cutting Edition 0 cards, including card size, cut grid, sheet IDs, and per-sheet card assignments.
- [print-and-bundle-package.md](./print-and-bundle-package.md): complete Edition 0 physical package checklist, including cards, rules sheets, paper widgets, tokens, dice, bundling groups, and playability gaps.

Production scripts:

- [scripts/build_card_atlases.py](./scripts/build_card_atlases.py): builds printable front and back atlas PNGs from generated individual card fronts and back textures.
- [scripts/build_duplex_card_atlas_pdf.py](./scripts/build_duplex_card_atlas_pdf.py): builds the complete duplex atlas PDF and two email-sized split PDFs from generated front/back atlas PNGs.
- [scripts/calculate_card_layout.py](./scripts/calculate_card_layout.py): reads the atlas definition and regenerates `defines/card-layout.md`.
- [scripts/card_rendering_common.py](./scripts/card_rendering_common.py): shared parser, layout, font, and drawing helpers for the card rendering pipeline.
- [scripts/check_card_art_integrity.py](./scripts/check_card_art_integrity.py): scans final card art for exact and near-duplicate images.
- [scripts/check_card_text_fit.py](./scripts/check_card_text_fit.py): reads `defines/card-layout.md` and the card `.txt` files, then regenerates `card-text-fit-report.md`.
- [scripts/generate_card_backs.py](./scripts/generate_card_backs.py): creates generated card-back texture PNGs.
- [scripts/generate_card_frames.py](./scripts/generate_card_frames.py): creates reusable deck-specific common and rare card-frame PNGs.
- [scripts/generate_printable_cards.py](./scripts/generate_printable_cards.py): renders individual front PNGs for defined cards, class references, and utility proxy cards.
- [scripts/generate_quick_start_guide.py](./scripts/generate_quick_start_guide.py): renders the quick-start guide PDF from the player-facing markdown.
- [scripts/generate_table_board.py](./scripts/generate_table_board.py): renders the three-page printable table organizer board PNGs and PDF.
- [scripts/print_pdf_common.py](./scripts/print_pdf_common.py): shared multipage-PDF writer used by print-output generators.

Generated outputs:

- `card-art/final/<deck-slug>/<card-id>.png`: final AI art inputs consumed by the renderer.
- `card-art/incoming/`: temporary drop zone for raw or alternate AI art before final selection.
- `generated/card-fronts/`: individual rendered card-front PNGs.
- `generated/atlases/fronts/` and `generated/atlases/backs/`: printable letter-size atlas PNGs.
- `generated/board/`: full table-board PNG and the three printable page slices.
- `generated/card-frames/` and `generated/card-backs/`: reproducible renderer support images; frames include common and rare variants for each card layout.
- `generated/guide/quick-start-guide.pdf`: generated printable quick-start guide.
- `generated/print/`: generated complete/split duplex atlas PDFs and the three-page board PDF.
