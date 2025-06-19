from typing import *
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def recur(nums, depth, pref):
            if depth == len(nums):
                self.ans.append(pref)
                return
            recur(nums, depth + 1, pref)
            recur(nums, depth + 1, pref + [nums[depth]])

        recur(nums, 0, [])
        return self.ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3]))