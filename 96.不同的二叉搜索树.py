#
# @lc app=leetcode.cn id=96 lang=python
#
# [96] 不同的二叉搜索树
#

# @lc code=start


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
            return 0
        self.mem = [[0 for i in range(n+1)] for j in range(n+1)] 
        res = self.count(1,n)
        return res
    def count(self,lo,hi):
        if lo-hi>0:
            return 1
        if self.mem[lo][hi]!=0:
            return self.mem[lo][hi]
        res = 0
        for i in range(lo,hi+1):
            left = self.count(lo,i-1)
            right = self.count(i+1,hi)
            res +=left*right
        self.mem[lo][hi] = res
        return res 
        
