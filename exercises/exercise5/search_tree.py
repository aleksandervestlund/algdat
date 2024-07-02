from __future__ import annotations

from exercises.exercise5.node import Node


def search_tree(root: Node, dna: str) -> int:
    current_node = root
    for sequence in dna:
        if sequence not in current_node.children:
            return 0

        current_node = current_node.children[sequence]

    return current_node.count
