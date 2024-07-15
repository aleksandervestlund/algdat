def knapsack(n: int, W: int, w: list[int], v: list[int]) -> int:
    """NP-complete problem. Also known as 0-1, or binary, knapsack
    problem.

    Runtime: Θ(n*W)=Θ(n*2^m).
    """
    if n == 0:
        return 0

    x = knapsack(n - 1, W, w, v)

    if w[n - 1] > W:
        return x

    y = knapsack(n - 1, W - w[n - 1], w, v) + v[n - 1]
    return max(x, y)


def knapsack_marked(n: int, W: int, w: list[int], v: list[int]) -> int:
    """NP-complete problem.

    Runtime: Θ(n*W)=Θ(n*2^m).
    """
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
