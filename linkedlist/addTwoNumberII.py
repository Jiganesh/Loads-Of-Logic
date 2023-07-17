# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def reverse_ll(linkedlist):

            curr = linkedlist
            prev = None

            while curr:
                nextnode = curr.next
                curr.next = prev

                prev = curr
                curr = nextnode
            
            return prev

        l1 = reverse_ll(l1)
        l2 = reverse_ll(l2)

        carry = 0
        result = ListNode(-1)
        head = result

        while l1 or l2  or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            if l1: l1 = l1.next
            if l2: l2 = l2.next

            digit = (v1 + v2 + carry)%10
            carry = (v1 + v2 + carry)//10

            result.next = ListNode(digit)
            result = result.next

        return reverse_ll(head.next)
