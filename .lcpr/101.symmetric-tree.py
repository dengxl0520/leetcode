#
# @lc app=leetcode.cn id=101 lang=python3
# @lcpr version=30203
#
# [101] 对称二叉树
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        def compare(LN, RN):
            if LN is None and RN is not None: return False      # 左空右不空
            elif LN is not None and RN is None: return False    # 右空左不空
            elif LN is None and RN is None: return True         # 左空右空
            elif LN.val != RN.val: return False                 # 左右不空，判断值：左右值不相等
            
            # 左右值相等，开始递归
            return compare(LN.left, RN.right) and compare(LN.right, RN.left)
            
        return compare(root.left, root.right)
# @lc code=end



#
# @lcpr case=start
# [1,2,2,3,4,4,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,null,3,null,3]\n
# @lcpr case=end

#

