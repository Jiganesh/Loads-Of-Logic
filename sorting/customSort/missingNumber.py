# https://leetcode.com/problems/missing-number/
class Solution:
    
    # TC :  O(N)
    # SC : O(1)
    def missingNumber(self, nums) -> int:
        
        
        for i in range(len(nums)):
            while nums[i]<len(nums) and nums[i] != i:
                numberAtIndexI = nums[i]
                nums[i], nums[numberAtIndexI]= nums[numberAtIndexI], nums[i]
                
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
    
        return len(nums)
    
    # TC : O(N)
    # SC : O(1)
    def missingNumber(self, nums) :
        
        summation = 0
        maximum = 0
        is_zero = False
        
        for i in nums:
            summation+=i
            maximum = max(i,maximum)
            if is_zero==False: is_zero = (i==0)
        
        missingNumber = maximum*(maximum+1)//2 -summation
        
        return maximum+1 if missingNumber==0 and is_zero else missingNumber 
    
    
