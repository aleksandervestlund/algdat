def gale_shapley(
    men: list[list[int]], women: list[list[int]]
) -> dict[int, int]:
    """Female-oriented Gale-Shapley algorithm.

    Runtime: O(n^2).
    """
    n = len(women)
    free_ws = set(range(n))
    engagements: dict[int, int] = {}  # man: woman

    while free_ws:
        w = free_ws.pop()

        for m in women[w]:
            priority = men[m]

            if (wife := engagements.get(m)) is None:
                engagements[m] = w
                break
            if priority.index(w) < priority.index(wife):
                free_ws.add(wife)
                engagements[m] = w
                break

    return {w: m for m, w in engagements.items()}  # woman: man
