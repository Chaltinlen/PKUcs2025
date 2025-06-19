from typing import *
from math import pow
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.cnt = self.h = 0
        self.h = 0
        def dfs(node, h):
            if not node:
                self.cnt += 1
                if not self.h:
                    self.h = h
                return
            if self.h and h == self.h and node:
                raise ValueError
            dfs(node.right, h + 1)
            dfs(node.left, h + 1)
        try:
            dfs(root, 0)
        except ValueError:
            pass
        return int(pow(2, self.h + 1)) - self.cnt - 1



if __name__ == "__main__":
    sol = Solution()
    print(sol.countNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))
