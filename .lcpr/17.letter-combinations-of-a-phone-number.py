# @lcpr-before-debug-begin
from python3problem17 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30203
#
# [17] 电话号码的字母组合
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        d = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["q","p","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }
        
        
        def backtracking(index, digits: str, path: List, res):
            if len(path) == len(digits):
                res.append("".join(path))
                return

            for char in d[digits[index]]:
                path.append(char)
                backtracking(index+1, digits, path, res)
                path.pop()
            
        res = []
        backtracking(0,digits, [], res)
        return res
                
            
        
# @lc code=end



#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#

