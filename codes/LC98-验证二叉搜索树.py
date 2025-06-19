from typing import *
# Definition for a binary tree node.
from functools import lru_cache
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.last = - (1 << 32)
        self.ans = True
        def midT(node):
            if self.ans and node:
                midT(node.left)
                self.ans &= (node.val > self.last)
                self.last = node.val
                midT(node.right)
        midT(root)
        return self.ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.isValidBST(TreeNode(1, TreeNode(2), TreeNode(3))))
