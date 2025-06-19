from typing import *
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        ans = []
        while True:
            try:
                ind = text.index(first)
            except ValueError:
                return ans
            if ind + 2 < len(text) and text[ind + 1] == second:
                ans.append(text[ind + 2])
            text = text[ind + 1:]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findOcurrences("we will we will rock we will", "we", "will"))