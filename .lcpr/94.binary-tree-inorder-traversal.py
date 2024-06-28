# @lcpr-before-debug-begin
from python3problem94 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=94 lang=python3
# @lcpr version=30203
#
# [94] 二叉树的中序遍历
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
    def dfs(self, root):
        if not root: return
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root)
        return self.res
# @lc code=end



#
# @lcpr case=start
# [1,null,2,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

