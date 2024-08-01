from source.datastructures.graph import Vertex


def print_all_pairs_shortest_paths(
    pis: list[list[Vertex | None]], i: Vertex | None, j: Vertex | None
) -> None:
    if i is None or j is None:
        return
    if not (isinstance(i.name, int) and isinstance(j.name, int)):
        return

    # Assumes that the first vertix is named 1.
    # It's weird to use the name as index, but it's what the pseudocode does.
    if i is j:
        print(i.name)
    elif pis[i.name - 1][j.name - 1] is None:
        print(f"No path from {i} to {j} exists.")
    else:
        print_all_pairs_shortest_paths(pis, i, pis[i.name - 1][j.name - 1])
        print(j.name)
