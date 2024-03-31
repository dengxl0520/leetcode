# @before-stub-for-debug-begin
from python3problem59 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0]*n for _ in range(n)]
        index = 1
        for i in range((n+1)//2):
            for j in range(i, n-1-i):
                ans[i][j] = index
                index +=1
            for j in range(i, n-1-i):
                ans[j][n-1-i] = index
                index +=1
            for j in range(i, n-1-i):
                ans[n-1-i][n-1-j] = index 
                index +=1
            for j in range(i, n-1-i):
                ans[n-1-j][i] = index
                index +=1
        if n % 2 == 1:
            ans[n//2][n//2] = index
        # print(ans)
        return ans
    
    # [[1, 2, 3, 4], 
    #  [12, 20, 15, 5], 
    #  [11, 19, 17, 6],
    #  [10, 9, 8, 7]]
            
# @lc code=end

