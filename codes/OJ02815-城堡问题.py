class Bingchaji:
    def __init__(self, n):
        self.lst = list(range(n))
        self.size = [1] * n
    def find(self, x):
        return x if self.lst[x] == x else self.find(self.lst[x])
    def merge(self, x, y):
        yrep = self.find(y)
        xrep = self.find(x)
        if xrep == yrep:
            return
        # print(xrep, yrep)
        # print(self.size[xrep], self.size[yrep])
        self.lst[yrep] = xrep
        self.size[xrep] += self.size[yrep]
        self.size[yrep] = 0
m = int(input())
n = int(input())
room = Bingchaji(m * n)
board = []
for i in range(m):
    board.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        if not board[i][j] & 1:
            # print(1, i, j, board[i][j])
            room.merge(i * n + j - 1, i * n + j)
        if not board[i][j] & 2:
            # print(2, i, j, board[i][j])
            room.merge(i * n + j - n, i * n + j)
        # print(room.lst)
        # print(room.size)
print(m * n - room.size.count(0))
print(max(room.size))