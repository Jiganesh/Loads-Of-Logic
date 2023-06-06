# https://leetcode.com/problems/reverse-nodes-in-k-group/

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    # Naive Approach
    
    # TC: O(N)
    # SC : O(N)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        array = []
        current = head
        while current:
            array.append(current.val)
            current = current.next

        result = []
        temp = []

        for num in array:
            temp.append(num)
            if len(temp)==k:
                result.extend(temp[::-1])
                temp=[]

        result.extend(temp)

        current = head
        for num in result :
            current.val = num
            current = current.next

        return head
    
    # TC : O(N)
    # SC : O(1)
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummyhead = ListNode(-1)
        dummyNode = dummyhead

        def reverse(head):

            current_node = head
            previous_node = None

            while current_node :
                next_node = current_node.next
                current_node.next = previous_node

                previous_node = current_node
                current_node = next_node



            head = previous_node
            return head

        
        pointer1 = head
        pointer2 = head

        node = 0

        while pointer2 and pointer2.next:

            pointer2 = pointer2.next
            node+=1

            if node == k-1:
                next_node = pointer2.next if pointer2 else None
                if pointer2 : 
                    pointer2.next = None

                new_node = reverse(pointer1)
                dummyNode.next = new_node
                while dummyNode.next:
                    dummyNode = dummyNode.next
                pointer1 = pointer2 = next_node
                node = 0

        dummyNode.next = pointer1
        return dummyhead.next
