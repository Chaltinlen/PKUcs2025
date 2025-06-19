from typing import *
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        def solve(n, depth, prev):
            if depth == n:
                self.ans.append(prev)
            for i in range(n):
                if i in prev:
                    continue
                for j in range(len(prev)):
                    if depth - i == j - prev[j] or depth + i == j + prev[j]:
                        break
                else:
                    solve(n, depth + 1, prev + [i])

        solve(n, 0, [])
        board = []
        for a in self.ans:
            board.append(["".join(["." if i != a[j] else "Q" for i in range(n)]) for j in range(n)])
        return board


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))
