# @lcpr-before-debug-begin
from python3problem15 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30121
#
# [15] 三数之和
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        
        for i in range(n):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue
            
            k = n-1
            for j in range(i+1, n):
                if j == k: break
                if j > i+1 and nums[j] == nums[j-1]: continue
                while -nums[i]-nums[j] <= nums[k] and j < k:
                    if -nums[i]-nums[j] == nums[k]:
                        ans.append([nums[i],nums[j],nums[k]])
                        break
                    else:
                        k -= 1
        print(ans)
        return ans

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] not in d:
                    d[nums[i]+nums[j]] = [[i, j]]
                elif [nums[i], nums[j]] not in d[nums[i]+nums[j]]:
                    d[nums[i]+nums[j]].append([i, j])
                    
        ans = []
        
        for i in range(len(nums)):
            if -nums[i] in d:
                for e in d[-nums[i]]:
                    if i in e: continue
                    tmp = [nums[e[0]], nums[e[1]], nums[i]]
                    tmp.sort()
                    if tmp not in ans:
                        ans.append(tmp)
                
        return ans
        
# @lc code=end



#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0]\n
# @lcpr case=end

#

