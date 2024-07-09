# @lcpr-before-debug-begin
from python3problem392 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=392 lang=python3
# @lcpr version=30204
#
# [392] 判断子序列
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
            bool 
        '''
        dp = [False] * (len(s)+1)
        dp[0] = True
        for i in range(len(t)):
            for j in range(len(s), 0,-1):
                if t[i] == s[j-1]:
                    dp[j] = dp[j-1]
        return dp[-1]

    def isSubsequence2(self, s: str, t: str) -> bool:
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    # dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = dp[i][j-1]
                    # dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        if dp[-1][-1] == len(s):
            return True
        return False
    
    def isSubsequence1(self, s: str, t: str) -> bool:
        '''
            错误解法
        '''
        if s == "": return True
        if t == "": return False
        dp = [False] * (len(t)+1)
        for i in range(1, len(t)+1):
            if s[0] == t[i-1]:
                dp[i] = True
            else:
                dp[i] = dp[i-1]
            # dp[i] = s[0] == t[i-1] or dp[i-1]
        for i in range(1, len(s)):
            for j in range(1, len(t)+1):
                if s[i] == t[j-1]:
                    dp[j] = dp[j]
                else:
                    dp[j] = dp[j-1]
                # dp[i] = ((s[i] == t[j]) or dp[i-1]) and dp[i] 
            if not dp[-1]: return False
        print(dp)
        return dp[-1]
# @lc code=end



#
# @lcpr case=start
# "aaaaaa"\n"bbaaaa"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"ahbgdc"\n
# @lcpr case=end

# @lcpr case=start
# "axc"\n"ahbgdc"\n
# @lcpr case=end

#

