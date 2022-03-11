# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        
        current = head
        length = 0
        while current :
            length+=1
            breakhere =current
            current= current.next
        
        if k ==0 or length<=1 : return head
        
        k= k% length
        breakAt = length-k-1
        
        
        current = head
        while current.next:
            
            if breakAt==0:
                breakhere = current
            
            breakAt-=1
            current = current.next
            
        current.next = head
        head = breakhere.next
        breakhere.next = None
        
        return head;
    
    
    
    
"""

linkedlist = 1->2->3->4->5
rotate = 2

Step 1 : traverse through array and to avoid edge cases keep pointer breakHere on last Node
Step 2 : find the length and calculate the Break Point

    In above example the length of linked list is 5 and rotate is 2 hence the node to be break is ahead of 3
    breakAt = length -k-1
    
Step 3 : Go to that node and keep a pointer breakHere on that Node and traverse till last node
Step 4 : Attach last node to head by doing  "current.next = head"
Step 5 : Now make the new head from the point where we are going to break it
         "head = breakHere.next" Do this step first so you will not lose reference
Step 6 : Break the Node

head breakHere                                           breakHere head
|     |                                                        |   |

1->2->3->4->5 --- current        will look like         1->2->->3  4->5
                                                        |_____________|

    
    
"""