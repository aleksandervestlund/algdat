from source.datastructures.graph import Graph, Status, Vertex
from source.datastructures.queue import Queue


def bipartite(g: Graph) -> bool:
    """Determines whether a graph is bipartite, also known as
    2-colorable.
    No given pseudocode and not part of curriculum, but common on exams.

    Runtime: O(V+E).

    :param Graph g: The graph.
    :raises ValueError: The graph is not undirected.
    :return bool: Whether the graph is bipartite.
    """
    if any((v, u) not in g.E for u, v in g.E):
        raise ValueError("The graph is not undirected.")

    q = Queue(len(g.V))
    s = next(u for u in g.V if u.color is Status.UNVISITED)
    s.color = Status.VISITING

    while not q.is_empty():
        u: Vertex = q.dequeue()
        adj_color = (
            Status.VISITED if u.color is Status.VISITING else Status.VISITING
        )

        for v in g.adj[u]:
            if v.color is adj_color:
                continue
            if v.color is u.color:
                return False

            v.color = adj_color
            q.enqueue(v)

    # If the graph is disconnected, we need to check the other components.
    if any(v.color is Status.UNVISITED for v in g.adj):
        return bipartite(g)
    return True
