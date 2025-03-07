from typing import *
from math import ceil
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def ispossible(mid, maxOperations):
            cnt = 0
            for n in nums:
                if n < mid:
                    break
                cnt += ceil(n / mid) - 1
            if cnt > maxOperations:
                return False
            return True

        nums = sorted(nums, reverse=True)
        lo = 1
        hi = nums[0] + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if ispossible(mid, maxOperations):
                hi = mid
            else:
                lo = mid + 1
        return lo

if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumSize([9], 10))