# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    
    
    # Runtime: 56 ms, faster than 92.91% of Python online submissions for Add Two Numbers.
    # Memory Usage: 13.6 MB, less than 18.13% of Python online submissions for Add Two Numbers.
    
    # TC: O(N)
    # SC : O(N)
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        carry = 0
        dummyNode = ListNode(-1)
        sentinel = dummyNode
        
        while l1 or l2 or carry:
            
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            
            if l1 : l1 = l1.next
            if l2 : l2 = l2.next
            
            newNumber = (digit1+digit2+carry)%10
            
            dummyNode.next = ListNode(newNumber)
            dummyNode = dummyNode.next
            
            carry=(digit1+digit2+carry)//10
            
        return sentinel.next
            
            
        