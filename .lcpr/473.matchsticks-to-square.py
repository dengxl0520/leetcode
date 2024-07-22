#
# @lc app=leetcode.cn id=473 lang=python3
# @lcpr version=30204
#
# [473] 火柴拼正方形
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        '''
            错误
        '''
        if len(matchsticks) < 4 or sum(matchsticks) % 4 != 0:
            return False
        average = sum(matchsticks) // 4
        if max(matchsticks) > average:
            return False
        
        dp = [0] + [0] * average
        for i in range(len(matchsticks)):
            for j in range(average, 0, -1):
                if j == matchsticks[i]:
                    dp[j] += 1
                elif j > matchsticks[i] and dp[j-matchsticks[i]] > 0:
                    dp[j] += 1
            print(dp)
        return True if dp[-1] == 4 else False

# @lc code=end



#
# @lcpr case=start
# [5,5,5,5,4,4,4,4,3,3,3,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,4]\n
# @lcpr case=end

#

