# @lcpr-before-debug-begin
from python3problem41 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=41 lang=python3
# @lcpr version=30204
#
# [41] 缺失的第一个正数
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if 0 < nums[i] < n and nums[nums[i] - 1] != nums[i]: # 已经暗含了nums[i] != i+1
                key = nums[i]
                nums[i], nums[key-1] = nums[key-1], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1

# @lc code=end



#
# @lcpr case=start
# [1,1]\n
# @lcpr case=end

# @lcpr case=start
# [-1,4,2,1,9,10]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,0]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,-1,1]\n
# @lcpr case=end

# @lcpr case=start
# [7,8,9,11,12]\n
# @lcpr case=end

#

