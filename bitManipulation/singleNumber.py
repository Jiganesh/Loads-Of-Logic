#  https://leetcode.com/problems/single-number/

class Solution(object):
    
    
    # Submitted By Jiganesh
    
    # TC: O(N)
    # SC: O(N)
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dictionary ={}
        for i in nums:
            if i in dictionary :
                dictionary [i]+= 1
            else :
                dictionary [i] =1
                
        for i in dictionary :
            if dictionary[i]==1:
                return i
            
    # TC : O(N)
    # SC : O(1)
    
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # If we take XOR of zero and some bit, it will return that bit
        # a XOR 0 = a, a XOR 0=a
        # If we take XOR of two same bits, it will return 0
        # a XOR a = 0 a XOR a=0
        # a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = b 
        # a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
        # So we can XOR all bits together to find the unique number.
        
        a =0 
        for i in nums:
            a ^= i
        return a
            
print(Solution().singleNumber([4,1,2,1,2]))