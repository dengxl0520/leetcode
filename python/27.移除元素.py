# @before-stub-for-debug-begin
from python3problem27 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast, slow, length = 0,0, len(nums)
        while fast < len(nums):
            if nums[fast] == val:
                fast = fast + 1
                length = length - 1
            else:
                nums[slow] = nums[fast]
                fast = fast + 1
                slow = slow + 1
        # print(nums[:length])
        return length
    
    def removeElement1(self, nums: List[int], val: int) -> int:
        fast, slow = 0,0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow = slow + 1
            fast = fast + 1
        return slow

            
# @lc code=end

