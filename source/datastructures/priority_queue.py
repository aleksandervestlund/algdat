import bisect
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class PriorityQueue:
    key: str | None = field(default=None, repr=False)
    queue: list[Any] = field(default_factory=list, init=False)

    def insert(self, value: Any) -> None:
        """Runtime: O(log(n))."""
        bisect.insort(
            self.queue,
            value,
            key=lambda x: x if self.key is None else getattr(x, self.key),
        )

    def extract_min(self) -> Any:
        """Runtime: O(1)."""
        return self.queue.pop(0)

    def extract_max(self) -> Any:
        """Runtime: O(1)."""
        return self.queue.pop()

    def decrease_key(self, item: Any, value: float) -> None:
        """Runtime: O(log(n))."""
        if self.key is None:
            if value > item:
                raise ValueError()
        else:
            if value > getattr(item, self.key):
                raise ValueError()

            setattr(item, self.key, value)

        self.queue.remove(item)
        self.insert(item)

    def increase_key(self, item: Any, value: float) -> None:
        """Runtime: O(log(n))."""
        if self.key is None:
            if value < item:
                raise ValueError()
        else:
            if value < getattr(item, self.key):
                raise ValueError()

            setattr(item, self.key, value)

        self.queue.remove(item)
        self.insert(item)

    def __len__(self) -> int:
        """Used for both `len(q)` and `while q`, which is equivalent to
        `while len(q) > 0`.
        """
        return len(self.queue)

    def __contains__(self, item: Any) -> bool:
        """Used for `if item in q`."""
        return item in self.queue
