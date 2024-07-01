def knapsack(n: int, W: int, w: list[int], v: list[int]) -> int:
    k = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(1, W + 1):
            x = k[i][j]

            if j < w[i]:
                k[i + 1][j] = x
            else:
                y = k[i][j - w[i]] + v[i]
                k[i + 1][j] = max(x, y)

    return k[n][W]
