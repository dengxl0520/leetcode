# @lcpr-before-debug-begin
from python3problem1 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30121
#
# [1] 两数之和
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            d[nums[i]] = i
                
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if target - nums[i] in d:
                return [d[target - nums[i]], i]
            if nums[i] not in d:
                d[nums[i]] = i
            
        
        
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

