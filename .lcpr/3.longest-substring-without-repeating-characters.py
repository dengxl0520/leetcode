#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        start_idx = 0
        res = 0
        for i in range(len(s)):
            if s[i] not in occ:
                occ.add(s[i])
                res = len(occ) if res < len(occ) else res
            else:
                while s[start_idx] != s[i]:
                    occ.remove(s[start_idx])
                    start_idx += 1
                start_idx +=1
                
        return res

# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

