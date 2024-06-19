def recursive_activity_selector(
    s: list[int], f: list[int], k: int, n: int
) -> set[int]:
    m = k + 1

    while m < n and s[m] < f[k]:
        m += 1

    if m < n:
        return {0, m} | recursive_activity_selector(s, f, m, n)
    return set()


def greedy_activity_selector(s: list[int], f: list[int], n: int) -> set[int]:
    a = {0}
    k = 0

    for m in range(1, n):
        if s[m] >= f[k]:
            a.add(m)
            k = m

    return a
