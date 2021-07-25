#
# @lc app=leetcode.cn id=103 lang=python
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queque = []
        if root is None:
            return []
        queque.insert(0,root)
        tag =True
        while len(queque) >0:
            temp = []
            for i in range(len(queque)):
                node = queque.pop()
                if node.left:
                    queque.insert(0,node.left)
                if node.right:
                    queque.insert(0,node.right)
                temp.append(node.val)
                
            if tag:
                res.append(temp)
                tag =False
            else:
                temp.reverse()
                res.append(temp)
                tag = True
        
        return res
# @lc code=end

