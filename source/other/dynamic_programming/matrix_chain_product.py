def matrix_chain_product(p: list[int], n: int) -> int:
    """`n` is the number of matrices, `len(p)-1`.

    Runtime: Θ(n^3).
    """
    m = [[0 if i == j else float("inf") for i in range(n)] for j in range(n)]

    for l in range(1, n):
        for i in range(n - l):
            j = i + l

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                m[i][j] = min(m[i][j], q)

    return m[0][-1]  # type: ignore
