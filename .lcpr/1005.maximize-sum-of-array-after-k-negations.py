# @lcpr-before-debug-begin
from python3problem1005 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=1005 lang=python3
# @lcpr version=30204
#
# [1005] K 次取反后最大化的数组和
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 从绝对值最大开始处理，确保从收益最大的开始
        nums.sort(key=lambda x: abs(x), reverse=True) 

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
            
        if k % 2 == 1:
            nums[-1] *= -1

        return sum(nums)
    
    def largestSumAfterKNegations1(self, nums: List[int], k: int) -> int:
        nums.sort()
        idx = 0
        for i in range(k):
            if idx < len(nums) and nums[idx] < 0:
                nums[idx] = -nums[idx]
                idx += 1
            else:
                nums.sort()
                return sum(nums[1:]) + (-1)**(k-i)*nums[0]
        return sum(nums)

# @lc code=end



#
# @lcpr case=start
# [4,2,3]\n1\n
# @lcpr case=end
    
# @lcpr case=start
# [-2,9,9,8,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,-1,0,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,-3,-1,5,-4]\n2\n
# @lcpr case=end

#

