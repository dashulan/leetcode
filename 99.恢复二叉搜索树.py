#
# @lc app=leetcode.cn id=99 lang=python
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        self.prev = TreeNode(float("-inf"))
        self.n1 =None
        self.n2 = None
        self.findError(root)
        self.n1.val ,self.n2.val = self.n2.val ,self.n1.val
        return root
    
    def findError(self,root):
        if root is None:
            return None
        self.findError(root.left)
        if self.n1 is None and root.val <=self.prev.val:
            self.n1 =self.prev
        if self.n1 and root.val <=self.prev.val:
            self.n2 = root
        self.prev = root    
        self.findError(root.right)
            

# @lc code=end

