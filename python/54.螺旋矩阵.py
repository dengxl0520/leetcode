#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
# @lc code=end

# @before-stub-for-debug-begin
from python3problem54 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m,n = len(matrix[0]), len(matrix)
        xmin, xmax, ymin, ymax = 0,n-1,0,m-1
        x,y = 0,0
        while xmin < xmax and ymin < ymax : # 边界符合规则
            while ymin <= y and y < ymax:
                ans.append(matrix[x][y])
                y += 1
            while xmin <= x and x < xmax:
                ans.append(matrix[x][y])
                x += 1
            while ymin < y and y <= ymax:
                ans.append(matrix[x][y])
                y -= 1
            while xmin < x and x <= xmax:
                ans.append(matrix[x][y])
                x -= 1
            x += 1
            y += 1
            xmin +=1
            ymin +=1
            xmax -=1
            ymax -=1
        if xmin == xmax and ymin == ymax:
            ans.append(matrix[x][y])
        elif xmin == xmax:
            while y <= ymax:
                ans.append(matrix[x][y])
                y+=1
        elif ymin == ymax:
            while x <= xmax:
                ans.append(matrix[x][y])
                x+=1
        print(ans)
        return ans

# @lc code=end

