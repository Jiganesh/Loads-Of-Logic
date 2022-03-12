# https://leetcode.com/problems/copy-list-with-random-pointer/
#  Solution = https://www.youtube.com/watch?v=5Y2EiZST97Y

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    
    # TC : O(N)
    # SC : O(N)
    
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        oldToCopy = {None : None}
        
        curr = head
        while curr:
            copy = Node (curr.val)
            oldToCopy [curr] = copy
            curr = curr.next
        
        curr = head 
        while curr :
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            
            curr = curr.next
            
        return oldToCopy[head]