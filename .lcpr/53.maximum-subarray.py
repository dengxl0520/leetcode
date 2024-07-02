# @lcpr-before-debug-begin
from python3problem53 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:            
    def maxSubArray1(self, nums: List[int]) -> int:
        '''
            思路二: 每一次累加，如果出现更大的，存入res
                    如果count小于0，证明累积无贡献，清零count
        '''
        res = float("-inf")
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > res:
                res = count
            if count <= 0:
                count = 0
        return res
    
    def maxSubArray(self, nums: List[int]) -> int:
        '''
            思路一: 累计的count<0, 代表累积无贡献,
                    则将count重置为当前nums[i]
        '''
        res = float("-inf")
        count = 0
        for i in range(len(nums)):
            if count < 0: 
                count = nums[i]
            else:
                count += nums[i]
            if count > res:
                res = count
        return res
                
                
# @lc code=end



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

