#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30204
#
# [322] 零钱兑换
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
            我们不能一次凑齐amount(很难)，因此我们需要从1推导到amount
            显然从n-i到n是存在重叠的。
            假设我们要凑齐n最少要m个硬币，那么凑齐n+coins[i]只需要m+1个。
        '''
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if j <= amount:
                    dp[i] = min(dp[i-j] + 1, dp[i])
        # print(dp)
        return dp[-1] if dp[-1] != amount+1 else -1
    
# @lc code=end



#
# @lcpr case=start
# [2,3,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

