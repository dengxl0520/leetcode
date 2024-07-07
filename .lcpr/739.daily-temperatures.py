# @lcpr-before-debug-begin
from python3problem739 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30204
#
# [739] 每日温度
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
# @lc code=end



#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#

