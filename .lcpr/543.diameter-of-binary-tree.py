#
# @lc app=leetcode.cn id=543 lang=python3
# @lcpr version=30204
#
# [543] 二叉树的直径
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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            nonlocal res
            res = max(res, left+right)
            return max(left, right) + 1
        
        dfs(root)
        return res
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

