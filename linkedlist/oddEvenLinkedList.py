# https://leetcode.com/problems/odd-even-linked-list/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        oddhead = oddnode = ListNode(-1)
        evenhead = evennode = ListNode(-1)

        current = head

        while current :
            oddnode.next = current
            if current :
                current = current.next
            if oddnode:
                oddnode = oddnode.next

            evennode.next = current
            if current :
                current = current.next
            if evennode:
                evennode = evennode.next

        
        oddnode.next = evenhead.next

        return oddhead.next