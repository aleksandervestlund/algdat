def largest_cuboid(x: list[list[int]]) -> int:
    n = len(x)
    potential_rectangles: set[tuple[tuple[int, int], tuple[int, int]]] = {
        ((0, 0), (n - 1, n - 1))
    }
    coordinates = [(i, j) for i in range(n) for j in range(n)]
    coordinates = sorted(coordinates, key=lambda c: x[c[0]][c[1]])
    max_volume = 0

    for c in coordinates:
        to_split: list[tuple[tuple[int, int], tuple[int, int]]] = []

        for rectangle in potential_rectangles:
            if (
                rectangle[0][0] <= c[0] <= rectangle[1][0]
                and rectangle[0][1] <= c[1] <= rectangle[1][1]
            ):
                to_split.append(rectangle)
                volume = (
                    (rectangle[1][0] - rectangle[0][0] + 1)
                    * (rectangle[1][1] - rectangle[0][1] + 1)
                    * x[c[0]][c[1]]
                )
                max_volume = max(max_volume, volume)

        for rectangle in to_split:
            potential_rectangles.remove(rectangle)

            if c[0] > rectangle[0][0]:
                rect = (
                    (rectangle[0][0], rectangle[0][1]),
                    (c[0] - 1, rectangle[1][1]),
                )
                potential_rectangles.add(rect)

            if c[1] > rectangle[0][1]:
                rect = (
                    (rectangle[0][0], rectangle[0][1]),
                    (rectangle[1][0], c[1] - 1),
                )
                potential_rectangles.add(rect)

            if c[0] < rectangle[1][0]:
                rect = (
                    (c[0] + 1, rectangle[0][1]),
                    (rectangle[1][0], rectangle[1][1]),
                )
                potential_rectangles.add(rect)

            if c[1] < rectangle[1][1]:
                rect = (
                    (rectangle[0][0], c[1] + 1),
                    (rectangle[1][0], rectangle[1][1]),
                )
                potential_rectangles.add(rect)

    return max_volume
