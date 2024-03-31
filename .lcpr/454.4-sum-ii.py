#
# @lc app=leetcode.cn id=454 lang=python3
# @lcpr version=30121
#
# [454] 四数相加 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = {}
        for i in nums1:
            for j in nums2:
                d[i+j] = d[i+j] +1 if i+j in d else 1
        ans = 0
        for i in nums3:
            for j in nums4:
                if -i-j in d:
                    ans += d[-i-j]
        return ans
                     
# @lc code=end



#
# @lcpr case=start
# [1,2]\n[-2,-1]\n[-1,2]\n[0,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n[0]\n[0]\n
# @lcpr case=end

#

