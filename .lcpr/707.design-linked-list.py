#
# @lc app=leetcode.cn id=707 lang=python3
# @lcpr version=30121
#
# [707] 设计链表
#


# @lcpr-template-start
from typing import *
# @lcpr-template-end
# @lc code=start

class LinkNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy_head = LinkNode()

    def get(self, index: int) -> int:
        cur = self.dummy_head
        
        for i in range(index):
            if cur.next == None:
                return -1
            cur = cur.next
            
        if cur.next == None:
            return -1
        return cur.next.val
                
    def addAtHead(self, val: int) -> None:
        new_node = LinkNode(val, self.dummy_head.next)
        self.dummy_head.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = LinkNode(val, None)
        cur = self.dummy_head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.dummy_head
        for i in range(index):
            if cur.next == None:
                return
            else:
               cur = cur.next
        new_node = LinkNode(val, cur.next)
        cur.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        cur = self.dummy_head
        for i in range(index):
            if cur.next == None:
                return
            else:
                cur = cur.next
        if cur.next == None:
            return 
        cur.next = cur.next.next

if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1, 2)
    obj.get(1)
    obj.deleteAtIndex(1)
    obj.get(1)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end



