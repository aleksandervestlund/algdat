UP_ARROW = "↑"
LEFT_ARROW = "←"
UP_LEFT_ARROW = "↖"


def lcs_length(
    x: str, y: str, m: int, n: int
) -> tuple[list[list[int]], list[list[str]]]:
    b = [[""] * n for _ in range(m)]
    c = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        c[i][0] = 0

    for j in range(n):
        c[0][j] = 0

    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                b[i][j] = UP_LEFT_ARROW
            elif c[i][j + 1] >= c[i + 1][j]:
                c[i + 1][j + 1] = c[i][j + 1]
                b[i][j] = UP_ARROW
            else:
                c[i + 1][j + 1] = c[i + 1][j]
                b[i][j] = LEFT_ARROW

    return c, b


def print_lcs(b: list[list[str]], x: str, i: int, j: int) -> None:
    if i == 0 or j == 0:
        return

    if b[i - 1][j - 1] == UP_LEFT_ARROW:
        print_lcs(b, x, i - 1, j - 1)
        print(x[i - 1], end="")
    elif b[i - 1][j - 1] == UP_ARROW:
        print_lcs(b, x, i - 1, j)
    else:
        print_lcs(b, x, i, j - 1)
