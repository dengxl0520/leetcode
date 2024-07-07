#
# @lc app=leetcode.cn id=474 lang=python3
# @lcpr version=30204
#
# [474] 一和零
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        '''
            zeroNum, oneNum = nums[k].count("0"), nums[k].count("1")
            dp[i][j]代表i个0，j个1的最大子集数
            时间复杂度：m*n*len(strs)
        '''
        dp = [[0] * (n+1) for _ in range(m+1)]


        for str in strs:
            zeroNum, oneNum = str.count("0"), str.count("1")
            for i in range(m, zeroNum-1, -1):
                for j in range(n, oneNum-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)

        return dp[-1][-1]
# @lc code=end



#
# @lcpr case=start
# ["10", "0001", "111001", "1", "0"]\n5\n3\n
# @lcpr case=end

# @lcpr case=start
# ["10", "0", "1"]\n1\n1\n
# @lcpr case=end

#

