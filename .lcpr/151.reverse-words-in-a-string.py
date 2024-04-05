# @lcpr-before-debug-begin
from python3problem151 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=151 lang=python3
# @lcpr version=30121
#
# [151] 反转字符串中的单词
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        i = j = len(s) -1
        while i>=0:
            while j>=0 and s[j] == " ": j -= 1
            i = j
            while i>=0 and s[i] != " ": i -= 1
            if i != j:
                ans.append(s[i+1:j+1])
            j = i
        return " ".join(ans)
    
    def reverseWords2(self, s: str) -> str:
        s = s.strip()                            # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1])          # 添加单词
            while i >= 0 and s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i                                # j 指向下个单词的尾字符
        return ' '.join(res)                     # 拼接并返回

    def reverseWords1(self, s: str) -> str:
        ans = s.strip().split() # split() and split(" ")
        return " ".join(ans[::-1])
# @lc code=end



#
# @lcpr case=start
# "the sky is blue"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

# @lcpr case=start
# "a good   example"\n
# @lcpr case=end

# @lcpr case=start
# "  hello world  "\n
# @lcpr case=end

#

