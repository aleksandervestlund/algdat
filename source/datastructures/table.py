from dataclasses import dataclass, field


@dataclass(slots=True)
class Table:
    data: list[int] = field(default_factory=list)
    size: int = field(default=0, repr=False, init=False)
    num: int = field(default=0, repr=False, init=False)

    def table_insert(self, key: int) -> None:
        """Runtime: Θ(n)."""
        if not self.size:
            self.size = 1

        if self.num == self.size:
            self.data = self.data.copy()
            self.size *= 2

        self.data.append(key)
        self.num += 1
