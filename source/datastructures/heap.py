from __future__ import annotations

import math
from dataclasses import dataclass, field

from source.datastructures.helpers.underflow import UnderflowError


def left(i: int) -> int:
    """Runtime: O(1)."""
    return 2 * i + 1


def right(i: int) -> int:
    """Runtime: O(1)."""
    return 2 * i + 2


def parent(i: int) -> int:
    """Runtime: O(1)."""
    return (i - 1) // 2


def print_heap(heap: MaxHeap | MinHeap) -> None:
    """Not part of curriculum, but useful for exams. Assumes there are
    no values smaller than -9 or greater than 99 (to look pretty💅).

    Runtime: O(n).
    """
    height = int(math.log2(heap.size)) + 1  # Didn't want a numpy dependency...
    left_space = 2**height - 2
    middle_space = 0
    idx = 0

    for level in range(height):
        print(" " * left_space, end="")

        for _ in range(2**level):
            if idx == heap.size:
                break

            print(f"{heap.heap[idx]:>2}{' ' * middle_space}", end="")
            idx += 1

        middle_space = left_space
        left_space -= 2 ** (height - level - 1)
        print()


# Could have used a Heap superclass, but wanted to follow the book.
@dataclass(slots=True)
class MaxHeap:
    """Heaps are balanced; WC = BC. Not random order, since all children
    are smaller than their parent.
    """

    heap: list[int] = field(default_factory=list, init=False)
    size: int = field(default=0, init=False, repr=False)

    def max_heapify(self, i: int) -> None:
        """Runtime: O(log(n))."""
        l = left(i)
        r = right(i)
        m = l if l < self.size and self.heap[l] > self.heap[i] else i

        if r < self.size and self.heap[r] > self.heap[m]:
            m = r

        if m != i:
            self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
            self.max_heapify(m)

    def build_max_heap(self, n: int) -> None:
        """Runtime: Θ(n)."""
        for i in range(n // 2, -1, -1):
            self.max_heapify(i)

    def max_heap_increase_key(self, x: int, k: int) -> None:
        """Runtime: O(log(n))."""
        if k < x:
            raise ValueError()

        i = self.heap.index(x)
        self.heap[i] = k

        while i and self.heap[j := parent(i)] < self.heap[i]:
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def max_heap_insert(self, key: int, n: int) -> None:
        """Runtime: O(log(n))."""
        if self.size == n:
            raise OverflowError()

        self.size += 1
        k = key
        key = float("-inf")  # type: ignore
        self.heap.append(key)
        self.max_heap_increase_key(key, k)

    def max_heap_maximum(self) -> int:
        """Runtime: Θ(1)."""
        if not self.size:
            raise UnderflowError()

        return self.heap[0]

    def max_heap_extract_max(self) -> int:
        """Runtime: O(log(n))."""
        maximum = self.max_heap_maximum()
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self.max_heapify(0)
        return maximum

    def heapsort(self, n: int) -> None:
        """Runtimes:
            BC: Θ(n).
            WC: Θ(n*log(n)).
        Stable: No.
        """
        self.build_max_heap(n)

        for i in range(n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.size -= 1
            self.max_heapify(0)


@dataclass(slots=True)
class MinHeap:
    """All children are greater than their parent."""

    heap: list[int] = field(default_factory=list)
    size: int = field(default=0, init=False, repr=False)

    def min_heapify(self, i: int) -> None:
        """Runtime: O(log(n))."""
        l = left(i)
        r = right(i)
        m = l if l < self.size and self.heap[l] < self.heap[i] else i

        if r < self.size and self.heap[r] < self.heap[m]:
            m = r

        if m != i:
            self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
            self.min_heapify(m)

    def build_min_heap(self, n: int) -> None:
        """Runtime: Θ(n)."""
        for i in range(n // 2, -1, -1):
            self.min_heapify(i)

    def min_heap_decrease_key(self, x: int, k: int) -> None:
        """Runtime: O(log(n))."""
        if k > x:
            raise ValueError()

        i = self.heap.index(x)
        self.heap[i] = k

        while i and self.heap[j := parent(i)] > self.heap[i]:
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def min_heap_insert(self, key: int, n: int) -> None:
        """Runtime: O(log(n))."""
        if self.size == n:
            raise OverflowError()

        self.size += 1
        k = key
        key = float("inf")  # type: ignore
        self.heap.append(key)
        self.min_heap_decrease_key(key, k)

    def min_heap_minimum(self) -> int:
        """Runtime: Θ(1)."""
        if not self.size:
            raise UnderflowError()

        return self.heap[0]

    def min_heap_extract_min(self) -> int:
        """Runtime: O(log(n))."""
        minimum = self.min_heap_minimum()
        self.heap[0] = self.heap.pop()
        self.size -= 1
        self.min_heapify(0)
        return minimum

    def heapsort(self, n: int) -> None:
        """Runtimes:
            BC: Θ(n).
            WC: Θ(n*log(n)).
        Stable: No.
        """
        self.build_min_heap(n)

        for i in range(n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.size -= 1
            self.min_heapify(0)
