# @lcpr-before-debug-begin
from python3problem31 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=31 lang=python3
# @lcpr version=30204
#
# [31] 下一个排列
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:                
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return
        n = len(nums)
        left = n-2
        while left >= 0 and nums[left] >= nums[left+1]:
            left -= 1
        
        if left >= 0:
            # find right
            right = left+1
            for i in range(n-1, left-1, -1):
                if nums[left] < nums[i]:
                    right = i
                    break
            # swap
            nums[left], nums[right] = nums[right], nums[left]

        left, right = left+1, n-1
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1



            
# @lc code=end



#
# @lcpr case=start
# [4,2,0,2,3,2,0]\n
# @lcpr case=end
        
# @lcpr case=start
# [1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5]\n
# @lcpr case=end

#

