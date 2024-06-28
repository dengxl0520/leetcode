#
# @lc app=leetcode.cn id=637 lang=python3
# @lcpr version=30203
#
# [637] 二叉树的层平均值
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
        res2 = []
        for i in res:
            sum = 0.
            for j in i:
                sum += j
            res2.append(sum/len(i))
        return res2

        
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [3,9,20,15,7]\n
# @lcpr case=end

#

