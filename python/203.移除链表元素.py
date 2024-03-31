# @before-stub-for-debug-begin
from python3problem203 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        cur_head = dummy_head
        while cur_head.next != None:
            if cur_head.next.val == val:
                cur_head.next = cur_head.next.next
            else:
                cur_head = cur_head.next
        return dummy_head.next
    
    def removeElements1(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        virtual_head = ListNode(next=head)
        curr_head = virtual_head
        while curr_head.next != None:
            if curr_head.next.val == val:
                curr_head.next = curr_head.next.next
            else:
                curr_head = curr_head.next
        return virtual_head.next
# @lc code=end

