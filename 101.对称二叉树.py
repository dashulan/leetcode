#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        

        def isSame(node1,node2):
            if node1 is None and node2 is not None:
                return False
            if node1 is not None and node2 is None:
                return False
            if node1 is None and node2 is None:
                return True
            return node1.val == node2.val and isSame(node1.left,node2.right) and isSame(node1.right,node2.left) 

        if root is None:
            return False
        return isSame(root.left,root.right)
