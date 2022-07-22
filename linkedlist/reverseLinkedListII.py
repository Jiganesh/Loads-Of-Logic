# https://leetcode.com/problems/reverse-linked-list-ii/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    
    # Runtime: 41 ms, faster than 71.75% of Python3 online submissions for Reverse Linked List II.
    # Memory Usage: 14 MB, less than 51.75% of Python3 online submissions for Reverse Linked List II.
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummyNode = ListNode(-1)
        dummyNode.next=head
        
        leftnode, rightnode = dummyNode, dummyNode
        prevleft, prevright = None,None
        
        right+=1
        
        while left or right:

            if left :
                prevleft = leftnode
                leftnode = leftnode.next
                left-=1
            if right : 
                prevright = rightnode
                rightnode = rightnode.next
                
                right-=1
            
        if prevleft :prevleft.next = None
        if prevright :prevright.next = None
        
        def reverse(head):

            current_node = head
            previous_node = None

            tail = head

            while current_node:
                next_node = current_node.next
                current_node.next = previous_node

                previous_node = current_node
                current_node = next_node

            head = previous_node
            return head,tail
 
        head, tail = reverse(leftnode)
        prevleft.next = head
        tail.next = rightnode
        
        return dummyNode.next
        
            
        