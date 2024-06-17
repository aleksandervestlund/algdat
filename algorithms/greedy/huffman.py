from __future__ import annotations

from dataclasses import dataclass


@dataclass
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

        z = HuffmanNode()
        x = q.pop(0)
        y = q.pop(0)

        z.left = x
        z.right = y
        z.freq = x.freq + y.freq
        q.append(z)

    return q[0]
