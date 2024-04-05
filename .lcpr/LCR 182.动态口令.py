# @lcpr-before-debug-begin
from python3problem182 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=LCR 182 lang=python3
# @lcpr version=30121
#
# [LCR 182] 动态口令
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def reserve(self, password, begin, end):
        for i in range(begin, (begin+end+1)//2):
            password[i], password[end-i+begin] = password[end-i+begin], password[i]
        
    def dynamicPassword(self, password: str, target: int) -> str:
        password = list(password)
        self.reserve(password, 0, target-1)
        self.reserve(password, target, len(password)-1)
        self.reserve(password, 0, len(password)-1)
        return "".join(password)
    
    def dynamicPassword2(self, password: str, target: int) -> str:
        return password[target:] + password[:target] 
    
    def dynamicPassword1(self, password: str, target: int) -> str:
        ans = []
        for i in range(target, len(password)):
            ans.append(password[i])
        for i in range(0, target):
            ans.append(password[i])
        return "".join(ans)
# @lc code=end


# @lcpr-div-debug-arg-start
# funName=dynamicPassword
# paramTypes= ["string","number"]
# @lcpr-div-debug-arg-end




#
# @lcpr case=start
# "s3cur1tyC0d3"\n4\n
# @lcpr case=end

# @lcpr case=start
# "lrloseumgh"\n6\n
# @lcpr case=end

#

