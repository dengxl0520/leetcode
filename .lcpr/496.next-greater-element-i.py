# @lcpr-before-debug-begin
from python3problem496 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=496 lang=python3
# @lcpr version=30204
#
# [496] 下一个更大元素 I
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
            lcpr的test case 有问题
        '''
        res = dict()
        stack = []
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[stack[-1]] < nums2[i]:
                res[nums2[stack[-1]]] = nums2[i]
                stack.pop()
            stack.append(i)
        
        res2 = []
        for i in nums1:
            if i in res:
                res2.append(res[i])
            else:
                res2.append(-1)
        return res2
    
# @lc code=end



#
# @lcpr case=start
# [4,1,2]\n[1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n[1,2,3,4]\n
# @lcpr case=end

#

