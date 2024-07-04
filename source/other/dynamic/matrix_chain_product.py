def matrix_chain_product(p: list[int], n: int) -> int:
    m = [[0] * n for _ in range(n)]

    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            m[i][j] = float("inf")  # type: ignore

            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                m[i][j] = min(m[i][j], q)

    return m[0][-1]
