#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.yanzheng(root,None,None)

    def yanzheng(self,root,minv,maxv):
        if root is None:
            return True
        if minv is not None and root.val<=minv.val:
            return False
        if maxv is not None and root.val >=maxv.val:
            return False


        return self.yanzheng(root.left,minv,root) and self.yanzheng(root.right,root,maxv)
# @lc code=end

