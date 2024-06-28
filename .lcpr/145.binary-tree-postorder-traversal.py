# @lcpr-before-debug-begin
from python3problem145 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=145 lang=python3
# @lcpr version=30203
#
# [145] 二叉树的后序遍历
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(root):
            nonlocal res
            if not root: return
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)
        dfs(root)
        return res
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

