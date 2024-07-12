from source.datastructures.graph import Graph, Status, Vertex
from source.datastructures.queue import Queue


def bipartite(g: Graph) -> bool:
    """Determines if a graph is bipartite, also known as 2-colorable.
    Not part of curriculum, but useful for exams.

    Runtime: O(V + E).

    :param Graph g: The graph.
    :raises ValueError: The graph is not undirected.
    :return bool: Whether the graph is bipartite.
    """
    if any((v, u) not in g.E for u, v in g.E):  # O(E).
        raise ValueError("The graph is not undirected.")

    q = Queue(len(g.adj))
    s = next(iter(g.adj))  # Need to start somewhere.
    s.color = Status.VISITING

    while not q.is_empty():
        u: Vertex = q.dequeue()
        adj_color = (
            Status.VISITED if u.color is Status.VISITING else Status.VISITING
        )

        for v in g.adj[u]:
            if v.color is u.color:
                return False

            v.color = adj_color
            q.enqueue(v)

    return True
