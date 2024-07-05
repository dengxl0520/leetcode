#
# @lc app=leetcode.cn id=1049 lang=python3
# @lcpr version=30204
#
# [1049] 最后一块石头的重量 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        res = sum(stones)
        target = res // 2 # 容量到和的一半就够了

        dp = [0] * (target+1)
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])

        return res - 2*dp[-1]
    
    def lastStoneWeightII1(self, stones: List[int]) -> int:
        target = sum(stones)
        res = target

        dp = [0] * (target+1)
        for i in range(len(stones)):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
                if target - 2*dp[j] >= 0:
                    res = min(res, target - 2*dp[j])
        return res
# @lc code=end



#
# @lcpr case=start
# [2,7,4,1,8,1]\n
# @lcpr case=end

# @lcpr case=start
# [31,26,33,21,40]\n
# @lcpr case=end

#

