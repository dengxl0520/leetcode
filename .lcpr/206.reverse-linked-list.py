#
# @lc app=leetcode.cn id=206 lang=python3
# @lcpr version=30121
#
# [206] 反转链表
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        left, right = None, head
        while right != None:
            tmp = right.next
            right.next = left
            left = right
            right = tmp
        return left
    
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        left, mid, right = None, head, head.next
        while right != None:
            mid.next = left
            left = mid
            mid = right
            right = right.next
        mid.next = left
        return mid
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

