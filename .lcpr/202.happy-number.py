# @lcpr-before-debug-begin
from python3problem202 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=202 lang=python3
# @lcpr version=30121
#
# [202] 快乐数
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        s1 = set()
        while True:
            s = str(n)
            n = 0
            for i in s:
                n += int(i)**2
            if n in s1:
                return False
            else:
                s1.add(n)
            if n == 1: return True
            
    def isHappy1(self, n: int) -> bool:
        s1 = set()
        while True:
            s = str(n)
            n = 0
            for i in s:
                n += int(i)**2
            if n in s1:
                return False
            else:
                s1.add(n)
            if n == 1: return True
        
# @lc code=end



#
# @lcpr case=start
# 19\n
# @lcpr case=end

# @lcpr case=start
# 2\n
# @lcpr case=end

#

