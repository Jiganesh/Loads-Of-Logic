# https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        head = list1
        
        while list1 and a>1:
            list1 = list1.next
            a-=1
            b-=1
        left = list1
        
        while list1 and b:
            list1 = list1.next
            b-=1
        right = list1.next
        
        left.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = right
        
        return head
        
        