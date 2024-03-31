# @before-stub-for-debug-begin
from python3problem48 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        print(n//2)
        for i in range((n+1)//2): # 注意需要遍历的元素
            for j in range(n//2): # 注意需要遍历的元素
                # print(i,j)
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp
        # print(matrix)
# @lc code=end

