# @lcpr-before-debug-begin
from python3problem350 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=350 lang=python3
# @lcpr version=30121
#
# [350] 两个数组的交集 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)
        ans = []
        for key in cnt1.keys():
            if key in cnt2:
                num = min(cnt1[key], cnt2[key])
                ans.extend([key]*num)
                
        print(ans)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n[2,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,9,5]\n[9,4,9,8,4]\n
# @lcpr case=end

#

