# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(node):
            if node is None:
                return None
            cur = None
            temp = None
            while node:
                temp = node.next
                node.next = cur
                cur = node
                node = temp
            return cur
        
        r1, r2 = reverse_list(l1), reverse_list(l2)
        carry = 0
        dummy = ListNode()
        r3 = dummy
        while r1 or r2:
            total_sum = 0
            if r1:
                total_sum += r1.val
                r1 = r1.next
            if r2:
                total_sum += r2.val
                r2 = r2.next
            total_sum += carry
            carry = total_sum // 10
            r3.next = ListNode(total_sum%10)
            r3 = r3.next
        if carry:
            r3.next = ListNode(1)
        return reverse_list(dummy.next)