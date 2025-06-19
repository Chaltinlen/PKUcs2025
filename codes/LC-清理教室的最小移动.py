from typing import *
from collections import deque
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        gar = set()
        sx, sy = 0, 0
        for i in range(len(classroom)):
            for j in range(len(classroom[0])):
                if classroom[i][j] == 'L':
                    gar.add((i, j))
                elif classroom[i][j] == 'S':
                    sx, sy = i, j
        queue = deque()
        queue.append([sx, sy, gar, energy, 0, (0, 0)])
        vis = {}
        while queue:
            x, y, g, e, s, l_s = queue.popleft()
            flag = False
            if (x, y) in vis:
                for ga, en, st in vis[(x, y)]:
                    if ga.issubset(g) and en >= e and st <= s:
                        flag = True
                        break
                else:
                    vis[(x, y)].append([g, e, s])
            else:
                vis[(x, y)] = [[g, e, s]]
            if flag:
                continue
            if not g:
                return s
            if e == 0:
                continue
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if (-dx, -dy) == l_s:
                    continue
                if 0 <= nx < len(classroom) and 0 <= ny < len(classroom[0]) and classroom[nx][ny] != 'X':
                    if (nx, ny) in g:
                        queue.append([nx, ny, g - {(nx, ny)}, e - 1, s + 1, (0, 0)])
                    elif classroom[nx][ny] == 'R':
                        queue.append([nx, ny, g, energy, s + 1, (0, 0)])
                    else:
                        queue.append([nx, ny, g, e - 1, s + 1, (dx, dy)])

        return -1



if __name__ == "__main__":
    sol = Solution()
    print(sol.minMoves(classroom = ["S...................", "....................", "....................", "....................", ".....RL........RR...", "....................", "......L....R..L.....", ".....L..............", ".........L........LL", "....................", "....................", "....................", "........L...........", "....................", "....................", "....................", "....L...............", "....................", ".....R..............", "..............L....."], energy = 20))
