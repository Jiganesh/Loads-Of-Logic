




# MONOTONIC STACK + LINKEDLIST

from typing import ListNode,Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = []
        
        while head:
            n.append(head.val)
            head = head.next
            
        stack = []
        for i in n:
            while stack and stack[-1]< i:
                stack.pop()
            stack.append(i)
            
        dummyNode = ListNode(-1)
        current = dummyNode
        
        for num in stack:

            current.next = ListNode(num)
            current = current.next
            
        return dummyNode.next
        