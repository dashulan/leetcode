#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
# from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i,n in enumerate(nums):
            nmap[i] = n
        for k in nmap.values():
            temp  = target - k
            if temp in nmap.keys() and nmap[temp]!=nmap[k]:
                return [nmap[k],nmap[temp]]
# @lc code=end

# s = Solution()
# s.twoSum([2,7,11,15],9)