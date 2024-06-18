from enum import Enum


class Arrow(Enum):
    UP = "↑"
    LEFT = "←"
    UP_LEFT = "↖"
    EMPTY = ""


def lcs_length(
    x: str, y: str, m: int, n: int
) -> tuple[list[list[int]], list[list[Arrow]]]:
    b = [[Arrow.EMPTY] * n for _ in range(m)]
    c = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        c[i][0] = 0

    for j in range(n):
        c[0][j] = 0

    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                b[i][j] = Arrow.UP_LEFT
            elif c[i][j + 1] >= c[i + 1][j]:
                c[i + 1][j + 1] = c[i][j + 1]
                b[i][j] = Arrow.UP
            else:
                c[i + 1][j + 1] = c[i + 1][j]
                b[i][j] = Arrow.LEFT

    return c, b


def print_lcs(b: list[list[Arrow]], x: str, i: int, j: int) -> None:
    if i == 0 or j == 0:
        return

    if b[i - 1][j - 1] is Arrow.UP_LEFT:
        print_lcs(b, x, i - 1, j - 1)
        print(x[i - 1], end="")
    elif b[i - 1][j - 1] is Arrow.UP:
        print_lcs(b, x, i - 1, j)
    else:
        print_lcs(b, x, i, j - 1)
