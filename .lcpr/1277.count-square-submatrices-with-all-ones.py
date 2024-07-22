#
# @lc app=leetcode.cn id=1277 lang=python3
# @lcpr version=30204
#
# [1277] 统计全为 1 的正方形子矩阵
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        dp = [[0]*n for i in range(m)]
        dp[0][0] = matrix[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + matrix[i][0]
        for i in range(1,n):
            dp[0][i] = dp[0][i-1] + matrix[0][i]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + matrix[i][j]
                # if matrix[i][j] == 1 and matrix[i-1][j-1]==1 and matrix[i-1][j]==1 and matrix[i][j-1]==1:
                #     dp[i][j] += 1

        print(dp)
        return dp[-1][-1]
# @lc code=end



#
# @lcpr case=start
# [[0,1,1,1],[1,1,1,1],[0,1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,1],[1,1,0],[1,1,0]]\n
# @lcpr case=end

#

