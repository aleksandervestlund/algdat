from __future__ import annotations

from source.datastructures.graph import Vertex


def make_set(x: Vertex) -> None:
    x.p = x
    x.rank = 0


def find_set(x: Vertex | None) -> Vertex | None:
    if x is None:
        return x

    if x is not x.p:
        x.p = find_set(x.p)

    return x.p


def union(x: Vertex | None, y: Vertex | None) -> None:
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x is not None and root_y is not None:
        link(root_x, root_y)


def link(x: Vertex, y: Vertex) -> None:
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y

        if x.rank == y.rank:
            y.rank += 1
