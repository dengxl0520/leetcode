#
# @lc app=leetcode.cn id=62 lang=python3
# @lcpr version=30204
#
# [62] 不同路径
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
            不能这样创建二维数组
            dp = [[1] * n] * m 
            否则,里层数组会直接指向相同的地址
            >>> m,n = 3, 2         
            >>> dp = [[0] * n] * m 
            >>> dp[0][0] = 1      
            >>> dp
            [[1, 0], [1, 0], [1, 0]]
        '''
        dp = [[0] * n for _ in range(m)]
        
        for i in range(1, m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
            

    def uniquePaths1(self, m: int, n: int) -> int:
        import math
        return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)) 
# @lc code=end



#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

# @lcpr case=start
# 7\n3\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n
# @lcpr case=end

#

