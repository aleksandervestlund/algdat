from source.datastructures.graph import Graph, Vertex


def verify_short_path(
    g: Graph, u: Vertex, v: Vertex, k: int, p: list[Vertex], n: int
) -> bool:
    if n - 1 > k:
        return False
    if p[0] is not u or p[-1] is not v:
        return False
    return not any((p[i], p[i + 1]) not in g.E for i in range(n - 1))
    # for i in range(0, n - 1):
    #     if (p[i], p[i + 1]) not in g.E:
    #         return False
    #
    # return True
