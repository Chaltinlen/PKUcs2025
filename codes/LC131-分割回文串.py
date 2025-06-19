from typing import *
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        def partify(s, prev):   # prev: List[str]
            if len(s) == 1:
                self.ans.append(prev + [s])
                return
            if len(s) == 0:
                self.ans.append(prev)
                return
            for i in range(1, len(s) + 1):
                if s[:i] == "".join(reversed(s[:i])):
                    partify(s[i:], prev + [s[:i]])

        partify(s, [])
        return self.ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.partition("aababba"))