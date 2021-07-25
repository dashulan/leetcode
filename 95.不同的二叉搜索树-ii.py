#
# @lc app=leetcode.cn id=95 lang=python
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n ==0:
            return[]
        return self.fuzhu(1,n)

    def fuzhu(self,lo,hi):
        res = []
        if lo-hi>0:
            res.append(None)
            return res
         
        for i in range(lo,hi+1):
            left = self.fuzhu(lo,i-1)
            right = self.fuzhu(i+1,hi)
            
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res

# @lc code=end

