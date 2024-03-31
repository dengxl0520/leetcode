# @lcpr-before-debug-begin
from python3problem18 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=18 lang=python3
# @lcpr version=30121
#
# [18] 四数之和
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]: continue
                p = n-1
                for k in range(j+1, n):
                    if k > j+1 and nums[k] == nums[k-1]: continue
                    if p == k: break
                    while nums[i] + nums[j] + nums[k] + nums[p] >= target and k < p:
                        if nums[i] + nums[j] + nums[k] + nums[p] == target:
                            ans.append([nums[i], nums[j], nums[k], nums[p]])
                            break
                        else:
                            p -=1
        return ans
                    
# @lc code=end



#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#

