# @lcpr-before-debug-begin
from python3problem51 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=51 lang=python3
# @lcpr version=30204
#
# [51] N 皇后
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(start_idx, n, path, res):
            if len(path) == n:
                res.append(path[:])
                return 
            
            for i in range(start_idx, n):
                if path:
                    # 同行同列
                    if i in path: continue
                    # 同斜线


                path.append(i)
                backtracking(0, n, path, res)
                path.pop()

        res = []
        backtracking(0, n, [], res)
        return res


# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

