# @lcpr-before-debug-begin
from python3problem160 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30121
#
# [160] 相交链表
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        
        return A
    
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        A, B = headA, headB
        while A.next != None and B.next != None:
            A = A.next
            B = B.next

        # 此时A或B其中比较短的到了尾部
        if A.next == None:
            A = headB
        else:
            A = A.next
        if B.next == None:
            B = headA
        else:
            B = B.next

        while A != B and (A.next != None and B.next != None):
            if A.next == None:
                A = headB
            else:
                A = A.next
            if B.next == None:
                B = headA
            else:
                B = B.next
        
        return A if A == B else None
        
        
# @lc code=end



#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#

