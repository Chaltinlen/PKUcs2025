from typing import *
from bisect import bisect
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        ans = []
        items.sort(key = lambda t: (t[0], -t[1]))
        stack = [0]
        price = [0]
        for i in range(len(items)):
            stack.append(max(stack[-1], items[i][1]))
            price.append(items[i][0])
        for q in queries:
            ans.append(stack[bisect(price, q) - 1])
        return ans
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumBeauty(items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]))