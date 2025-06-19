from typing import *
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = 0
        for i in nums:
            n ^= i
        return n

if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([2, 4, 2, 4, 1]))