class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0 for i in range(m - k + 1)] for j in range(n - k + 1)]
        diff = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                
