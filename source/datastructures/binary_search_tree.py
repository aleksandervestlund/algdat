from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class BinarySearchTreeNode:
    value: int
    left: BinarySearchTreeNode | None = None
    right: BinarySearchTreeNode | None = None


@dataclass(slots=True)
class BinarySearchTree:
    root: BinarySearchTreeNode | None = None

    def insert(self, value: int) -> None:
        """No given pseudocode.

        Runtime: O(h).
        """
        new_node = BinarySearchTreeNode(value)
        parent = None
        child = self.root

        while child is not None:
            parent = child
            child = child.left if new_node.value < child.value else child.right

        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

    def height(self) -> int:
        """No given pseudocode.

        Runtime: O(n).
        """

        def _height(node: BinarySearchTreeNode | None) -> int:
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)
