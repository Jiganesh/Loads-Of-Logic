# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    # TC : O(N)
    # SC : O(N)
    
    # As elements can be duplicate so We need unique id of the node
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        array=[]
        curr = head

        while curr:
            if id(curr) in array :
                return True
            array.append(id(curr))
            curr = curr.next
        return False

    # Submitted by Jiganesh

    # TC: O(N)
    # SC: O(1)

    # Runtime: 47 ms, faster than 84.80% of Python online submissions for Linked List Cycle.
    # Memory Usage: 20.4 MB, less than 84.36% of Python online submissions for Linked List Cycle.

    # Floyd’s Cycle-Finding Algorithm

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow , fast = head, head

        while slow  and fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast :
                return True

        return False
