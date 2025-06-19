from typing import *
from bisect import bisect_left
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        s = sorted(citations)
        lo, hi = 0, s[-1] + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if len(s) - bisect_left(s, mid) >= mid:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.hIndex([3,0,6,1,5]))
