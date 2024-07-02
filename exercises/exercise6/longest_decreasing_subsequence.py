def longest_decreasing_subsequence(s: list[int]) -> list[int]:
    length = len(s)
    lds = [1] * length
    prev = [-1] * length
    max_length = 1

    for i in range(1, length):
        si = s[i]

        for j in range(i):
            sj = s[j]

            if si < sj and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
                prev[i] = j

                if lds[i] > max_length:
                    max_length = lds[i]
                    max_length_index = i

    if max_length == 1:
        return [s[0]]

    result = []
    current_index = max_length_index

    while current_index != -1:
        result.insert(0, s[current_index])
        current_index = prev[current_index]

    return result
