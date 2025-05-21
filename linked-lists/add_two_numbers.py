from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# THE TRICKY PART IN THIS PROBLEM WAS THE NESTED LINKED LIST, traverse it recursively.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                
        def create_num(node):
            if node is None:
                return 0
            return node.val + 10 * create_num(node.next)
        
        def create_list(num):
            if num == 0:
                return None
            d = num % 10
            node = ListNode(d)
            node.next = create_list(num//10)
            return node

        n1 = create_num(l1)
        n2 = create_num(l2)
        n3 = n1 + n2
        if n3 == 0:
            return ListNode(0)
        l3 = create_list(n3)
        
        return l3
            

    