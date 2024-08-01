from __future__ import annotations

from dataclasses import dataclass, field


def tree_minimum(x: TreeNode) -> TreeNode:
    """Runtime: O(h)."""
    while x.left is not None:
        x = x.left

    return x


def tree_maximum(x: TreeNode) -> TreeNode:
    """Runtime: O(h)."""
    while x.right is not None:
        x = x.right

    return x


def tree_successor(x: TreeNode) -> TreeNode | None:
    """Runtime: O(h)."""
    if x.right is not None:
        return tree_minimum(x.right)

    y = x.parent

    while y is not None and x is y.right:
        x = y
        y = y.parent

    return y


@dataclass(slots=True)
class TreeNode:
    key: int
    parent: TreeNode | None = field(default=None, repr=False)
    left: TreeNode | None = None
    right: TreeNode | None = None


@dataclass(slots=True)
class Tree:
    root: TreeNode | None = None

    def tree_inorder_walk(self, x: TreeNode | None) -> None:
        """Runtime: Θ(n)."""
        if x is not None:
            self.tree_inorder_walk(x.left)
            print(x.key)
            self.tree_inorder_walk(x.right)

    def tree_preorder_walk(self, x: TreeNode | None) -> None:
        """Not part of curriculum.

        Runtime: Θ(n).
        """
        if x is not None:
            print(x.key)
            self.tree_preorder_walk(x.left)
            self.tree_preorder_walk(x.right)

    def tree_postorder_walk(self, x: TreeNode | None) -> None:
        """Not part of curriculum.

        Runtime: Θ(n).
        """
        if x is not None:
            self.tree_postorder_walk(x.left)
            self.tree_postorder_walk(x.right)
            print(x.key)

    def tree_search(self, x: TreeNode | None, key: int) -> TreeNode | None:
        """Runtime: O(h)."""
        if x is None or x.key == key:
            return x
        if key < x.key:
            return self.tree_search(x.left, key)
        return self.tree_search(x.right, key)

    def tree_insert(self, z: TreeNode) -> None:
        """Runtime: O(h)."""
        x = self.root
        y = None

        while x is not None:
            y = x
            x = x.left if z.key < x.key else x.right

        z.parent = y

        if y is None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def transplant(self, u: TreeNode, v: TreeNode | None) -> None:
        """Runtime: O(1)."""
        if u.parent is None:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def tree_delete(self, z: TreeNode) -> None:
        """Runtime: O(h)."""
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            if (y := tree_minimum(z.right)) is not z.parent:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

    def height(self) -> int:
        """Not part of curriculum and no given pseudocode.

        Runtime: O(n).
        """

        def _height(node: TreeNode | None) -> int:
            if node is None:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)
