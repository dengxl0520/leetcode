# @lcpr-before-debug-begin
from python3problem957 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=957 lang=python3
# @lcpr version=30204
#
# [957] N 天后的牢房
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        res = cells[:]
        for j in range(1, len(cells)-1):
            if cells[j-1] == cells[j+1]:
                res[j] = 1
            else:
                res[j] = 0
        res[0], res[-1] = 0,0
        cycle = []
        cycle.append(res[:])
        for _ in range(n-1):
            tmp = []
            for j in range(8):
                if j==0 or j==7 or cycle[-1][j-1] != cycle[-1][j+1]:
                    tmp.append(0)
                else:
                    tmp.append(1)
            if tmp == res:
                break
            cycle.append(tmp[:])
        
        return cycle[(n-1)%len(cycle)]

    def prisonAfterNDays1(self, cells: List[int], n: int) -> List[int]:
        '''
            暴力 TLE
        '''
        res = cells[:]
        for i in range(n):
            for j in range(1, len(cells)-1):
                if cells[j-1] == cells[j+1]:
                    res[j] = 1
                else:
                    res[j] = 0
            if i == 0 : 
                res[0], res[-1] = 0,0
            cells = res[:]
        return res
# @lc code=end



#
# @lcpr case=start
# [0,1,0,1,1,0,0,1]\n7\n
# @lcpr case=end

# @lcpr case=start
# [1,0,0,1,0,0,1,0]\n1000000000\n
# @lcpr case=end

#

