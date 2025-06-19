from typing import *
from math import ceil
from pprint import pprint
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(ceil(n/2)):
            for j in range(n//2):
                matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i] = matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]
        pprint(matrix)

if __name__ == '__main__':
    sol = Solution()
    sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])