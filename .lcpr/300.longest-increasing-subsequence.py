#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30204
#
# [300] 最长递增子序列
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
            题意：求第i个元素前有多少个比nums[i]小的？
            状态转移：与前i个元素比较，如果比他大，长度就+1
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        '''
        res = 1
        dp = [1]* len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[-1]) # 答案可能出现在第i个元素上，而不是最后一个
        return res

    def lengthOfLIS1(self, nums: List[int]) -> int:
        res = 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > res: 
                res = dp[i]
        return res
# @lc code=end



#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#

