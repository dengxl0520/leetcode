# @lcpr-before-debug-begin
from python3problem343 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=343 lang=python3
# @lcpr version=30204
#
# [343] 整数拆分
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        '''
            dp[i] dp[i-j]*j (i-j)*j
            i=10, j=3
            dp[10] dp[7]*3 7*3
        '''
        dp = [0] * (n+1)
        dp[0],dp[1] = 0,1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[i-j]*j, (i-j)*j)

        return dp[-1]
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#

