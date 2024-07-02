#
# @lc app=leetcode.cn id=509 lang=python3
# @lcpr version=30204
#
# [509] 斐波那契数
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1: 
            return n
        dp1, dp2 = 0, 1
        for i in range(n-1):
            tmp = dp1 + dp2
            dp1 = dp2
            dp2 = tmp
            
        return dp2
    
    def fib1(self, n: int) -> int:
        if n == 0: return 0
        dp = [0] * (n+1)
        dp[0], dp[1] = 0,1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
        
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

