def longest_repeated_substring(dna: str, k: int) -> str | None:
    solutions: list[str | None] = [None]
    length = len(dna)

    for i in range(1, length):
        substring_counts: dict[str, int] = {}

        for j in range(length - i + 1):
            if (sub := dna[j : j + i]) in substring_counts:
                substring_counts[sub] = substring_counts[sub] + 1
            else:
                substring_counts[sub] = 1

            if substring_counts[sub] < k:
                continue

            if solutions[0] is None or len(solutions[0]) < len(sub):
                solutions = [sub]
            else:
                solutions.append(sub)

        if len(solutions) == 1:
            return solutions[0]

    return solutions[0]
