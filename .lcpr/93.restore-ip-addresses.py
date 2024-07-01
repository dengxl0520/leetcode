# @lcpr-before-debug-begin
from python3problem93 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=93 lang=python3
# @lcpr version=30204
#
# [93] 复原 IP 地址
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        s = list(s)
        def backtracking(start_idx, k, path, res):
            if k == 4 and start_idx == len(s):
                res.append(".".join(path))
                return
            if k == 4:
                return 
            
            for i in range(start_idx, len(s)):
                if i != start_idx and s[start_idx] == "0": # 有前导零
                    break
                num = "".join(s[start_idx:i+1])
                if int(num) > 255:
                    break
                path.append(num)
                backtracking(i+1, k+1, path, res)
                path.pop()

        res = []
        backtracking(0, 0, [], res)
        return res

# @lc code=end



#
# @lcpr case=start
# "25525511135"\n
# @lcpr case=end

# @lcpr case=start
# "0000"\n
# @lcpr case=end

# @lcpr case=start
# "101023"\n
# @lcpr case=end

#

