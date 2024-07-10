# @lcpr-before-debug-begin
from python3problem20 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'{': '}', '[':']', '(':')'}
        stack = []
        for i in s:
            if i in d: 
                stack.append(d[i])
            elif len(stack) == 0 or stack.pop() != i:
                return False

        return len(stack) == 0

    def isValid1(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) == 0: return False
                j = stack.pop()
                if not ((j == "(" and i == ")") or (j == "{" and i == "}") or (j == "[" and i == "]")):
                    return False
        if len(stack) != 0:
            return False
        return True
    
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

#

