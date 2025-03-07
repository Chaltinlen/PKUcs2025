class MinStack:

    def __init__(self):
        self.stack = []
        self.helper = []
        self.pres = (1 << 31) - 1
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.pres = min(self.pres, val)
        self.helper.append(self.pres)

    def pop(self) -> None:
        self.stack.pop()
        self.helper.pop()
        if self.helper:
            self.pres = self.helper[-1]
        else:
            self.pres = (1 << 31) - 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()