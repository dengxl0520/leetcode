# @lcpr-before-debug-begin
from python3problem116 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=116 lang=python3
# @lcpr version=30203
#
# [116] 填充每个节点的下一个右侧节点指针
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        from collections import deque
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if i != 0:
                    pre.next = cur
                pre = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        # print(root)
        return root
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

