#
# @lc app=leetcode.cn id=141 lang=python3
# @lcpr version=30204
#
# [141] 环形链表
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return False
        return True


    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        for i in range(10001):
            if head == None:
                return False
            else:
                head = head.next
            
        return True
    

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast != None and slow != None:
            slow = slow.next
            fast = fast.next
            if fast == None or slow == None:
                return False
            else:
                fast = fast.next
            if fast == slow:
                return True
        return False
        
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

