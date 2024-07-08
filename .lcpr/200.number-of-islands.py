# @lcpr-before-debug-begin
from python3problem200 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=200 lang=python3
# @lcpr version=30204
#
# [200] 岛屿数量
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            bfs version
        '''
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        search = [[0,-1], [-1,0], [1,0], [0,1]]
        res = 0
        def bfs(i,j):
            queue = [[i,j]]
            while len(queue) > 0:
                i,j = queue[-1]
                queue.pop()
                for ii, jj in search:
                    if  0 <= i+ii < len(grid) and 0 <= j+jj < len(grid[0]) and grid[i+ii][j+jj] == '1' and not visited[i+ii][j+jj]:
                        visited[i+ii][j+jj] = True
                        queue.append([i+ii, j+jj])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    res += 1
                    bfs(i,j)
                    
        return res
    
    def numIslands1(self, grid: List[List[str]]) -> int:
        '''
            dfs version
        '''
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        search = [[0,-1], [-1,0], [1,0], [0,1]]
        res = 0
        def dfs(i,j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                if not visited[i][j]:
                    visited[i][j] = True
                    for ii, jj in search:
                        dfs(i+ii, j+jj)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    res += 1
                    dfs(i,j)
                    
        return res

# @lc code=end



#
# @lcpr case=start
# [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]\n
# @lcpr case=end

# @lcpr case=start
# [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]\n
# @lcpr case=end

#

