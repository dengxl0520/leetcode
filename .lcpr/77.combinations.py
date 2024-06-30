# @lcpr-before-debug-begin
from python3problem77 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=77 lang=python3
# @lcpr version=30203
#
# [77] 组合
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(n, k, startIndex, path:List, result):
            if len(path) == k:
                result.append(path[:]) # 注意path[:]和path的区别
                return 
            for i in range(startIndex, n+1):
                path.append(i)
                backtracking(n,k,i+1,path,result)
                path.pop()
                
        res = []
        backtracking(n,k,1,[],res)
        return res
            
# @lc code=end



#
# @lcpr case=start
# 4\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#

