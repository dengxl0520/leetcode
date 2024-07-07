#
# @lc app=leetcode.cn id=503 lang=python3
# @lcpr version=30204
#
# [503] 下一个更大元素 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i in range(2*len(nums)):
            idx = i % len(nums)
            while len(stack) > 0 and nums[stack[-1]] < nums[idx]:
                res[stack[-1]] = nums[idx]
                stack.pop()
            stack.append(idx)
        
        return res

# @lc code=end



#
# @lcpr case=start
# [1,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,3]\n
# @lcpr case=end

#

