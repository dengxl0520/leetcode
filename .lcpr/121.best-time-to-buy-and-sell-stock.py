#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30204
#
# [121] 买卖股票的最佳时机
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            dp写法：
            dp[i][0] 维护买入股票的最大金额
            dp[i][1] 维护卖出股票的最大金额
            dp[i][0] = min(dp[i-1][0], -prices[i]) 
            dp[i][1] = max(dp[i][0]+prices[i], dp[i-1][1])
        '''
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][0],dp[0][1] = -prices[0], 0
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i]) 
            dp[i][1] = max(dp[i-1][0]+prices[i], dp[i-1][1])

        return dp[-1][1]
    
    def maxProfit2(self, prices: List[int]) -> int:
        '''
            贪心
        '''
        res = 0
        min_prices = prices[0]
        for i in range(1, len(prices)):
            min_prices = min(min_prices, prices[i])
            res = max(res, prices[i]-min_prices)
        return res
    
    def maxProfit1(self, prices: List[int]) -> int:
        res = 0
        min_prices = prices[0]
        for i in range(1, len(prices)):
            if min_prices > prices[i]:
                min_prices = prices[i]
            elif min_prices < prices[i]:
                res = max(res, prices[i]-min_prices)
        return res

# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

