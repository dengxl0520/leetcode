# @lcpr-before-debug-begin
from python3problem144 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=144 lang=python3
# @lcpr version=30203
#
# [144] 二叉树的前序遍历
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
        self.res.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traversal(root)
        return self.res

    def traversal(self, root, results):
        if root == None: return results
        results.append(root.val)
        self.traversal(root.left, results)
        self.traversal(root.right, results)
        return results
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        results = self.traversal(root, results)
        return results
        
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

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2]\n
# @lcpr case=end

#

