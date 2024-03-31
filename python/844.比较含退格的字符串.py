# @before-stub-for-debug-begin
from python3problem844 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def delete(self, string: str) -> str:
        string = list(string)
        fast, slow = 0,0
        while fast < len(string):
            if string[fast] != '#':
                string[slow] = string[fast]
                slow += 1
            elif string[fast] == '#' and slow > 0:
                slow -= 1
            fast += 1
        return str(string[:slow])
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.delete(s) == self.delete(t)
# @lc code=end

