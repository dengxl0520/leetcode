#
# @lc app=leetcode.cn id=134 lang=python3
# @lcpr version=30204
#
# [134] 加油站
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
            如果累积油量小于0,则证明不可能从该点出发
            找到累积油量大于零的最后的下标
        '''
        if sum(gas) < sum(cost): return -1
        res = [i-j for i,j in zip(gas, cost)]
        cur_sum = 0
        cur_index = 0
        for i in range(len(res)):
            cur_sum += res[i]
            if cur_sum < 0:
                cur_sum = 0
                cur_index = i+1

        return cur_index

    
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        """
            暴力做法,TLE
        """
        for i in range(len(gas)):
            # find a start point
            if gas[i] >= cost[i]:
                cur_gas = 0
                for j in range(len(gas)):
                    cur_idx = (i+j) % len(gas)
                    cur_gas = cur_gas + gas[cur_idx] - cost[cur_idx]
                    if cur_gas < 0:
                        break
                if cur_gas >= 0: return i
        return -1


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n[3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,4]\n[3,4,3]\n
# @lcpr case=end

#

