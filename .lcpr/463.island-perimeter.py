#
# @lc app=leetcode.cn id=463 lang=python3
# @lcpr version=30204
#
# [463] 岛屿的周长
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        search = [[0,1], [1,0], [-1,0], [0,-1]]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: continue
                for ii, jj in search:
                    x,y = ii+i, jj+j
                    if x>=m or x<0 or y>=n or y<0 or grid[x][y] == 0:
                        res += 1

        return res
# @lc code=end



#
# @lcpr case=start
# [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0]]\n
# @lcpr case=end

#

