#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30204
#
# [234] 回文链表
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse_list(self, head):
            previous = None
            current = head
            while current is not None:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous

        slow, fast = head, head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # 从slow开始反转
        # 感觉反转前面比反转后面更好
        # 反转后面
        second_half_start = reverse_list(slow.next)

        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        slow.next = reverse_list(second_half_start)
        return result


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        from collections import deque
        queue = deque([])
        cur = head
        while cur != None:
            queue.append(cur.val)
            cur = cur.next
        
        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False
        
        return True
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

