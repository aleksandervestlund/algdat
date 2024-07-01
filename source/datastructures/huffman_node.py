from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class HuffmanNode:
    freq: float
    symbol: Any = ""
    left: HuffmanNode | None = None
    right: HuffmanNode | None = None
