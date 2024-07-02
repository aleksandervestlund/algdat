from math import ceil

from exercises.exercise12.max_flow import max_flow


def item_index(j: int) -> int:
    return j + 1


def agent_category_index(c: int, i: int, n: int, m: int) -> int:
    return 1 + m + c * n + i


def agent_index(i: int, k: int, n: int, m: int) -> int:
    return 1 + m + k * n + i


def allocate(
    categories: tuple[tuple[int, tuple[int, int]], ...],
    valuations: tuple[list[int], ...],
    n: int,
    m: int,
) -> list[list[int]] | None:
    k = len(categories)
    all_items = range(m)
    n_nodes = 2 + m + n * k + n + 1
    source = 0
    sink = n_nodes - 1
    capacities = [[0] * n_nodes for _ in range(n_nodes)]

    for item in all_items:
        item_idx = item_index(item)
        capacities[source][item_idx] = 1

    for category, (threshold, items) in enumerate(categories):
        for agent, valuation in enumerate(valuations):
            agent_category_idx = agent_category_index(category, agent, n, m)
            agent_idx = agent_index(agent, k, n, m)
            capacities[agent_category_idx][agent_idx] = threshold

            for item in set(valuation) & set(items):
                item_idx = item_index(item)
                capacities[item_idx][agent_category_idx] = 1

    flow_req = 0

    for agent, valuation in enumerate(valuations):
        prop = ceil(len(valuation) / n)
        flow_req += prop
        agent_idx = agent_index(agent, k, n, m)
        capacities[agent_idx][sink] = prop

    flows, total_flow = max_flow(0, n_nodes - 1, n_nodes, capacities)

    if total_flow != flow_req:
        return None

    allocation = []

    for agent in range(n):
        bundle = []

        for category, (_, items) in enumerate(categories):
            for item in items:
                item_idx = item_index(item)
                agent_category_idx = agent_category_index(
                    category, agent, n, m
                )

                if flows[item_idx][agent_category_idx] == 1:
                    bundle.append(item)

        allocation.append(bundle)

    return allocation
