from typing import *
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        ans = []
        lst = list(range(n))
        for i in range(n-1):
            if nums[i+1] - nums[i] <= maxDiff:
                lst[i+1] = lst[i]
        for u, v in queries:
            ans.append(lst[u] == lst[v])
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.pathExistenceQueries(n = 2, nums = [1,3], maxDiff = 1, queries = [[0,0],[0,1]]))
