#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res  =[]
        queue = []
        if root is None:
            return []
        queue.insert(0,root)
        while len(queue)>0:
            temp =[]
            for i in range(len(queue)):
                node = queue.pop()
                temp.append(node.val)
                left = node.left
                right = node.right
                if left:
                    queue.insert(0,left)
                if right: 
                    queue.insert(0,right)
            res.append(temp) 
        
        return res
# @lc code=end

