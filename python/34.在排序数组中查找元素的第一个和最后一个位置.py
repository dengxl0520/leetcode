# @before-stub-for-debug-begin
from python3problem34 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List

# @lc code=start
class Solution:
    def search_left(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if left >= len(nums) or nums[left] != target:
            return -1
        return left
    
    def search_right(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if right < 0 or nums[right] != target:
            return -1
        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        print([self.search_left(nums,target), self.search_right(nums, target)])
        return [self.search_left(nums,target), self.search_right(nums, target)]
# @lc code=end

