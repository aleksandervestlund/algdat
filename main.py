from algorithms.datastructures.graph import Graph, Vertex
from algorithms.graphs.traversal.bfs import bfs
from algorithms.graphs.traversal.dfs import dfs, iterative_dfs_visit


def main() -> None:
    graph = Graph()
    one = Vertex(1)
    two = Vertex(2)
    three = Vertex(3)
    four = Vertex(4)
    five = Vertex(5)
    six = Vertex(6)
    seven = Vertex(7)
    eight = Vertex(8)
    nine = Vertex(9)

    graph.adj = {
        one: {two},
        two: {three, four},
        three: {five, seven},
        four: {five},
        five: {six},
        six: {seven},
        seven: {eight},
        eight: {four, six},
        nine: {eight},
    }

    print(graph)
    bfs(graph, one)
    print()
    print(graph)


if __name__ == "__main__":
    main()
