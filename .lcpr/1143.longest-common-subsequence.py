# @lcpr-before-debug-begin
from python3problem1143 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=1143 lang=python3
# @lcpr version=30204
#
# [1143] 最长公共子序列
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
            为左上边添加一条0的边，防止dp[i-1][j-1]取到越界
        '''

        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
# @lc code=end


# @lcpr-div-debug-arg-start
# funName=longestCommonSubsequence
# paramTypes= ["string","string"]
# @lcpr-div-debug-arg-end


#
# @lcpr case=start
# "oxcpqrsvwf"\n"shmtulqrypy"\n
# @lcpr case=end
    
# @lcpr case=start
# "abcde"\n"ace"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"def"\n
# @lcpr case=end

#

