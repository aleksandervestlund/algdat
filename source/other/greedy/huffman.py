from __future__ import annotations

from dataclasses import dataclass

from source.datastructures.minimum_priority_queue import (
    MinimumPriorityQueue,
)


@dataclass(frozen=True, slots=True)
class HuffmanNode:
    freq: int = 0
    symbol: str = ""
    left: HuffmanNode | None = None
    right: HuffmanNode | None = None


def huffman(c: dict[str, int]) -> HuffmanNode:
    q = MinimumPriorityQueue(key="freq")

    for s, f in c.items():
        q.insert(HuffmanNode(symbol=s, freq=f))

    while len(q) > 1:
        x = q.extract_min()
        y = q.extract_min()

        z = HuffmanNode(left=x, right=y, freq=x.freq + y.freq)
        q.insert(z)

    return q.extract_min()
