#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30204
#
# [279] 完全平方数
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        tmp = []
        
        for i in range(1, int(n**0.5)+1):
            tmp.append(i*i)
            
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(len(tmp)):
                dp[i] = min(dp[i], dp[i-tmp[j]] + 1)
            
        return dp[-1]
# @lc code=end



#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#

