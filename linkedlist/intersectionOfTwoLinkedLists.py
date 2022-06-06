# https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    # Runtime: 247 ms, faster than 30.08% of Python3 online submissions for Intersection of Two Linked Lists.
    # Memory Usage: 29.9 MB, less than 26.80% of Python3 online submissions for Intersection of Two Linked Lists.
    
    def getIntersectionNode(self, headA, headB) :
        
        
        lenA =0
        pa=headA
        pb=headB
        
        while headA:
            lenA+=1
            headA=headA.next
        
        lenB =0
        while headB:
            lenB+=1
            headB=headB.next
            
        
        if lenA>lenB:
            while lenA != lenB:
                lenA-=1
                pa=pa.next
        else:
            while lenB != lenA:
                lenB-=1
                pb=pb.next
                
        
        while pa and pb and pa !=pb:
            pa=pa.next
            pb=pb.next
        
        return pa
    
    
    # Runtime: 160 ms, faster than 93.54% of Python3 online submissions for Intersection of Two Linked Lists.
    # Memory Usage: 29.5 MB, less than 93.75% of Python3 online submissions for Intersection of Two Linked Lists.
    
    def getIntersectionNode(self, headA, headB) :
                
        pa = headA
        pb = headB
        
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
            
        return pa