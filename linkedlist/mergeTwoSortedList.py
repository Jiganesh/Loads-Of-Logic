# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.\
    
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    
    
    # Submitted by Jiganesh
    
    # TC: O(N)
    # SC: O(N)  Recursion Stack Space
    
    # Runtime: 23 ms, faster than 90.58% of Python online submissions for Merge Two Sorted Lists.
    # Memory Usage: 13.4 MB, less than 84.87% of Python online submissions for Merge Two Sorted Lists.
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = None
        if list1==None : return list2
        if list2==None : return list1
        
        
        if list1.val <= list2.val:
            node = list1
            node.next= self.mergeTwoLists(list1.next, list2)
        else:
            node = list2
            node.next =self.mergeTwoLists(list1, list2.next)
            
        return node
    
    
    # TC: O(N)
    # SC : O(1)
    
    # Runtime: 20 ms, faster than 96.61% of Python online submissions for Merge Two Sorted Lists.
    # Memory Usage: 13.5 MB, less than 61.57% of Python online submissions for Merge Two Sorted Lists.
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        pointerOnNode1 = list1
        pointerOnNode2 = list2
        
        dummyNode =ListNode();
        dummyPointer  = dummyNode
        
        while pointerOnNode1 and pointerOnNode2:
            if pointerOnNode1.val < pointerOnNode2.val:
                dummyPointer.next = pointerOnNode1
                dummyPointer = dummyPointer.next
                pointerOnNode1 = pointerOnNode1.next
            else:
                dummyPointer.next = pointerOnNode2
                dummyPointer = dummyPointer.next
                pointerOnNode2 = pointerOnNode2.next
                
        if pointerOnNode1:
            dummyPointer.next = pointerOnNode1
        if pointerOnNode2:
            dummyPointer.next = pointerOnNode2
        
        return dummyNode.next;
                