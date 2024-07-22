#
# @lc app=leetcode.cn id=338 lang=python3
# @lcpr version=30204
#
# [338] 比特位计数
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
            i.bit_count()在python 3.10版本被加入
            等价于 bin(i).count("1")
        '''
        res = []
        for i in range(n+1):
            res.append(i.bit_count())
        return res
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

#

