#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res =[]
        self.inorder(root)
        return self.res
    def inorder(self,root):
        if root is None:
            return None
        
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
# @lc code=end

