#
# @lc app=leetcode.cn id=429 lang=python3
# @lcpr version=30203
#
# [429] N 叉树的层序遍历
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children # 应该是一个list的节点

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res = []
        from collections import deque
        queue = deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                for ch in cur.children:
                    queue.append(ch)
            res.append(level)
        return res
                
        
# @lc code=end



#
# @lcpr case=start
# [1,null,3,2,4,null,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]\n
# @lcpr case=end

#

