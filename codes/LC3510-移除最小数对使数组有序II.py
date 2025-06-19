from typing import *
from heapq import heappush, heappop
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        left = list(range(-1, len(nums)))
        right = list(range(1, len(nums) + 1))
        heap = []
        dec = 0
        ans = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                dec += 1
            heappush(heap, (nums[i] + nums[i+1], i))
        while dec:
            s, ind = heappop(heap)
            if right[ind] >= len(nums) or s != nums[ind] + nums[right[ind]]:
                continue
            ans += 1
            lst = left[ind]
            nxt = right[ind]
            nnxt = right[nxt]
            if nums[ind] > nums[right[ind]]:
                dec -= 1

            if lst >= 0:
                if nums[lst] > nums[ind]:
                    dec -= 1
                if s < nums[lst]:
                    dec += 1
                heappush(heap, (s + nums[lst], lst))
            if nnxt < len(nums):
                if nums[nxt] > nums[nnxt]:
                    dec -= 1
                if s > nums[nnxt]:
                    dec += 1
                heappush(heap, (s + nums[nnxt], ind))
                
            

            nums[ind] = s
            l, r = left[nxt], right[nxt]
            right[l] = r
            left[r] = l
            right[nxt] = len(nums)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumPairRemoval([7,5,3,2,1]))
