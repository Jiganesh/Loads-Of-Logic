# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    dummy = ListNode(-1)
    prev, current = dummy, head;
    dummy.next = head
    
    while current and current.next: 
        prev.next = current.next
        current.next= current.next.next
        prev.next.next = current
        
        current = current.next
        prev = prev.next.next
    
    return dummy.next    
    
def printListNode(head):
    while head:
        print(str(head.val) +" ----->", end=" ")
        head= head.next
    print()
    
list = ListNode(1)
list.next = ListNode(2)
list.next.next = ListNode(3)
list.next.next.next = ListNode(4)

printListNode(list)
list = swapPairs(list)
printListNode(list)