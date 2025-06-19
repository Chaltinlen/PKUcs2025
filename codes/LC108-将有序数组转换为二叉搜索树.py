from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def transform(array):
            if not len(array):
                return None
            node = TreeNode(array[len(array)//2])
            node.right = transform(array[len(array)//2 + 1:])
            node.left = transform(array[:len(array)//2])
            return node 
        return transform(nums)


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortedArrayToBST([-10, -3, 0, 5, 9]))
