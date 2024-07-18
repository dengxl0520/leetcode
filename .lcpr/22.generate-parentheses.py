# @lcpr-before-debug-begin
from python3problem22 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30204
#
# [22] 括号生成
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        
        def dfs(left_num,right_num):
            if len(path) == 2*n:
                res.append("".join(path))
                return

            if left_num < n:
                path.append("(")
                dfs(left_num+1, right_num)
                path.pop()
            if left_num > right_num:
                path.append(")")
                dfs(left_num, right_num+1)
                path.pop()
                
        dfs(0,0)
        return res
# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

