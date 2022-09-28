# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
    # Runtime: 24 ms, faster than 69.92% of Python online submissions for Remove Nth Node From End of List.
    # Memory Usage: 13.4 MB, less than 68.36% of Python online submissions for Remove Nth Node From End of List.
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = 0
        
        dummyNode = ListNode(0)
        current = head
        dummyNode.next = current
        
        while current:
            current = current.next
            l+=1
            
        nstart = l-n
        previous = dummyNode
        current = head
        
        while nstart and current:
            previous = current
            current = current.next
            nstart-=1
            
        previous.next = current.next
        current.next = None
        
        return dummyNode.next   
    
    # OPTIMIZED SOLUTION SINGLE PASS
    def removeNthFromEnd(self, head, n: int):
        dummyNode = ListNode(-1)
        dummyNode.next = head
        head = dummyNode

        pointer_nth = current = head
        length = 0
        
        while current:
            if length > n:
                pointer_nth = pointer_nth.next
            length+=1
            current = current.next
            
        pointer_nth.next = pointer_nth.next.next if pointer_nth.next else None
        return dummyNode.next
        
    
    