from typing import *
from collections import deque
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        t_prod = 1
        for i in nums:
            t_prod *= i
        if target * target != t_prod:
            return False
        self.ans = False
        def recur(t, L):
            if not self.ans:
                for i in L:
                    if i == t:
                        self.ans = True
                        return True
                    if t % i == 0:
                        recur(t // i, L - {i})
        recur(target, set(nums))
        return self.ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.checkEqualPartitions(nums = [3,6], target = 9))
