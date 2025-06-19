from typing import *
from heapq import heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_mat = [[1000001 for i in range(n)] for j in range(n)]
        for s, c, p in flights:
            adj_mat[s][c] = p
        dist = [[1000001 for i in range(k + 2)] for j in range(n)]
        heap = [(0, 0, src)]
        ans = -1
        while heap:
            c, ret, node = heappop(heap)
            if dist[node][ret] < c:
                continue
            if node == dst:
                ans = c
                break
            for i in range(n):
                if adj_mat[node][i] < 10001 and ret <= k and c + adj_mat[node][i] < dist[i][ret + 1]:
                    dist[i][ret + 1] = c + adj_mat[node][i]
                    heappush(heap, (dist[i][ret + 1], ret + 1, i))
        return ans



if __name__ == "__main__":
    sol = Solution()
    print(sol.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
