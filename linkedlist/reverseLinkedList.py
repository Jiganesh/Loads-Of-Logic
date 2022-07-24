# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # Runtime: 52 ms, faster than 59.50% of Python3 online submissions for Reverse Linked List.
    # Memory Usage: 15.4 MB, less than 55.79% of Python3 online submissions for Reverse Linked List.
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        currentNode = head
        previousNode = None
        
        while currentNode:
            
            nextNode = currentNode.next
            currentNode.next = previousNode
            
            previousNode = currentNode
            currentNode = nextNode
            
        head = previousNode
        
        return head