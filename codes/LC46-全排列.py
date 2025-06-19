from typing import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def generate(nums, pref):
            if len(pref) == len(nums):
                self.ans.append(pref)
                return
            for i in nums:
                if i not in pref:
                    generate(nums, pref + [i])


        generate(nums, [])
        return self.ans

if __name__ == '__main__':
    sol = Solution()
    print(*sol.permute(list(range(1, 6))), sep="\n")