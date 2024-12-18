from source.datastructures.graph import Vertex


def relax(u: Vertex, v: Vertex, w: dict[tuple[Vertex, Vertex], float]) -> None:
    """Runtime: O(1)."""
    if v.d > (distance := u.d + w[(u, v)]):
        v.d = distance
        v.pi = u
