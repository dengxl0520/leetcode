#
# @lc app=leetcode.cn id=2970 lang=python3
# @lcpr version=30204
#
# [2970] 统计移除递增子数组的数目 I
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l = 1
        while l < n and nums[l-1] < nums[l]:
            l += 1
        res += l + (l < n)
        for r in range(n - 2, -1, -1):
            while l > 0 and nums[l - 1] >= nums[r + 1]:
                l -= 1
            res += l + (l <= r)
            if nums[r] >= nums[r + 1]:
                break
        return res

    def incremovableSubarrayCount1(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i,n):
                flag = True
                new_nums = nums[:i]+nums[j+1:]
                for k in range(1, len(new_nums)):
                    if new_nums[k-1] >= new_nums[k]:
                        flag = False
                if flag: res += 1
        return res    
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,4,3,2,1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [6,5,7,8]\n
# @lcpr case=end

# @lcpr case=start
# [8,7,6,6]\n
# @lcpr case=end

#

