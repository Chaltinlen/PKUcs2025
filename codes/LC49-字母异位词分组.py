from typing import *
from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnter = defaultdict(list)
        for s in strs:
            cnter[frozenset(Counter(s).items())].append(s)
        return list(cnter.values())


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
