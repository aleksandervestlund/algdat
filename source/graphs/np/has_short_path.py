from source.datastructures.graph import Graph, Vertex
from source.graphs.traversal.bfs import bfs


def has_short_path(g: Graph, u: Vertex, v: Vertex, k: int) -> bool:
    bfs(g, u)
    return v.d <= k
