
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    # Runtime: 47 ms, faster than 55.36% of Python3 online submissions for Middle of the Linked List.
    # Memory Usage: 13.8 MB, less than 55.74% of Python3 online submissions for Middle of the Linked List.
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        return slow