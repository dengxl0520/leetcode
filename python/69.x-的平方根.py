# @before-stub-for-debug-begin
from python3problem69 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1,x
        while left <= right:
            mid = (left + right) // 2
            if mid**2 > x:
                right = mid -1
            elif mid**2 < x:
                left = mid + 1
            elif mid **2 == x:
                return mid
        return right
# @lc code=end

