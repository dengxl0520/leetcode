# @lcpr-before-debug-begin
from python3problem394 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30204
#
# [394] 字符串解码
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        num_list = []
        i = 0
        while i < len(s):
            if "0" <= s[i] <= "9":
                j = i+1
                while j <len(s) and "0" <= s[j] <= "9":
                    j += 1
                num_list.append(int(s[i:j]))
                i = j
            elif "a" <= s[i] <= "z":
                res.append(s[i])
                i += 1
            elif s[i] == "[":
                res.append("[")
                i += 1
            elif s[i] == "]":
                tmp = ""
                while res[-1] != "[":
                    tmp = res.pop() + tmp
                res.pop() # remove [
                res.append(tmp * num_list.pop())
                i += 1
        
        return "".join(res)
    
    def decodeString3(self, s: str) -> str:
        res = []
        num_list = []
        i = 0
        while i < len(s):
            if "0" <= s[i] <= "9":
                j = i+1
                while j <len(s) and "0" <= s[j] <= "9":
                    j += 1
                num_list.append(int(s[i:j]))
                i = j
            elif "a" <= s[i] <= "z":
                j = i+1
                while j <len(s) and "a" <= s[j] <= "z":
                    j+=1
                res.append(s[i:j])
                i=j
            elif s[i] == "[":
                res.append("[")
                i+=1
            elif s[i] == "]":
                tmp = ""
                while res[-1] != "[":
                    tmp = res.pop() + tmp
                res.pop() # remove [
                res.append(tmp * num_list.pop())
                i+=1
        
        return "".join(res)
    
    def decodeString2(self, s: str) -> str:
        res = [""]
        num_list = []
        depth = 0
        i = 0
        while i < len(s):
            if "0" <= s[i] <= "9":
                j = i+1
                while j <len(s) and "0" <= s[j] <= "9":
                    j += 1
                num_list.append(int(s[i:j]))
                i = j
            elif "a" <= s[i] <= "z":
                j = i+1
                while j <len(s) and "a" <= s[j] <= "z":
                    j+=1
                res.append(s[i:j])
                i=j
            elif s[i] == "[":
                depth += 1
                i+=1
            elif s[i] == "]":
                if depth > 1:
                    tmp = res.pop() * num_list.pop()
                    res[-1] += tmp
                else:
                    res.append(res.pop() * num_list.pop())
                depth -= 1
                i+=1
        
        return "".join(res)
    
    def decodeString1(self, s: str) -> str:
        res = []
        num_list = []
        s_list = []
        is_repeat = False
        for si in s:
            if "a" <= si <= "z":
                if is_repeat:
                    s_list.append(si)
                else:
                    res.append(si)
            elif "0" <= si <= "9":
                num_list.append(si)
            elif si == "[":
                is_repeat = True
            elif si == "]":
                is_repeat = False
                num = int("".join(num_list))
                ss = "".join(s_list)
                res.append(ss*num)
                num_list = []
                s_list = []

        return "".join(res)
            
# @lc code=end



#
# @lcpr case=start
# "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"\n
# @lcpr case=end
    
# @lcpr case=start
# "3[a]2[bc]"\n
# @lcpr case=end

# @lcpr case=start
# "3[a2[c]]"\n
# @lcpr case=end

# @lcpr case=start
# "2[abc]3[cd]ef"\n
# @lcpr case=end

# @lcpr case=start
# "abc3[cd]xyz"\n
# @lcpr case=end

#

