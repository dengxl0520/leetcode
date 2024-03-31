# @before-stub-for-debug-begin
from python3problem977 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:        
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        left, right = 0,len(nums)-1
        res = []
        while left != right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left]*nums[left])
                left +=1
            else:
                res.append(nums[right]*nums[right])
                right -=1
        res.append(nums[left]*nums[left])
        res.reverse()
        print(res)
        return res
    
    def sortedSquares1(self, nums: List[int]) -> List[int]:
        return sorted(num * num for num in nums)
    
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # 先创建好空间然后逆序放入，可以不反转
        left, right = 0, len(nums)-1 
        pos = len(nums) - 1
        res = [0] * len(nums)
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos] = nums[left]*nums[left]
                left +=1
            else:
                res[pos] = nums[right]*nums[right]
                right -=1
            pos -= 1
        print(res)
        return res


# @lc code=end

