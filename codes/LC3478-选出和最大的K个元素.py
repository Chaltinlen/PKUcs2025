from heapq import heappushpop
from typing import *
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums2)
        nums2.append(0)
        elem = [0 for i in range(k)]
        ans = [0 for i in range(n)]
        temp = sorted(enumerate(nums1), key=lambda x: x[1])
        # print(temp)
        msum = 0
        ind = -1
        for i in range(n):
            msum += nums2[ind]
            msum -= heappushpop(elem, nums2[ind])
            ind = temp[i][0]
            if i == 0 or temp[i][1] != temp[i-1][1]:
                ans[ind] = msum
            else:
                ans[ind] = ans[temp[i-1][0]]
            # print(elem, msum, ans)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxSum([18,11,24,9,10,11,7,29,16], [28,26,27,4,2,19,23,1,2], 1))