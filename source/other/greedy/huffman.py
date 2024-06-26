from __future__ import annotations

from typing import Any

from source.datastructures.huffman_node import HuffmanNode
from source.datastructures.priority_queue import PriorityQueue


def huffman(c: dict[Any, float]) -> HuffmanNode:
    q = PriorityQueue(key="freq")

    for s, f in c.items():
        q.insert(HuffmanNode(symbol=s, freq=f))

    while len(q) > 1:
        x: HuffmanNode = q.extract_min()
        y: HuffmanNode = q.extract_min()

        z = HuffmanNode(left=x, right=y, freq=x.freq + y.freq)
        q.insert(z)

    return q.extract_min()
