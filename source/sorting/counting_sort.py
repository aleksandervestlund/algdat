def counting_sort(a: list[int], n: int, k: int) -> list[int]:
    """Assumes no negative numbers in the array.

    Runtime: Θ(n+k).
    Stable: Yes.
    """
    _validate_range(a, k)  #! Not part of pseudocode.

    b = [0] * n
    c = [0] * (k + 1)

    for i in range(n):
        c[a[i]] += 1

    for i in range(1, k + 1):
        c[i] += c[i - 1]

    for i in range(n - 1, -1, -1):
        b[c[a[i]] - 1] = a[i]
        c[a[i]] -= 1

    return b


def _validate_range(a: list[int], k: int) -> None:
    if not all(0 <= x <= k for x in a):
        raise ValueError("Elements should be in the range [0, k].")
