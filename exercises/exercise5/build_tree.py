from exercises.exercise5.node import Node


def build_tree(dna_sequences: list[str]) -> Node:
    root = Node()
    current_node = root

    for sequence in dna_sequences:
        current_node = root

        for protein in sequence:
            if protein not in current_node.children:
                current_node.children[protein] = Node()

            current_node = current_node.children[protein]

        current_node.count += 1

    return root
