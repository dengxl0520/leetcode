#
# @lc app=leetcode.cn id=494 lang=python3
# @lcpr version=30204
#
# [494] 目标和
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
            暴力法时间复杂度：2^len(nums)
            动态规划思路：left - right = target
            相当于将nums分成两组，使其的差为target，计数有多少种
        '''
        total_sum = sum(nums)
        if (total_sum - target) % 2 == 1 or total_sum < target:
            return 0

        weight = (total_sum-target) // 2

        dp = [0] * (weight + 1)
        dp[0] = 1
        # 只要搞到nums[i]，凑成dp[j]就有dp[j - nums[i]] 种方法。 from：代码随想录
        # dp[j] 表示j容量有dp[j]种方式
        for i in range(len(nums)):
            for j in range(weight, nums[i]-1, -1):
                dp[j] = dp[j] + dp[j-nums[i]] # 和其他01背包问题一样，要和不要nums[i]两种选择

        return dp[-1]
# @lc code=end



#
# @lcpr case=start
# [2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53]\n1000\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

#

