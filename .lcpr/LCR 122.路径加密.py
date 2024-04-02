# @lcpr-before-debug-begin
from python3problem122 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=LCR 122 lang=python3
# @lcpr version=30121
#
# [LCR 122] 路径加密
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def pathEncryption(self, path: str) -> str:
        path = list(path)
        for i in range(len(path)):
            if path[i] == ".": path[i] = " "
        print("".join(path))
        return "".join(path)
        
# @lc code=end


# @lcpr-div-debug-arg-start
# funName=pathEncryption
# paramTypes= ["string"]
# @lcpr-div-debug-arg-end




#
# @lcpr case=start
# "a.aef.qerf.bb"\n
# @lcpr case=end

#

