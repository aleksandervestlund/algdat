from __future__ import annotations

from dataclasses import dataclass, field


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
        if x is not None:
            self.tree_inorder_walk(x.left)
            print(x.key)
            self.tree_inorder_walk(x.right)

    def tree_search(self, x: TreeNode | None, key: int) -> TreeNode | None:
        if x is None or x.key == key:
            return x
        if key < x.key:
            return self.tree_search(x.left, key)
        return self.tree_search(x.right, key)

    def tree_insert(self, z: TreeNode) -> None:
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

    @staticmethod
    def tree_minimum(x: TreeNode) -> TreeNode:
        while x.left is not None:
            x = x.left

        return x

    @staticmethod
    def tree_successor(x: TreeNode) -> TreeNode | None:
        if x.right is not None:
            return Tree.tree_minimum(x.right)

        y = x.parent

        while y is not None and x == y.right:
            x = y
            y = y.parent

        return y

    def transplant(self, u: TreeNode, v: TreeNode | None) -> None:
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def tree_delete(self, z: TreeNode) -> None:
        if z.left is None:
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            if (y := Tree.tree_minimum(z.right)) != z.parent:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
