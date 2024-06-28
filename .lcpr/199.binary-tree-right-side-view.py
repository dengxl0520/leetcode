#
# @lc app=leetcode.cn id=199 lang=python3
# @lcpr version=30203
#
# [199] 二叉树的右视图
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return []
        
        from collections import deque
        queue = deque([root])
        
        while queue:
            l = len(queue)
            for i in range(l):
                cur = queue.popleft()
                if i == l-1: # end
                    res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
                    
                
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5,null,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,3]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

