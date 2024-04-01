class MinStack:

    def __init__(self):
        self.cache = []
        self.min = []

    def push(self, val: int) -> None:
        self.cache.append(val)
        self.min.append(val if len(self.min) == 0 or val < self.min[-1] else self.min[-1])

    def pop(self) -> None:
        self.cache.pop()
        self.min.pop()

    def top(self) -> int:
        return self.cache[-1]

    def getMin(self) -> int:
        return self.min[-1]


if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert -3 == min_stack.getMin()
    min_stack.pop()
    assert 0 == min_stack.top()
    assert -2 == min_stack.getMin()
