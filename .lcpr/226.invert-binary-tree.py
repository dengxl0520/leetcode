# @lcpr-before-debug-begin
from python3problem226 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=226 lang=python3
# @lcpr version=30203
#
# [226] 翻转二叉树
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        def reverse(root):
            if not root: return
            
            root.left, root.right = root.right, root.left
            reverse(root.left)
            reverse(root.right)
        reverse(root)
        return root
        
        
# @lc code=end



#
# @lcpr case=start
# [4,2,7,1,3,6,9]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

