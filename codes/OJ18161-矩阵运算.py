class matrix():
    def __init__(self, row, col, val):
        self.row = row
        self.col = col
        self.val = val
    def __add__(self, other):
        if self.row != other.row or self.col != other.col:
            raise ValueError
        ans = [[self.val[i][j] + other.val[i][j] for j in range(self.col)] for i in range(self.row)]
        return matrix(self.row, self.col, ans)
    def __str__(self):
        ans = []
        for r in self.val:
            ans.append(" ".join(map(str, r)))
        return "\n".join(ans)
    def __mul__(self, other):
        if self.col != other.row:
            raise ValueError
        ans = [[0 for i in range(other.col)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(other.col):
                for k in range(self.col):
                    ans[i][j] += self.val[i][k] * other.val[k][j]
        return matrix(self.row, other.col, ans)

A = []
for i in range(3):
    row, col = map(int, input().split())
    val = [list(map(int, input().split())) for i in range(row)]
    A.append(matrix(row, col, val))
try:
    print(A[0] * A[1] + A[2])
except ValueError:
    print("Error!")