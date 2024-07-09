# @lcpr-before-debug-begin
from python3problem718 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=718 lang=python3
# @lcpr version=30204
#
# [718] 最长重复子数组
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        dp = [[0] * len(nums1) for _ in range(len(nums2))]
        for i in range(len(nums1)):
            if nums1[i] == nums2[0]:
                dp[0][i] = 1
            res = max(res, dp[0][i])

        for i in range(len(nums2)):
            if nums1[0] == nums2[i]:
                dp[i][0] = 1
            res = max(res, dp[i][0])

        for i in range(1,len(nums2)):
            for j in range(1,len(nums1)):                    
                if nums2[i] == nums1[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res = max(dp[i][j], res)
        # print(dp)
        return res
# @lc code=end



#
# @lcpr case=start
# [1,2,3,2,8]\n[5,6,1,4,7]\n
# @lcpr case=end
    
# @lcpr case=start
# [1,2,3,2,1]\n[3,2,1,4,7]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0,0]\n[0,0,0,0,0]\n
# @lcpr case=end

#

