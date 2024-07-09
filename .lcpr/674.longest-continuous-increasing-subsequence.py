#
# @lc app=leetcode.cn id=674 lang=python3
# @lcpr version=30204
#
# [674] 最长连续递增序列
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                dp[i] = dp[i-1] + 1
            res = max(dp[i], res)
        return res
    
    def findLengthOfLCIS1(self, nums: List[int]) -> int:
        res = 1
        s_idx = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                res = max(i-s_idx+1, res)
            else:
                s_idx = i
        return res
# @lc code=end



#
# @lcpr case=start
# [1,3,5,4,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n
# @lcpr case=end

#

