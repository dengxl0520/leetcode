#
# @lc app=leetcode.cn id=242 lang=python3
# @lcpr version=30121
#
# [242] 有效的字母异位词
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        d = {}
        for i,j in zip(s,t):
            d[i] = d[i] + 1 if i in d else 1
            d[j] = d[j] - 1 if j in d else -1
                
        for value in d.values():
            if value != 0: return False
        return True
    
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        d = {}
        for i,j in zip(s,t):
            d[i] = d[i] + 1 if i in d else 1
            d[j] = d[j] - 1 if j in d else -1
                
        for i in d.keys():
            if d[i] != 0: return False
        return True


    def isAnagram1(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        for i in t:
            if i in d:
                d[i] -= 1
            else:
                d[i] = -1
                
        for i in d.keys():
            if d[i] != 0:
                return False
        return True
# @lc code=end



#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

#

