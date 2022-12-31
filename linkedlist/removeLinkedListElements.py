# https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:


        dummyhead = ListNode(-1, head)
        previous = None
        current = dummyhead

        while current :
            previous = current
            current = current.next

            while current and  current.val == val:
                previous.next = current.next
                current = current.next

            
        return dummyhead.next