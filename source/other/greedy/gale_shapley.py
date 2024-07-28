def gale_shapley(
    men: list[list[int]], women: list[list[int]], male_oriented: bool = False
) -> dict[int, int]:
    """Runtime: O(n^2)."""
    if male_oriented:
        men, women = women, men

    free_ws = set(range(len(women)))

    # {man: woman}. More efficient to check if man is engaged.
    engagements: dict[int, int] = {}

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

    # Want to return {woman: man}, since it is female-oriented.
    return {w: m for m, w in engagements.items()}
