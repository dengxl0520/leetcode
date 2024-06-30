# @lcpr-before-debug-begin
from python3problem40 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=40 lang=python3
# @lcpr version=30203
#
# [40] 组合总和 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backtracking(candidates, index, target, path, res):
            _sum = sum(path)
            if _sum > target:
                return
            elif _sum == target:
                res.append(path[:])
                return 
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtracking(candidates, i+1, target, path, res)
                path.pop()
                
        res = []
        backtracking(candidates, 0, target, [], res)
        print(res)
        return res

# @lc code=end



#
# @lcpr case=start
# [10,1,2,7,6,1,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2,5,2,1,2]\n5\n
# @lcpr case=end

#

