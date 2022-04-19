# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    
    # TC : O(N)
    # SC : O(N)
    
    
    # Runtime: 281 ms, faster than 38.18% of Python online submissions for Product of Array Except Self.
    # Memory Usage: 22.1 MB, less than 32.91% of Python online submissions for Product of Array Except Self.
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left , right  = [0]*n ,[0]*n
        
        mul = 1
        for i in range (0, len(nums)):
            mul*=nums[i]
            left[i] = mul
            
        mul = 1
        for i in range (len(nums)-1,-1,-1):
            mul*=nums[i]
            right[i] = mul
    
        for i in range (1, len(nums)-1):
            nums[i] = left[i-1]*right[i+1]
            
        nums[0] = right[1]
        nums[-1] = left[-2]
            
        return nums
    
    
    # TC : O(N)
    # SC : O(1)
    
    # Runtime: 196 ms, faster than 93.31% of Python online submissions for Product of Array Except Self.
    # Memory Usage: 20.4 MB, less than 77.22% of Python online submissions for Product of Array Except Self.
    
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        outputArray = [1]*len(nums)
        
        prefix = nums[0]
        
        for i in range (1, len (outputArray)):
            
            outputArray [i] = prefix
            prefix *= nums[i]
            
        postfix = nums[-1]
        
        for i in range(len(outputArray)-2, -1, -1):
            
            outputArray[i]*=postfix
            postfix *= nums[i]
            
        return outputArray