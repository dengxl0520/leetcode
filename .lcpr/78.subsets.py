# @lcpr-before-debug-begin
from python3problem78 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=30204
#
# [78] 子集
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start_idx, nums, path, res):
            res.append(path[:])
            if start_idx == len(nums):
                return
            
            for i in range(start_idx, len(nums)):
                path.append(nums[i])
                backtracking(i+1, nums, path, res)
                path.pop()

        res = []
        backtracking(0, nums, [], res)
        return res

# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

