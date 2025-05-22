from typing import Optional
# Definition for singly-linked list.
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
            total_sum = carry
            if r1:
                total_sum += r1.val
                r1 = r1.next
            if r2:
                total_sum += r2.val
                r2 = r2.next
            r3.val = total_sum%10
            carry = total_sum // 10
            nxt = ListNode(carry)
            nxt.next = r3
            r3 = nxt
        if carry:
            return r3
        else:
            return r3.next