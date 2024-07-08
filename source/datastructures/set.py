from __future__ import annotations

from source.datastructures.graph import Vertex


#        {0, n ≤ 2
#        {1, n = 3
# α(n) = {2, 4 ≤ n ≤ 7
#        {3, 8 ≤ n ≤ 2047
#        {4, 2048 ≤ n ≤ 16^512
# α(n) = O(log(n))


def make_set(x: Vertex) -> None:
    """O(1)."""
    x.p = x
    x.rank = 0


def find_set(x: Vertex | None) -> Vertex | None:
    """O(log(V))."""
    if x is None:
        return x

    if x is not x.p:
        x.p = find_set(x.p)

    return x.p


def union(x: Vertex | None, y: Vertex | None) -> None:
    """O(log(V))."""
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x is not None and root_y is not None:
        link(root_x, root_y)


def link(x: Vertex, y: Vertex) -> None:
    """O(1)."""
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        y.rank += x.rank == y.rank
