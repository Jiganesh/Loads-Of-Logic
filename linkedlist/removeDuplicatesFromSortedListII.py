# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    

    # Runtime: 41 ms, faster than 46.10% of Python online submissions for Remove Duplicates from Sorted List II.
    # Memory Usage: 13.2 MB, less than 97.59% of Python online submissions for Remove Duplicates from Sorted List II.
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        dummynode = ListNode(-1);
        dummyNodePointer = dummynode
        # create a dummy Node
        
        currentNode = head
        unique=  head
        # keep unique and currentNode on head
        
        count=0
        #create a count variable to check how many times number is repeating
        
        while currentNode:
            
            # Below block of code check how many times the number is occuring
            while currentNode and currentNode.val == unique.val:
                count+=1
                currentNode= currentNode.next
        
            # If the number is occuring only once the add the number node to dummyPointer
            if count==1:
                dummyNodePointer.next =unique
                dummyNodePointer=dummyNodePointer.next
                dummyNodePointer.next = None
            
            # move the next number
            unique = currentNode
            count =0

        return dummynode.next
    
    
    # Runtime: 34 ms, faster than 69.50% of Python online submissions for Remove Duplicates from Sorted List II.
    # Memory Usage: 13.6 MB, less than 14.45% of Python online submissions for Remove Duplicates from Sorted List II.
    
    
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        dummynode = ListNode(-1);
        dummyNodePointer = dummynode
        
        
        current = head
        
        
        while current:
            
            
            if (current.next and current.val ==current.next.val):
                while (current.next and current.val == current.next.val):
                    current.next = current.next.next
                current = current.next
                
            else:
                
                dummyNodePointer.next= current
                current = current.next
                dummyNodePointer = dummyNodePointer.next
                dummyNodePointer.next= None
                
                
        return dummynode.next
            
            
            
            
            