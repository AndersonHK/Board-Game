#!/usr/bin/env python3
"""Shared PDF output helpers for generated print assets."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path

from PIL import Image


def save_multipage_pdf(path: Path, pages: Sequence[Image.Image], dpi: int) -> None:
    if not pages:
        raise ValueError(f"No pages to write for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    first, rest = pages[0], list(pages[1:])
    first.save(path, save_all=True, append_images=rest, resolution=dpi)
    print(f"Wrote {path} ({len(pages)} pages)")
