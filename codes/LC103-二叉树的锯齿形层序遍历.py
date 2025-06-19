from typing import *
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        ans = [[]]
        lasth = -1
        while queue:
            node, h = queue.popleft()
            if not node:
                continue
            if h != lasth:
                lasth = h
                if not h % 2:
                    ans[-1].reverse()
                ans.append([])
            ans[-1].append(node.val)
            queue.append((node.left, h + 1))
            queue.append((node.right, h + 1))
        if not h % 2:
            ans[-1].reverse()
        return ans[1:]

if __name__ == "__main__":
    sol = Solution()
    print(sol.zigzagLevelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
