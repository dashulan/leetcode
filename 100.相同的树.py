#
# @lc app=leetcode.cn id=100 lang=python
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p and not q:
            return False 
        if q and not p:
            return False
        return  p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
# @lc code=end

