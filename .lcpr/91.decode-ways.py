#
# @lc app=leetcode.cn id=91 lang=python3
# @lcpr version=30204
#
# [91] 解码方法
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # dp = [0] * (len(s)+1)
        # dp[0] = 1
        dp = [1] + [0] * len(s)
        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1
        for i in range(1,len(s)):
            if s[i-1] != "0" and int(s[i-1:i+1]) <= 26:
                dp[i+1] += dp[i-1]
            if s[i] != "0":
                dp[i+1] += dp[i]
        return dp[-1]
# @lc code=end



#
# @lcpr case=start
# "10"\n
# @lcpr case=end

# @lcpr case=start
# "226"\n
# @lcpr case=end

# @lcpr case=start
# "06"\n
# @lcpr case=end

#

