#
# @lc app=leetcode.cn id=515 lang=python3
# @lcpr version=30203
#
# [515] 在每个树行中找最大值
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        from collections import deque
        queue = deque([root])
        res = []
        while queue:
            max_val = float('-inf')
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.val > max_val:
                    max_val = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(max_val)
        return res
        
# @lc code=end



#
# @lcpr case=start
# [1,3,2,5,3,null,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

