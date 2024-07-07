# @lcpr-before-debug-begin
from python3problem416 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30204
#
# [416] 分割等和子集
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
            思路2：dp,将元素当作物品的重量和价值，背包大小为sum/2
            尽量放满背包，如果能放满，即return True
        '''
        target = sum(nums)
        if len(nums) < 2 or target % 2 == 1:
            return False
        target = target // 2

        dp = [0] * (target+ 1)
        '''
            为什么要先物品后背包：
                滚动数组，数组只记录第i件物品时各容量的状态
                模拟一件件物品尝试添加，每次来第i件物品，
                取决于第i-1件物品的状态（包括容量够放入i物品和不放i物品的状态）
            
            for j in range(target, nums[i]-1, -1):
            为什么要倒序遍历dp，因为当前状态容量大的时候，依赖上个状态容量小的时候的值，
            所以需要从大的开始遍历，如果使用二维dp可以正常遍历

            max(
                dp[j], 因为使用了滚动数组, dp[j]就是上一个状态的
                dp[j - nums[i]] + nums[i], 正常的背包dp
            )
        '''

        for i in range(len(nums)):                  # 物品
            for j in range(target, nums[i]-1, -1):  # 背包
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        if dp[target] == target:
            return True
        return False


    def canPartition1(self, nums: List[int]) -> bool:
        '''
            思路1：回溯法，可能超时，只是写下思路
        '''
        target = sum(nums)
        if len(nums) < 2 or target % 2 == 1:
            return False
        target = target / 2

        def backtracking(index, target, path_sum, nums):
            if path_sum == target: 
                return True
            elif path_sum > target:
                return False

            for i in range(index, len(nums)):
                path_sum += nums[i]
                if backtracking(i+1, target, path_sum, nums):
                    return True
                else:
                    path_sum -= nums[i]

            return False
        
        return backtracking(0, target, 0, nums)
        
# @lc code=end



#
# @lcpr case=start
# [2,2,3,5]\n
# @lcpr case=end
    
# @lcpr case=start
# [1,2,5]\n
# @lcpr case=end
    
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#

