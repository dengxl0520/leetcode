#
# @lc app=leetcode.cn id=455 lang=python3
# @lcpr version=30204
#
# [455] 分发饼干
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_p, s_p = 0,0
        res = 0
        while g_p < len(g) and s_p < len(s):
            if g[g_p] <= s[s_p]:
                res += 1
                g_p += 1
                s_p += 1
            else:
                s_p += 1
        return res
    
    def findContentChildren1(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        index = 0
        for i in s:
            if g[index] <= i:
                res += 1
                index += 1
        return res


# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n[1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n[1,2,3]\n
# @lcpr case=end

#

