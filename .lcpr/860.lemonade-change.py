#
# @lc app=leetcode.cn id=860 lang=python3
# @lcpr version=30204
#
# [860] 柠檬水找零
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {
            5:0,
            10:0,
        }
        for bill in bills:
            if bill == 5:
                d[5] += 1
            elif bill == 10:
                d[5] -= 1
                d[10] += 1
            elif bill == 20:
                if d[10] == 0: # 没有十块钱
                    d[5] -= 3
                else:
                    d[5] -= 1
                    d[10] -= 1
            if d[5] < 0 or d[10] < 0:
                return False
        return True
                    
# @lc code=end



#
# @lcpr case=start
# [5,5,5,10,20]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,10,10,20]\n
# @lcpr case=end

#

