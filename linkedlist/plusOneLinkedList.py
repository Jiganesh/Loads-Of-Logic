# https://leetcode.com/problems/plus-one-linked-list/


# Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# 81 ms time cost.
# 6.00 MB memory cost.
# Your submission beats 84.60 % Submissions.
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def __reverse(head: ListNode) -> ListNode:
            if head is None or head.next is None:
                return head
            new_head = __reverse(head.next)
            head.next.next = head
            head.next = None
            return new_head

        sum, carry = 0, 1
        new_head = __reverse(head)
        current_node, prev_node = new_head, new_head
        while current_node is not None:
            sum = carry + current_node.val
            current_node.val = sum % 10
            carry = sum // 10
            prev_node = current_node
            current_node = current_node.next
        if carry > 0:
            prev_node.next = ListNode(carry)
        head = __reverse(new_head)

        return head
