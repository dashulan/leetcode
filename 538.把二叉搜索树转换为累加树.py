#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.bianli(root)

        return root

    def bianli(self,root):
        if root is None:
            return
        self.bianli(root.right)
        self.sum = self.sum+root.val
        root.val = self.sum
        self.bianli(root.left)




# @lc code=end

