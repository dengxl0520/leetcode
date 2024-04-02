# @lcpr-before-debug-begin
from python3problem541 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=541 lang=python3
# @lcpr version=30121
#
# [541] 反转字符串 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        ans = list(s) # transfer to list first
        for i in range(0,n,2*k):
            ans[i:i+k] = ans[i:i+k][::-1] # reverse k char
        return "".join(ans)
    
    def reverseStr2(self, s: str, k: int) -> str:
        n = len(s)
        ans = list(s) # transfer to list first
        start = 0
        while n>0:
            if n -2*k >= 0:
                ans[start:start+k] = ans[start:start+k][::-1]
                n -= 2*k
                start += 2*k
            elif n-k >=0:
                ans[start:start+k] = ans[start:start+k][::-1]
                n=0
            else:
                ans[start:] = ans[start:][::-1]
                n=0

        print("".join(ans))
        return "".join(ans)
    
    def reverseStr1(self, s: str, k: int) -> str:
        n = len(s)
        ans = []
        start = 0
        while n>0:
            if n -2*k >= 0:
                ans.extend(list(s[start:start+k])[::-1])
                ans.extend(list(s[start+k:start+2*k]))
                n -= 2*k
                start += 2*k
            elif n-k >=0:
                ans.extend(list(s[start:start+k])[::-1])
                ans.extend(list(s[start+k:]))
                n=0
            else:
                ans.extend(list(s[start:][::-1]))
                n=0

        print("".join(ans))
        return "".join(ans)

            
# @lc code=end



#
# @lcpr case=start
# "a"\n2\n
# @lcpr case=end
    
# @lcpr case=start
# "abcdefg"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n2\n
# @lcpr case=end

#

