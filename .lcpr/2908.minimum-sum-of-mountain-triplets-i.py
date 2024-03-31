# @lcpr-before-debug-begin
from python3problem2908 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=2908 lang=python3
# @lcpr version=30121
#
# [2908] 元素和最小的山形三元组 I
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:        
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        mn = nums[0]
        for i in range(1, n):
            left[i] = mn = min(mn, nums[i-1])
        
        right = nums[n-1]
        ans = 1000
        for i in range(n-2, 0, -1):
            if left[i] < nums[i] and nums[i] > right:
                ans = min(ans, left[i] + nums[i] + right)
            right = min(right, nums[i])
        
        return ans if ans != 1000 else -1
            
        
    def minimumSum2(self, nums: List[int]) -> int:
        min_index = 0
        for i in range(len(nums)):
            if nums[min_index] > nums[i]:
                min_index = i
        
        left_sum = 999999999
        for i in range(0, min_index):
            for j in range(i+1, min_index):
                if nums[i] < nums[j]:
                    left_sum = min(left_sum, nums[i]+nums[j])
                    
        right_sum = 999999999
        for i in range(min_index+1, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    right_sum = min(right_sum, nums[i]+nums[j])
        
        if left_sum == 999999999 and right_sum == 999999999:
            return -1
        elif left_sum == 999999999:
            return right_sum + nums[min_index]
        elif right_sum == 999999999:
            return left_sum + nums[min_index]
        else:
            return min(right_sum + nums[min_index], left_sum + nums[min_index])
        
    def minimumSum1(self, nums: List[int]) -> int:
        ans = 100000
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] and nums[i+2] < nums[i+1]:
                _sum = nums[i] + nums[i+1] + nums[i+2] 
                ans = min(_sum, ans)
                    
        return ans
        
# @lc code=end


# @lcpr-div-debug-arg-start
# funName=minimumSum
# paramTypes= ["number[]"]
# @lcpr-div-debug-arg-end




#
# @lcpr case=start
# [8,6,1,5,3]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,7,10,2]\n
# @lcpr case=end

# @lcpr case=start
# [6,5,4,3,4,5]\n
# @lcpr case=end

#

