from typing import *
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # cnt = [0] * 3
        # for i in nums:
        #     cnt[i] += 1
        # for i in range(cnt[0]):
        #     nums[i] = 0
        # for i in range(cnt[0], cnt[1] + cnt[0]):
        #     nums[i] = 1
        # for i in range(cnt[1] + cnt[0], len(nums)):
        #     nums[i] = 2
        left, i, right = 0, 0, len(nums) - 1
        while i < right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                i += 1
                left += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
        print(nums)
sol = Solution()
print(sol.sortColors([2, 0, 2, 1, 1, 0]))