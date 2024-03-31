#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r = 0,num
        while l<=r:
            m = (l+r) //2
            if m*m == num:
                return True
            elif m*m > num:
                r = m-1
            elif m*m < num:
                l = m+1
        return False
# @lc code=end

