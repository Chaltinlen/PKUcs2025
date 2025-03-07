class Solution:
    def separateSquares(self, squares: List[List[int]]):
        interval = []
        for square in squares:
            interval.append((square[1], square[1] + square[2]))
        interval.sort(reverse=True)
        print(interval)
        new = []
        left = interval[-1][0]
        right = interval[-1][1]
        while interval:
            I = interval.pop()
            right = max(right, I[1])
            if I[0] > right:
                new.append((left, right))
                left = I[0]
                right = I[1]
        new.append((left, right))
        print(new)
