# @lcpr-before-debug-begin
from python3problem131 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30204
#
# [131] 分割回文串
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        s = list(s)
        def isPalindrome(start_idx, end_idx, s):
            while start_idx < end_idx:
                if s[start_idx] != s[end_idx]: 
                    return False
                else:
                    start_idx += 1
                    end_idx -= 1
            return True

        def backtracking(start_idx, s, path, res):
            if start_idx == len(s):
                res.append(path[:])
                return
            
            for cur_idx in range(start_idx, len(s)):
                if isPalindrome(start_idx, cur_idx, s):
                    path.append("".join(s[start_idx:cur_idx+1]))
                    backtracking(cur_idx+1,s, path, res)
                    path.pop()
                else:
                    continue
        
        res = []
        backtracking(0, s, [], res)
        return res





# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end
    
# @lcpr case=start
# "abbab"\n
# @lcpr case=end

#

