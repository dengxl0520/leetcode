# @lcpr-before-debug-begin
from python3problem491 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=491 lang=python3
# @lcpr version=30204
#
# [491] 非递减子序列
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start_idx, nums, path, res):
            if len(path) > 1:
                res.append(path[:])
            if start_idx == len(nums):
                return
            
            used = set()
            for i in range(start_idx, len(nums)):
                if nums[i] in used or (len(path) > 0 and path[-1] > nums[i]):
                    continue
                used.add(nums[i])
                path.append(nums[i])
                backtracking(i+1, nums, path, res)
                path.pop()
        
        res = []
        backtracking(0, nums, [], res)
        return res
                
# @lc code=end



#
# @lcpr case=start
# [1,2,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,6,7,7]\n
# @lcpr case=end

# @lcpr case=start
# [4,4,3,2,1]\n
# @lcpr case=end

#

