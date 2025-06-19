from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def travel(node, prev):
            if not node.left and not node.right:
                self.ans += prev * 10 + node.val
                return
            if node.left:
                travel(node.left, prev * 10 + node.val)
            if node.right:
                travel(node.right, prev * 10 + node.val)
        travel(root, 0)
        return self.ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))))
