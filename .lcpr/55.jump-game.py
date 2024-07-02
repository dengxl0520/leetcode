# @lcpr-before-debug-begin
from python3problem55 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30204
#
# [55] 跳跃游戏
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        max_index = 0
        for i in range(len(nums)):
            if max_index < i: return False
            max_index = max(i+nums[i], max_index)
            
        return True

    
    def canJump1(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        res = [False] * len(nums)
        res[0] = True
        for i in range(len(nums)):
            if not res[i]: break 
            if nums[i] != 0:
                for j in range(i, min(i+nums[i]+1, len(nums))):
                    res[j] = True
        return res[-1]
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#

