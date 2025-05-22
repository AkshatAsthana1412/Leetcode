from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# THE TRICKY PART IN THIS PROBLEM WAS THE NESTED LINKED LIST, traverse it recursively.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # total_sum = 0
        carry = 0
        dummy = ListNode()
        l3 = dummy
        while l1 or l2:
            total_sum = 0
            if l1:
                total_sum += l1.val
                l1 = l1.next
            if l2:
                total_sum += l2.val
                l2 = l2.next
            total_sum += carry
            carry = total_sum // 10
            l3.next = ListNode(total_sum % 10)
            l3 = l3.next
        if carry:
            l3.next = ListNode(carry)
        return dummy.next

            
            

    