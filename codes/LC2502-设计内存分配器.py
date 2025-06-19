from collections import deque
class Allocator:

    def __init__(self, n: int):
        self.allo = [0] * n
        self.mid_to_loc = {0: (0, n - 1)}
        self.loc_to_mid = {(0, n - 1): 0}

    def allocate(self, size: int, mID: int) -> int:
        

    def freeMemory(self, mID: int) -> int:
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)