# @lcpr-before-debug-begin
from python3problem56 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30204
#
# [56] 合并区间
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        while len(intervals) > 0:
            # find min
            minleft_idx = 0
            for i in range(1, len(intervals)):
                if intervals[i][0] < intervals[minleft_idx][0]:
                    minleft_idx = i
            
            if len(res) != 0 and res[-1][1] >= intervals[minleft_idx][0]:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[minleft_idx][1])]
            else:
                res.append(intervals[minleft_idx])
            intervals.remove(intervals[minleft_idx])

        return res
# @lc code=end



#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

#

