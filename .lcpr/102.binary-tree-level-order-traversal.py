# @lcpr-before-debug-begin
from python3problem102 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=102 lang=python3
# @lcpr version=30203
#
# [102] 二叉树的层序遍历
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)): # len()在第一次运行时已经确定，后续的pop不会变化
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            res.append(level)
        # print(res)
        return res
                
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

