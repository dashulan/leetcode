#
# @lc app=leetcode.cn id=450 lang=python
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if key == root.val:
            root = self.fuzhu(root)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        return root

    def fuzhu(self,root):
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            root = root.right
        elif root.right is None:
            root = root.left
        elif root.left is not None and root.right is not None:
            minNode = self.getmin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right,minNode.val)
        return root

    def getmin(self,root):
        while(root.left is not None): root = root.left
        return root
# @lc code=end

