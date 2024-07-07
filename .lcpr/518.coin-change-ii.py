# @lcpr-before-debug-begin
from python3problem518 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=518 lang=python3
# @lcpr version=30204
#
# [518] 零钱兑换 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if j >= coins[i]:
                    dp[j] = dp[j] + dp[j-coins[i]]
        return dp[-1]
# @lc code=end



#
# @lcpr case=start
# 5\n[1, 2, 5]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[2]\n
# @lcpr case=end

# @lcpr case=start
# 10\n[10]\n
# @lcpr case=end

#

