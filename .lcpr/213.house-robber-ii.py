#
# @lc app=leetcode.cn id=213 lang=python3
# @lcpr version=30204
#
# [213] 打家劫舍 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robrange(nums):
            if len(nums) == 1:
                return nums[0]

            dp = [0]* len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])

            return dp[-1]
        
        return max(robrange(nums[1:]),robrange(nums[:-1]))

# @lc code=end



#
# @lcpr case=start
# [2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

