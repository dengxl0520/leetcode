# @lcpr-before-debug-begin
from python3problem39 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30203
#
# [39] 组合总和
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(candidates, index, target, path, res):
            _sum = sum(path)
            if _sum > target:
                return
            elif _sum == target:
                res.append(path[:])
                return 
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtracking(candidates, i, target, path, res)
                path.pop()
                
        res = []
        backtracking(candidates, 0, target, [], res)
        print(res)
        return res
                
# @lc code=end



#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#

