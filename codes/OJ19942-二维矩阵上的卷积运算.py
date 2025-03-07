class matrix():
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
    def __str__(self):
        ans = []
        for r in self.val:
            ans.append(" ".join(map(str, r)))
        return "\n".join(ans)
    def __mul__(self, other):
        ans = [[0 for i in range(self.col - other.col + 1)] for j in range(self.row - other.row + 1)]
        for i in range(self.row - other.row + 1):
            for j in range(self.col - other.col + 1):
                for k in range(other.row):
                    for w in range(other.col):
                        ans[i][j] += self.val[i + k][j + w] * other.val[k][w]
        return matrix(
            self.row - other.row + 1, 
            self.col - other.col + 1, 
            ans
            )


m, n, p, q = map(int, input().split()) 
M = matrix(m, n, [list(map(int, input().split())) for i in range(m)])
C = matrix(p, q, [list(map(int, input().split())) for j in range(p)])
print(M * C)
