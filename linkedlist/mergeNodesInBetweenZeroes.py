# https://leetcode.com/problems/merge-nodes-in-between-zeros/

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    
    # Submitted By @Jiganesh
    
    # Runtime: 4388 ms, faster than 100.00% of Python online submissions for Merge Nodes in Between Zeros.
    # Memory Usage: 131.5 MB, less than 100.00% of Python online submissions for Merge Nodes in Between Zeros.

    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """


        curr = head
        s = 0

        while curr:
            if curr.val ==0:
                curr.val = s
                s=0
            else:
                s+=curr.val
                curr.val=0
            curr=curr.next


        curr = head
        while curr and curr.next:
            if curr.next.val==0 and curr.next.next:
                curr.next = curr.next.next
            else:
                curr= curr.next

        return head.next

