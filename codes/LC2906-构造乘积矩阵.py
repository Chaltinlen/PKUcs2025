from typing import *
from itertools import accumulate
from collections import deque
import operator
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        # p = 1
        # cnt = []
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] % 12345:
        #             p *= grid[i][j] % 12345
        #         else:
        #             cnt.append((i, j))
        # if len(cnt) == 1:
        #     ans[cnt[0][0]][cnt[0][1]] = p % 12345
        #     return ans
        # elif len(cnt) > 1:
        #     return ans
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         ans[i][j] = p // grid[i][j] % 12345
        # return ans
        one_dim = []
        for i in grid:
            for j in i:
                one_dim.append(j)
        pre = []
        suf = deque()
        p = 1
        for i in one_dim:
            pre.append(p)
            p *= i
        p = 1
        for i in one_dim[::-1]:
            suf.appendleft(p)
            p *= i
        for i in range(n * m):
            grid[i // m][i % m] = (pre[i] % 12345) * (suf[i] % 12345) % 12345
        return grid
if __name__ == '__main__':
    sol = Solution()
    print(sol.constructProductMatrix([[12345],[2],[1]]))

