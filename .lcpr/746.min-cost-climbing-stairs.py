#
# @lc app=leetcode.cn id=746 lang=python3
# @lcpr version=30204
#
# [746] 使用最小花费爬楼梯
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2], dp[i-1]) +cost[i]
        return min(dp[-2], dp[-1])
# @lc code=end



#
# @lcpr case=start
# [10,15,20]\n
# @lcpr case=end

# @lcpr case=start
# [1,100,1,1,1,100,1,1,100,1]\n
# @lcpr case=end

#

