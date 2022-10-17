# https://leetcode.com/problems/reorder-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    # TC : O(N)
    # SC : O(1)
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Handling Edge Case
        if head.next == None:
            return head

        pointer1 = head
        slow , fast = head , head
        
        # Step 1
        # Finding middle 
        
        while fast and fast.next :
            middle = slow
            slow, fast = slow.next, fast.next.next

        middle.next = None
        
        # Step 2
        # Reversing after Middle Part

        prev = None
        current = slow
        while current:
            nxt = current.next
            current.next = prev

            
            prev = current
            current = nxt

        pointer2 = prev

        # Step 3
        # Building LinkedList

        dummyNode = ListNode(-1)

        while pointer1 and pointer2:
            if pointer1 :
                dummyNode.next = pointer1
                pointer1 = pointer1.next
                dummyNode = dummyNode.next
            if pointer2:
                dummyNode.next = pointer2
                pointer2 = pointer2.next
                dummyNode = dummyNode.next
        return dummyNode
