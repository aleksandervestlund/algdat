from typing import Any

from source.datastructures.huffman_node import HuffmanNode
from source.datastructures.priority_queue import PriorityQueue


def huffman(c: dict[Any, float]) -> HuffmanNode:
    """The root node is not counted when calculating the height of the
    tree.

    Runtime: O(n*log(n)).
    """
    q = PriorityQueue(key="freq")

    for s, f in c.items():
        z = HuffmanNode(symbol=s, freq=f)
        q.insert(z)

    while len(q) > 1:
        x: HuffmanNode = q.extract_min()
        y: HuffmanNode = q.extract_min()

        z = HuffmanNode(left=x, right=y, freq=x.freq + y.freq)
        q.insert(z)

    return q.extract_min()
