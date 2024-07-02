def string_match(dna: str, segments: list[str]) -> int:
    amount = 0

    for segment in segments:
        idx = dna.find(segment)

        while idx != -1:
            amount += 1
            idx = dna.find(segment, idx + 1)

    return amount
