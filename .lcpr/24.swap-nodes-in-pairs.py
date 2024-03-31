#
# @lc app=leetcode.cn id=24 lang=python3
# @lcpr version=30121
#
# [24] 两两交换链表中的节点
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        left, right = dummy_head, dummy_head.next
        while right and right.next:
            left.next = right.next
            right.next = right.next.next
            left.next.next = right
            left = right
            right = right.next
            
        return dummy_head.next
    
    def swapPairs1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy_head = ListNode(next=head)
        left, right = dummy_head, dummy_head.next
        while right != None and right.next != None:
            left.next = right.next
            right.next = right.next.next
            left.next.next = right
            left = right
            right = right.next
            
        return dummy_head.next
            
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

