# https://leetcode.com/problems/palindrome-linked-list/


from typing import Optional
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Runtime: 1118 ms, faster than 61.63% of Python3 online submissions for Palindrome Linked List.
    # Memory Usage: 39.1 MB, less than 68.93% of Python3 online submissions for Palindrome Linked List.
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        # Step 1
        # Find middle node 
        
        slow = fast = first_head = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2
        # Reverse the second half
        second_head = slow
        prev = None
        
        while second_head:
            nxt = second_head.next
            second_head.next = prev
            
            prev = second_head
            second_head = nxt
        
        second_head = prev
    
       # Step 3
       # Compare both string values by traversing
        while first_head and second_head and first_head != second_head:
            if first_head.val != second_head.val:
                return False
            
            first_head = first_head.next
            second_head = second_head.next
        
        return True
