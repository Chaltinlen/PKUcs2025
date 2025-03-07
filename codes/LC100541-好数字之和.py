class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ans = 0
        tot = len(nums)
        for i in range(tot):
            left = nums[i - k] if 0 <= i - k else 0
            right = nums[i + k] if i + k < tot else 0
            if left < nums[i] and right < nums[i]:
                ans += nums[i]
        return ans
