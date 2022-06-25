
from typing import List
class Solution:
    
    # Bruteforce TLE
    def checkPossibility(self, nums: List[int]) -> bool:    
        
        for i in range (len(nums)):
            
            array = nums[: i]+ nums[i+1:]
            if sorted(array)==array:
                return True
            
        return False
            
            
    # Runtime: 189 ms, faster than 96.05% of Python3 online submissions for Non-decreasing Array.
    # Memory Usage: 15.4 MB, less than 15.99% of Python3 online submissions for Non-decreasing Array.
            
    def checkPossibility(self, nums: List[int]) -> bool:
        
        
        
        element_changed = False
        
        for i in range (len(nums)-1):
            
            
            
            if nums[i]> nums[i+1]:
                
                if element_changed : return False
                
                #    i i+1  or   i  i+1
                # [1 4 2]       [4, 2]
                if i==0 or nums[i+1]>= nums[i-1]:
                    nums[i] = nums[i+1]
                # if we encounter below condition
                #     i   i+1
                # [3, 4 , 2]
                else:
                    nums[i+1]= nums[i]
                    
                element_changed = True
                
        return True
                    
                    
         
                    
                    