import re
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        exp = re.sub(r"\*{1,}", ".*?", p)
        ans = 1e6
        start = 0
        while (res := re.search(exp, s[start:])) != None:
            ans = min(ans, len(res.group()))
            start = res.start() + 1
            if ans == len(p) - 2:
                return ans
        return ans if ans != 1e6 else -1