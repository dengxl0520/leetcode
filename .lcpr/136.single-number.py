# @lcpr-before-debug-begin
from python3problem136 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=136 lang=python3
# @lcpr version=30204
#
# [136] 只出现一次的数字
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res
    
    def singleNumber2(self, nums: List[int]) -> int:
        s = set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                s.remove(nums[i])
        return s.pop()

    def singleNumber1(self, nums: List[int]) -> int:
        '''
            TLE
        '''
        for i in range(len(nums)):
            found = False
            for j in range(len(nums)):
                if i == j: continue
                if nums[i] == nums[j]:
                    found = True
                    break
            if not found: 
                return nums[i]
# @lc code=end



#
# @lcpr case=start
# [2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [4,1,2,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

