# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    # Submitted by Jiganesh
    
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        
        n1= k-1
        pointer1= head
        current = head 
        l=0
        
        while n1:
            pointer1= pointer1.next
            n1-=1
            
        while current  :
            l+=1
            current = current.next
            
        pointer2 = head
        n2 = l-k
        
        while n2 :
            pointer2= pointer2.next
            n2-=1
            
        pointer1.val, pointer2.val = pointer2.val, pointer1.val

        return head;    
    
    
    # Runtime: 1338 ms, faster than 96.46% of Python online submissions for Swapping Nodes in a Linked List.
    # Memory Usage: 90.7 MB, less than 83.92% of Python online submissions for Swapping Nodes in a Linked List.
    
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        pointer1 = head 
        
        n = k-1 
        
        while n :
            pointer1 = pointer1.next 
            n -=1
            
            
        first = pointer1
        second = head
        
        while pointer1.next:
            pointer1 = pointer1.next
            second  = second.next
            
        first.val , second.val = second.val ,first.val
        
        return head;        
        