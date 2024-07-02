# @lcpr-before-debug-begin
from python3problem45 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30204
#
# [45] 跳跃游戏 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
            核心：每个格子都能达到
            以最小的步数增加覆盖范围，覆盖范围一旦覆盖了终点，得到的就是最少步数
        '''
        ans = 0
        cur_dis, max_dis = 0,0
        for i in range(len(nums)-1):
            max_dis = max(nums[i] + i, max_dis)  # 每一步更新最远覆盖距离
            if i == cur_dis:  # 到达最远覆盖边界
                cur_dis = max_dis
                ans += 1
        return ans

    def jump1(self, nums: List[int]) -> int:
        ans = 0
        cur_dis, next_dis = 0,0
        for i in range(len(nums)-1):
            next_dis = max(nums[i] + i, next_dis)
            if i == cur_dis:
                cur_dis = next_dis
                ans += 1
        return ans

            
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

