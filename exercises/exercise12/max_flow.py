from collections import deque


def find_augmenting_path(
    source: int,
    sink: int,
    nodes: int,
    flows: list[list[int]],
    capacities: list[list[int]],
) -> list[int] | None:
    def create_path(source: int, sink: int, parent: list[int]) -> list[int]:
        node = sink
        path = [sink]

        while node != source:
            node = parent[node]
            path.insert(0, node)

        return path

    discovered = [False] * nodes
    parent = [0] * nodes
    queue = deque()
    queue.append(source)

    while queue:
        if (node := queue.popleft()) == sink:
            return create_path(source, sink, parent)

        for neighbour in range(nodes):
            if (
                not discovered[neighbour]
                and flows[node][neighbour] < capacities[node][neighbour]
            ):
                queue.append(neighbour)
                discovered[neighbour] = True
                parent[neighbour] = node

    return None


def send_flow(path: list[int], flow: int, flows: list[list[int]]) -> None:
    for i in range(1, len(path)):
        u, v = path[i - 1], path[i]
        flows[u][v] += flow
        flows[v][u] -= flow


def max_path_flow(
    path: list[int], flows: list[list[int]], capacities: list[list[int]]
) -> int:
    flow = float("inf")

    for i in range(1, len(path)):
        u, v = path[i - 1], path[i]
        flow = min(flow, capacities[u][v] - flows[u][v])

    return flow  # type: ignore


def max_flow(
    source: int, sink: int, nodes: int, capacities: list[list[int]]
) -> tuple[list[list[int]], int]:
    flows = [[0] * nodes for _ in range(nodes)]
    total_flow = 0
    path = find_augmenting_path(source, sink, nodes, flows, capacities)

    while path is not None:
        flow = max_path_flow(path, flows, capacities)
        send_flow(path, flow, flows)
        total_flow += flow
        path = find_augmenting_path(source, sink, nodes, flows, capacities)

    return flows, total_flow
