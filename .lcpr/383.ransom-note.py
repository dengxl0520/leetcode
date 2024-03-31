# @lcpr-before-debug-begin
from python3problem383 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=383 lang=python3
# @lcpr version=30121
#
# [383] 赎金信
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt1 = Counter(ransomNote)
        cnt2 = Counter(magazine)
        for s in cnt1.keys():
            if s not in cnt2 or cnt1[s] > cnt2[s]:
                return False
            
        return True
        
# @lc code=end



#
# @lcpr case=start
# "a"\n"b"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"ab"\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n"aab"\n
# @lcpr case=end

#

