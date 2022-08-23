# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    # TC: O(N)
    # SC: O(N)
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        array =[]
        while head !=None :
            array.append(head.val)
            head = head.next;
            
        #return max([l[i] + l[-i - 1] for i in range(len(l) // 2)])
        #creating extra list

        
        i=0
        maximum = array[0]
        while i<len(array)//2 :
            sum = array[i]+array[-i-1]
            maximum = max(maximum, sum)
            i+=1;
        return maximum

    # TC : O(N)
    # SC : O(1)
    
    # Runtime: 1653 ms, faster than 25.95% of Python3 online submissions for Maximum Twin Sum of a Linked List.
    # Memory Usage: 45.1 MB, less than 71.22% of Python3 online submissions for Maximum Twin Sum of a Linked List.
    def pairSum(self, head):
        
        # Step 1
        # Find the middle node
        
        slow = fast = first_head = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2
        # Reverse the second half
        second_head = slow
        prev = None
        
        while second_head:
            nxt = second_head.next
            second_head.next = prev
            
            prev = second_head
            second_head = nxt
            
        second_head = prev
        
        # Step 3
        # Traverse through both ends
        maximum_twin_sum = float("-inf")
        while first_head and second_head:

            maximum_twin_sum = max(maximum_twin_sum, first_head.val + second_head.val)
            first_head = first_head.next
            second_head = second_head.next
            
        return maximum_twin_sum
        
            
        
