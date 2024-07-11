#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30204
#
# [11] 盛最多水的容器
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
            双指针，关键在于想清楚哪边要移动
            应该是小的那边移动
        '''
        res = 0
        n = len(height)
        left, right = 0,n-1
        while left < right:
            if height[left] < height[right]:
                res = max(res, (right-left) * height[left])
                left += 1
            else:
                res = max(res, (right-left) * height[right])
                right -= 1
        return res
    
    def maxArea2(self, height: List[int]) -> int:
        '''
            简单剪枝，TLE
        '''
        n = len(height)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                res = max(res, (j-i)*min(height[i], height[j]))
        return res
    
    def maxArea1(self, height: List[int]) -> int:
        '''
            纯暴力，TLE
        '''
        n = len(height)
        res = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    res = max(res, (j-i)*min(height[i], height[j]))
        return res
# @lc code=end



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end
    
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

#

