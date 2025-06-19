# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.ans = []
        queue = deque()
        queue.append((root, 0))
        curr_layer = -1
        while queue:
            node, layer = queue.popleft()
            if node:
                if curr_layer != layer:
                    curr_layer = layer
                    self.ans.append([])
                self.ans[-1].append(node.val)
                queue.append((node.left, layer + 1))
                queue.append((node.right, layer + 1))

        return self.ans