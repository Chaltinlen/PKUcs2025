from typing import *
from pprint import pprint
from heapq import heappush, heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = []
        adj_mat = [[1e9 for i in range(n)] for j in range(n)]
        for u, v, w in times:
            adj_mat[u-1][v-1] = w
            if u == k:
                heappush(heap, (w, v-1))
        k -= 1
        adj_mat[k][k] = 0
        # pprint(adj_mat)
        # pprint(heap)
        while heap:
            w, v = heappop(heap)
            if adj_mat[k][v] < w:
                continue
            # print(w, v)
            # pprint(adj_mat)
            for node in range(n):
                if adj_mat[v][node] != 1e9 and adj_mat[k][node] > adj_mat[k][v] + adj_mat[v][node]:
                    adj_mat[k][node] = adj_mat[k][v] + adj_mat[v][node]
                    heappush(heap, (adj_mat[k][node], node))

        # pprint(adj_mat)
        M = max(adj_mat[k])
        return M if M != 1e9 else -1





if __name__ == "__main__":
    sol = Solution()
    print(sol.networkDelayTime(times = [[1,2,1],[2,3,2]], n = 3, k = 1))
