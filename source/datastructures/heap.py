from dataclasses import dataclass, field

from source.datastructures.helpers.underflow import UnderflowError


def left(i: int) -> int:
    return 2 * i + 1


def right(i: int) -> int:
    return 2 * i + 2


def parent(i: int) -> int:
    return (i - 1) // 2


@dataclass(slots=True)
class MaxHeap:
    heap: list[int] = field(default_factory=list)
    size: int = field(default=0, init=False, repr=False)

    def max_heapify(self, i: int) -> None:
        l = left(i)
        r = right(i)
        m = l if l < self.size and self.heap[l] > self.heap[i] else i

        if r < self.size and self.heap[r] > self.heap[m]:
            m = r

        if m != i:
            self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
            self.max_heapify(m)

    def build_max_heap(self, n: int) -> None:
        for i in range(n // 2, -1, -1):
            self.max_heapify(i)

    def max_heap_increase_key(self, x: int, k: int) -> None:
        if k < x:
            raise ValueError()

        i = self.heap.index(x)
        self.heap[i] = k

        while i and self.heap[(j := parent(i))] < self.heap[i]:
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def max_heap_insert(self, key: int, n: int) -> None:
        if self.size == n:
            raise OverflowError()

        self.size += 1
        k = key
        key = float("-inf")  # type: ignore
        self.heap.append(key)
        self.max_heap_increase_key(key, k)

    def max_heap_maximum(self) -> int:
        if not self.size:
            raise UnderflowError()

        return self.heap[0]

    def max_heap_extract_max(self) -> int:
        maximum = self.max_heap_maximum()
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.max_heapify(0)
        return maximum

    def heapsort(self, n: int) -> None:
        self.build_max_heap(n)

        for i in range(n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.size -= 1
            self.max_heapify(0)


@dataclass(slots=True)
class MinHeap:
    heap: list[int] = field(default_factory=list)
    size: int = field(default=0, init=False, repr=False)

    def min_heapify(self, i: int) -> None:
        l = left(i)
        r = right(i)
        m = l if l < self.size and self.heap[l] < self.heap[i] else i

        if r < self.size and self.heap[r] < self.heap[m]:
            m = r

        if m != i:
            self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
            self.min_heapify(m)

    def build_min_heap(self, n: int) -> None:
        for i in range(n // 2, -1, -1):
            self.min_heapify(i)

    def min_heap_decrease_key(self, x: int, k: int) -> None:
        if k > x:
            raise ValueError()

        i = self.heap.index(x)
        self.heap[i] = k

        while i and self.heap[(j := parent(i))] > self.heap[i]:
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def min_heap_insert(self, key: int, n: int) -> None:
        if self.size == n:
            raise OverflowError()

        self.size += 1
        k = key
        key = float("inf")  # type: ignore
        self.heap.append(key)
        self.min_heap_decrease_key(key, k)

    def min_heap_minimum(self) -> int:
        if not self.size:
            raise UnderflowError()

        return self.heap[0]

    def min_heap_extract_min(self) -> int:
        minimum = self.min_heap_minimum()
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.min_heapify(0)
        return minimum

    def heapsort(self, n: int) -> None:
        self.build_min_heap(n)

        for i in range(n - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.size -= 1
            self.min_heapify(0)
