# @lcpr-before-debug-begin
from python3problem695 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=695 lang=python3
# @lcpr version=30204
#
# [695] 岛屿的最大面积
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        search = [[0,-1], [-1,0], [1,0], [0,1]]
        res = 0
        def bfs(i, j):
            area = 1
            node = [[i,j]]
            while len(node)>0:
                i,j = node[-1]
                node.pop()
                for ii,jj in search:
                    if 0<=i+ii<m and 0<=j+jj<n and grid[i+ii][j+jj] == 1 and not visited[i+ii][j+jj]:
                        area+= 1
                        visited[i+ii][j+jj] = True
                        node.append([i+ii, j+jj])

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    res = max(bfs(i,j), res)
        return res

# @lc code=end



#
# @lcpr case=start
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0,0,0,0,0,0]]\n
# @lcpr case=end

#

