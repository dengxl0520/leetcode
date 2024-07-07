# @lcpr-before-debug-begin
from python3problem2 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30204
#
# [2] 两数相加
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        left, right = l1, l2
        head = ListNode() # dummy_head
        res = head
        cur = 0
        while left != None or right != None:
            if left == None:
                cur += right.val
                right = right.next
            elif right == None:
                cur += left.val
                left = left.next
            else:
                cur += left.val + right.val
                left = left.next
                right = right.next
            
            if cur >= 10:
                res.next = ListNode(val=cur-10)
                cur = 1 
            else:
                res.next = ListNode(val=cur)
                cur = 0
            res = res.next
            
        if cur != 0:
            res.next = ListNode(val=cur)
        
        return head.next
                
# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

