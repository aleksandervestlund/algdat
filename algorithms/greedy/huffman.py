from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class HuffmanNode:
    freq: int = 0
    symbol: str = ""
    left: HuffmanNode | None = None
    right: HuffmanNode | None = None


def huffman(c: dict[str, int]) -> HuffmanNode:
    n = len(c)
    q = [HuffmanNode(symbol=s, freq=f) for s, f in c.items()]

    for _ in range(n - 1):
        q.sort(key=lambda x: x.freq)
        x = q.pop(0)
        y = q.pop(0)

        z = HuffmanNode(freq=x.freq + y.freq, left=x, right=y)
        q.append(z)

    return q[0]
