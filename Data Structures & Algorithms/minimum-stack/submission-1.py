from collections import deque

class MinStack:

    def __init__(self):
        self.queue = deque()
        self.minimum = deque()

    def push(self, val: int) -> None:
        self.queue.append(val)
        minimum = self.minimum[-1] if (len(self.minimum) > 0 and self.minimum[-1] < val) else val
        self.minimum.append(minimum)

    def pop(self) -> None:
        self.queue.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.queue[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
