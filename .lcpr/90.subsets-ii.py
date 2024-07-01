# @lcpr-before-debug-begin
from python3problem90 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=90 lang=python3
# @lcpr version=30204
#
# [90] 子集 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtracking(start_idx, nums, path, res):
            res.append(path[:])
            if start_idx == len(nums):
                return
            
            for i in range(start_idx, len(nums)):
                if start_idx != i and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(i+1, nums, path, res)
                path.pop()

        res = []
        backtracking(0, nums, [], res)
        return res


# @lc code=end



#
# @lcpr case=start
# [1,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

