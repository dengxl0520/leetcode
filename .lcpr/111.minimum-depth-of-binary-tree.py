#
# @lc app=leetcode.cn id=111 lang=python3
# @lcpr version=30203
#
# [111] 二叉树的最小深度
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        from collections import deque
        queue = deque([root])
        res = 0
        while queue:
            res += 1
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left: 
                    queue.append(cur.left)
                if cur.right: 
                    queue.append(cur.right)
                if not cur.left and not cur.right:
                    return res
        return res

# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,null,3,null,4,null,5,null,6]\n
# @lcpr case=end

#

