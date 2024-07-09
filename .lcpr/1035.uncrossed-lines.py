#
# @lc app=leetcode.cn id=1035 lang=python3
# @lcpr version=30204
#
# [1035] 不相交的线
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums1)+1) for _ in range(len(nums2)+1)]
        for i in range(1, len(nums2)+1):
            for j in range(1, len(nums1)+1):
                if nums1[j-1] == nums2[i-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
# @lc code=end



#
# @lcpr case=start
# [1,4,2]\n[1,2,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,5,1,2,5]\n[10,5,2,1,5,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,7,1,7,5]\n[1,9,2,5,1]\n
# @lcpr case=end

#

