# @lcpr-before-debug-begin
from python3problem377 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=377 lang=python3
# @lcpr version=30204
#
# [377] 组合总和 Ⅳ
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        '''
            from: 代码随想录
            如果求组合数就是外层for循环遍历物品，内层for遍历背包。
            如果求排列数就是外层for遍历背包，内层for循环遍历物品。
        '''
        dp = [0] * (target+1)
        dp[0] = 1
        for j in range(1, target+1):
            for i in range(len(nums)):  
                if j >= nums[i]:
                    dp[j] = dp[j] + dp[j-nums[i]]
        return dp[-1]
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [9]\n3\n
# @lcpr case=end

#

