from typing import *
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        a = set([i for i in nums if i >= 0])
        return sum(a) if a else max(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSum([1,2,-1,-2,1,0,-1]))
