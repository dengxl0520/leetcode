# @lcpr-before-debug-begin
from python3problem96 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=96 lang=python3
# @lcpr version=30204
#
# [96] 不同的二叉搜索树
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        '''
            dp[2] = dp[0] * dp[1] + dp[1] * dp[0]
            dp[3] = dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[0]
        '''
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[-1]

# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

