from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HuffmanNode:
    freq: int = 0
    symbol: str = ""
    left: HuffmanNode | None = None
    right: HuffmanNode | None = None
