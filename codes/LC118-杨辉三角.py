from typing import *
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        yang_hui = [[1] for i in range(numRows)]
        for i in range(1, numRows):
            for j in range(1, i):
                yang_hui[i].append(yang_hui[i - 1][j - 1] + yang_hui[i - 1][j])
            yang_hui[i].append(1)
        return yang_hui

if __name__ == '__main__':
    sol = Solution()
    print(sol.generate(int(input())))