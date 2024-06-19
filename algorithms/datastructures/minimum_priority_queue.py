import bisect
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class MinimumPriorityQueue:
    priority: Callable[[Any], int | float] = field(
        default=lambda x: x, repr=False
    )
    key: str | None = field(default=None, repr=False)
    queue: list[Any] = field(default_factory=list, init=False)

    def insert(self, value: Any) -> None:
        bisect.insort(self.queue, value, key=self.priority)

    def extract_min(self) -> Any:
        return self.queue.pop(0)

    def decrease_key(self, item: Any, value: float) -> None:
        if self.key is not None:
            setattr(item, self.key, value)

        self.queue.remove(item)
        self.insert(item)

    def __len__(self) -> int:
        return len(self.queue)

    def __contains__(self, item: Any) -> bool:
        return item in self.queue
