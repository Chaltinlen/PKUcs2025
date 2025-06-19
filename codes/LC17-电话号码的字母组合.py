from typing import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        NUM_TO_LETTER = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        self.ans = []
        def recur(digits, depth, prev):
            if depth >= len(digits):
                self.ans.append(prev)
                return
            for n in NUM_TO_LETTER[digits[depth]]:
                recur(digits, depth + 1, prev + n)
        recur(digits, 0, "")
        if not self.ans[0]:
            self.ans.pop()
        return self.ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations(""))
