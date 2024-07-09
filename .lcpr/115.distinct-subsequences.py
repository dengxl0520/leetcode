#
# @lc app=leetcode.cn id=115 lang=python3
# @lcpr version=30204
#
# [115] 不同的子序列
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(s)+1) for i in range(len(t)+1)]
        for i in range(len(s)+1):
            dp[0][i] = 1
        
        for i in range(1, len(t)+1):
            for j in range(1, len(s)+1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        # print(dp)
        return dp[-1][-1]

# @lc code=end



#
# @lcpr case=start
# "rabbbit"\n"rabbit"\n
# @lcpr case=end

# @lcpr case=start
# "babgbag"\n"bag"\n
# @lcpr case=end

#

