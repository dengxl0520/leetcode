#
# @lc app=leetcode.cn id=344 lang=python3
# @lcpr version=30121
#
# [344] 反转字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            s[i], s[n-1-i] = s[n-1-i], s[i]
            # s[i], s[-i-1] = s[-i-1], s[i]
            
    def reverseString1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n // 2):
            tmp = s[i]
            s[i] = s[n-1-i]
            s[n-1-i] = tmp
# @lc code=end



#
# @lcpr case=start
# ["h","e","l","l","o"]\n
# @lcpr case=end

# @lcpr case=start
# ["H","a","n","n","a","h"]\n
# @lcpr case=end

#

