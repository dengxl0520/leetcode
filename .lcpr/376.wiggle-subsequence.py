#
# @lc app=leetcode.cn id=376 lang=python3
# @lcpr version=30204
#
# [376] 摆动序列
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        up, down = 1,1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1

        return max(up, down)

# @lc code=end



#
# @lcpr case=start
# [1,7,4,9,2,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,17,5,10,13,15,10,5,16,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7,8,9]\n
# @lcpr case=end

#

