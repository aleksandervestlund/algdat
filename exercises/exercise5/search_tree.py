from __future__ import annotations

from exercises.exercise5.node import Node


def search_tree(root: Node, dna: str) -> int:
    current = root

    for sequence in dna:
        if sequence not in current.children:
            return 0

        current = current.children[sequence]

    return current.count
