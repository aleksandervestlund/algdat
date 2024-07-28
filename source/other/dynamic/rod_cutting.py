R: list[int] = []


def cut_rod(p: list[int], n: int) -> int:
    """Runtime: Θ(2^n)."""
    if not n:
        return 0

    q = 0

    for i in range(n):
        t = p[i] + cut_rod(p, n - i - 1)
        q = max(q, t)

    return q


def bottom_up_rod_cut(p: list[int], n: int) -> int:
    """Runtime: Θ(n^2)."""
    r = [0] * (n + 1)

    for j in range(1, n + 1):
        q = 0

        for i in range(1, j + 1):
            t = p[i - 1] + r[j - i]
            q = max(q, t)

        r[j] = q

    return r[n]


def memoized_cut_rod_aux(p: list[int], n: int, r: list[int]) -> int:
    """Runtime: Θ(n^2)."""
    if r[n] >= 0:
        return r[n]

    if not n:
        q = 0
    else:
        q = -1

        for i in range(n):
            t = p[i] + memoized_cut_rod_aux(p, n - i - 1, r)
            q = max(q, t)

    r[n] = q
    return q


def memoized_cut_rod(p: list[int], n: int) -> int:
    """Runtime: Θ(n^2)."""
    global R
    if not R:
        R = [-1] * (n + 1)

    return memoized_cut_rod_aux(p, n, R)
