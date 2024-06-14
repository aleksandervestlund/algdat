class Table:
    def __init__(self) -> None:
        self.data: list[int] = []
        self.size = 0
        self.num = 0

    def insert(self, key: int) -> None:
        if self.size == 0:
            self.size = 1
        if len(self.data) == self.size:
            self.data = self.data.copy()
            self.size *= 2
        self.data[self.num] = key
        self.num += 1
