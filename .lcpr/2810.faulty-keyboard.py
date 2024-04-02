# @lcpr-before-debug-begin
from python3problem2810 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=2810 lang=python3
# @lcpr version=30121
#
# [2810] 故障键盘
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def finalString(self, s: str) -> str:
        n = len(s)
        ans = []
        for i in range(n):
            if s[i] == 'i':
                ans = ans[::-1] # list reverse
            else:
                ans.append(s[i])

        print("".join(ans))
        return "".join(ans) # list to str

    def reverse(self, s):
        n = len(s)
        ans = list(s)
        for i in range(n//2):
            ans[i], ans[n-i-1] = ans[n-i-1], ans[i]
        return ans
    
    # def reverse(self, s, begin, end):
    #     n = (end-begin+1)
    #     ans = list(s[begin:end+1])
    #     for i in range(begin, n//2):
    #         ans[i], ans[n-i-1] = ans[n-i-1], ans[i]
    #     return ans

    def finalString1(self, s: str) -> str:
        n = len(s)
        ans = []
        for i in range(n):
            if s[i] == 'i':
                ans = self.reverse(ans)
            else:
                ans.append(s[i])

        print("".join(ans))
        return "".join(ans)
        

# @lc code=end


# @lcpr-div-debug-arg-start
# funName=finalString
# paramTypes= ["string"]
# @lcpr-div-debug-arg-end




#
# @lcpr case=start
# "string"\n
# @lcpr case=end

# @lcpr case=start
# "poiinter"\n
# @lcpr case=end

#

