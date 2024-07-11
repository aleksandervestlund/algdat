def gale_shapley(
    men: list[list[int]], women: list[list[int]]
) -> dict[int, int]:
    n = len(women)
    free_ws = set(range(n))
    engagements: dict[int, int] = {}  # woman: man

    while free_ws:
        w = free_ws.pop()

        for m in women[w]:
            priority = men[m]
            wife = next(
                (woman for woman, man in engagements.items() if man == m),
                None,
            )

            if wife is None:
                engagements[w] = m
            elif priority.index(w) < priority.index(wife):
                free_ws.add(wife)
                engagements.pop(wife)
                engagements[w] = m

    return engagements
