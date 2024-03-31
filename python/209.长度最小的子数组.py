# @before-stub-for-debug-begin
from python3problem209 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow, fast = 0,0
        sum = 0
        min_len = len(nums)+1
        while fast < len(nums):
            sum += nums[fast]
            while sum >= target:
                cur_len = fast - slow + 1
                if cur_len < min_len:
                    min_len = cur_len
                sum -= nums[slow]
                slow += 1
            fast += 1
        if min_len == len(nums) +1:
            return 0
        return min_len
# @lc code=end

