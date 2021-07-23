#
# @lc app=leetcode.cn id=700 lang=python
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        return self.isBST(root,val)
    def isBST(self,root,val):
        
        if root is None:
            return None
        if root.val == val:
            return root
        if val < root.val:
            return self.isBST(root.left,val)
        if val > root.val:
            return self.isBST(root.right,val)

# @lc code=end

