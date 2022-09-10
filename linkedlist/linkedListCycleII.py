# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # Runtime: 51 ms, faster than 95.94% of Python3 online submissions for Linked List Cycle II.
    # Memory Usage: 17.9 MB, less than 10.00% of Python3 online submissions for Linked List Cycle II.
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        lookup = set()
        
        while head:
            if head in lookup:
                return head
            
            lookup.add(head)
            head = head.next
    
    # Optimized Approach
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        
        while fast and fast.next:
            slow , fast = slow.next, fast.next.next
            
            if slow == fast:
                tracker = head
                while slow != tracker:
                    slow = slow.next
                    tracker = tracker.next
                    
                return slow
'''
Math Proof for optimized Approach

    An easier formula to explain to the interviewer:
    Distance traveled by slow when they meet: L1+L2
    Distance traveled by fast when they meet: L1+L2+x+L2, where x is the remaining length of the cycle (meeting point to start of the cycle).

    2(L1+L2) = L1+L2+x+L2
    2L1 + 2L2 = L1+2L2+x
    => x = L1

    so we need to move L1 steps from the current meeting point to reach the entry point of the cycle.
    
'''