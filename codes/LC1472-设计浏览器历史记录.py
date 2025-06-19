# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.bwd = [homepage]
#         self.fwd = []

#     def visit(self, url: str) -> None:
#         self.bwd.append(url)
#         if self.fwd:
#             self.fwd = []

#     def back(self, steps: int) -> str:
#         steps = min(steps, len(self.bwd) - 1)
#         for i in range(steps):
#             self.fwd.append(self.bwd.pop())
#         return self.bwd[-1]

#     def forward(self, steps: int) -> str:
#         steps = min(steps, len(self.fwd))
#         for i in range(steps):
#             self.bwd.append(self.fwd.pop())
#         return self.bwd[-1]


# # Your BrowserHistory object will be instantiated and called as such:
# # obj = BrowserHistory(homepage)
# # obj.visit(url)
# # param_2 = obj.back(steps)
# # param_3 = obj.forward(steps)
class DoubleLinkedList:
    def __init__(self, bwd=None, val="", fwd=None):
        self.bwd = bwd
        self.val = val
        self.fwd = fwd
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = DoubleLinkedList(val=homepage)
        self.tail = self.head

    def visit(self, url: str) -> None:
        self.tail.fwd = DoubleLinkedList(self.tail, url)
        self.tail = self.tail.fwd

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.tail != self.head:
                self.tail = self.tail.bwd
            else:
                break
        return self.tail.val


    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.tail.fwd:
                self.tail = self.tail.fwd
            else:
                break
        return self.tail.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)