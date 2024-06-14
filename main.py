from algorithms.datastructures.chained_hash_table import ChainedHashTable
from algorithms.datastructures.linked_list import LinkedList
from algorithms.datastructures.node import Node


def main() -> None:
    x = Node(1)
    y = Node(2)
    z = Node(3)
    a = Node(12)
    b = Node(13)
    c = Node(14)
    arr = LinkedList()
    arr.prepend(x)
    arr.prepend(y)
    arr.insert(z, x)
    print(arr)

    table = ChainedHashTable(10)
    table.insert(x)
    table.insert(y)
    table.insert(z)
    table.insert(a)
    table.insert(b)
    table.insert(c)
    print(table)


if __name__ == "__main__":
    main()
