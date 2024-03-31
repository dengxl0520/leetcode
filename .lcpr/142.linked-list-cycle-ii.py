# @lcpr-before-debug-begin
from python3problem142 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=142 lang=python3
# @lcpr version=30121
#
# [142] 环形链表 II
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        left, right = head, head
        while True:
            left = left.next
            if right.next and right.next.next:
                right = right.next.next
            else:
                return None
            if left == right: break
            
        left = head
        while left != right:
            left = left.next
            right = right.next
        return left
# @lc code=end



#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#

