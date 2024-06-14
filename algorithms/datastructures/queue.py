class Queue:
    def __init__(self, size: int) -> None:
        self.queue: list[int] = []
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, x: int) -> None:
        self.queue[self.tail] = x
        if self.tail == self.size:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self) -> int:
        x = self.queue[self.head]
        if self.head == self.size:
            self.head = 0
        else:
            self.head += 1
        return x

    def __repr__(self) -> str:
        return f"Queue({self.queue})"
