from typing import *
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # def construct(prefix, infix):
        #     if prefix:
        #         node = TreeNode(prefix[0])
        #         p = infix.index(prefix[0])
        #         node.left = construct(prefix[1:p + 1], infix[:p])
        #         node.right = construct(prefix[p + 1:], infix[p + 1:])
        #         return node
        # return construct(preorder, inorder)
        def recur(root, left, right):
            if left <= right:                             # 递归终止
                node = TreeNode(preorder[root])                       # 建立根节点
                i = dic[preorder[root]]                               # 划分根节点、左子树、右子树
                node.left = recur(root + 1, left, i - 1)              # 开启左子树递归
                node.right = recur(i - left + root + 1, i + 1, right) # 开启右子树递归
                return node                                           # 回溯返回根节点

        dic, preorder = {}, preorder
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0, 0, len(inorder) - 1)


def pstT(node):
    if node:
        pstT(node.left)
        pstT(node.right)
        print(node.val)

if __name__ == "__main__":
    sol = Solution()
    pstT(sol.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))
