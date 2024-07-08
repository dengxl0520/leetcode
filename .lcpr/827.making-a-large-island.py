#
# @lc app=leetcode.cn id=827 lang=python3
# @lcpr version=30204
#
# [827] 最大人工岛
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        d = {}
        # visited = [[False]* n for _ in range(m)]
        search = [[-1,0], [0,-1], [1,0], [0,1]]
        grid_id = 2
        
        def dfs(i,j):
            area = 1
            grid[i][j] = grid_id
            for ii, jj in search:
                x,y = i+ii, j+jj
                if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                    area += dfs(x,y)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    d[grid_id] = dfs(i,j)
                    grid_id += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 1
                    visited = set()
                    for ii, jj in search:
                        x,y = i+ii, j+jj
                        if 0<=x<m and 0<=y<n and grid[x][y] > 0 and grid[x][y] not in visited:
                            area += d[grid[x][y]]
                            visited.add(grid[x][y])
                    res = max(res, area)
        if res == 0:
            return max(d.values())
        return res
    

    def largestIsland1(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        d = {}
        # visited = [[False]* n for _ in range(m)]
        search = [[-1,0], [0,-1], [1,0], [0,1]]
        grid_id = 2
        area = 0
        def dfs(i,j):
            nonlocal area 
            area += 1
            grid[i][j] = grid_id
            for ii, jj in search:
                x,y = i+ii, j+jj
                if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                    dfs(x,y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i,j)
                    d[grid_id] = area
                    grid_id += 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 1
                    visited = []
                    for ii, jj in search:
                        x,y = i+ii, j+jj
                        if 0<=x<m and 0<=y<n and grid[x][y] > 0 and grid[x][y] not in visited:
                            area += d[grid[x][y]]
                            visited.append(grid[x][y])
                    res = max(res, area)
        if res == 0:
            return max(d.values())
        return res
# @lc code=end



#
# @lcpr case=start
# [[1, 0], [0, 1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1, 1], [1, 0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1, 1], [1, 1]]\n
# @lcpr case=end

#

