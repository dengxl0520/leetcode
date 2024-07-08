# @lcpr-before-debug-begin
from python3problem417 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=417 lang=python3
# @lcpr version=30204
#
# [417] 太平洋大西洋水流问题
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        search = [[0,-1], [-1,0], [1,0], [0,1]]
        p_visited = [[False] * n for _ in range(m)]
        a_visited = [[False] * n for _ in range(m)]
        res = []
        def dfs(visited, i, j):
            visited[i][j] = True
            for ii, jj in search:
                if 0<=i+ii<m and 0<=j+jj<n and not visited[i+ii][j+jj]:
                    if heights[i][j] <= heights[i+ii][j+jj]:
                        dfs(visited, i+ii, j+jj)

        for i in range(m):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, n-1)

        for i in range(n):
            dfs(p_visited, 0, i)
            dfs(a_visited, m-1, i)

        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i,j])

        return res

# @lc code=end



#
# @lcpr case=start
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,1],[1,2]]\n
# @lcpr case=end

#

