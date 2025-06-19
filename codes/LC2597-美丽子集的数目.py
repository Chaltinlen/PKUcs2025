from typing import *
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.ans = []
        def recur(nums, depth, pref):
            if depth == len(nums):
                self.ans.append(pref)
                return
            recur(nums, depth + 1, pref)
            recur(nums, depth + 1, pref | {nums[depth]})

        recur(nums, 0, set())
        cnt = 0
        for s in self.ans:
            for n in s:
                if n + k in s:
                    break
            else:
                cnt += 1
        return cnt - 1

if __name__ == '__main__':
    sol = Solution()
    print(sol.beautifulSubsets([1, 2, 3, 4], 1))