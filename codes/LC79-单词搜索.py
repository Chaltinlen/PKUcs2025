from typing import *
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        DIRECTION = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        word = list(word)
        self.ans = False
        visited = set()
        def dfs(pos, step):
            if self.ans:
                return
            if step == len(word):
                self.ans = True
                return
            for dx, dy in DIRECTION:
                nx, ny = pos[0] + dx, pos[1] + dy
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in visited:
                    if board[nx][ny] == word[step]:
                        visited.add((nx, ny))
                        dfs((nx, ny), step + 1)
                        visited.remove((nx, ny))


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and not self.ans:
                    visited.add((i, j))
                    dfs((i, j), 1)
                    visited.remove((i, j))
        return self.ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))