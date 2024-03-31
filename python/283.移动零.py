# @before-stub-for-debug-begin
from python3problem283 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast, slow = 0,0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow +=1
            fast += 1
        for i in range(slow,len(nums)):
            nums[i] = 0
        print(nums)
# @lc code=end

