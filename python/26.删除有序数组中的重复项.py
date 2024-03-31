# @before-stub-for-debug-begin
from python3problem26 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast,slow = 1,1
        while fast < len(nums):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast]
                slow = slow + 1
            fast = fast + 1
        # print(nums[:slow])
        return slow
    
    def removeDuplicates1(self, nums: List[int]) -> int:
        fast,slow = 0,0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow = slow + 1
                nums[slow] = nums[fast]
            fast = fast + 1
        print(nums[:slow +1])
        return slow + 1
   
# @lc code=end

