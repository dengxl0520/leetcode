# @lcpr-before-debug-begin
from python3problem216 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=216 lang=python3
# @lcpr version=30203
#
# [216] 组合总和 III
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtracking(startIndex, k, n, path: List, res):
            if k == 0:
                if sum(path) == n:
                    res.append(path[:])
                return
                
            for i in range(startIndex, 10):
                path.append(i)
                if sum(path) > n: 
                    path.pop()
                    break
                backtracking(i+1, k-1, n, path, res)
                path.pop()
                
        res = []
        backtracking(1, k, n, [], res)
        return res
            
            
            
# @lc code=end



#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n9\n
# @lcpr case=end

# @lcpr case=start
# 4\n1\n
# @lcpr case=end

#

