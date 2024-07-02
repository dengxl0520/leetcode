#
# @lc app=leetcode.cn id=122 lang=python3
# @lcpr version=30204
#
# [122] 买卖股票的最佳时机 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                res += prices[i] - prices[i-1]
        return res
    
    def maxProfit1(self, prices: List[int]) -> int:
        price = prices[0]
        res = 0
        for cur_price in prices[1:]:
            if cur_price > price:
                res += cur_price - price
            price = cur_price
        return res

# @lc code=end



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

