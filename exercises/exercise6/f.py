from math import comb


def f(x: int, y: int) -> int:
    return comb(x + y - 2, x - 1)
