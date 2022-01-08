# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
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
    
