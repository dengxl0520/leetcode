# @lcpr-before-debug-begin
from python3problem119 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=119 lang=python3
# @lcpr version=30204
#
# [119] 杨辉三角 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex+1)
        for i in range(rowIndex+1):
            for j in range(i-1, 0, -1):
                row[j] += row[j-1]
        return row

    def getRow1(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex+1):
            tmp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    tmp.append(1)
                else:
                    tmp.append(row[j-1]+row[j])
            row = tmp
        return row
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

