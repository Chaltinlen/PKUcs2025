from heapq import heappush, heappop
from typing import *
class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []
        ans = 0
        for i in range(len(grid)):
            grid[i].sort(reverse=True)
            for j in range(limits[i]):
                heappush(heap, -grid[i][j])
        for i in range(k):
            ans -= heappop(heap)
        return ans
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSum([[1,2],[3,4]], [1, 2], 2))
