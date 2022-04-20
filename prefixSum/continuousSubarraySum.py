# https://leetcode.com/problems/continuous-subarray-sum/

# https://www.youtube.com/watch?v=OKcrLfR-8mE&t=734s


class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        
        dictionary = {0:-1}
        summation = 0
        for i in range (len(nums)):
            
            summation+=nums[i]
            
            # Note
            # If you do :
            # if summation%k in dictionary and i- dictionary[summation%k]>= 2 then that will be wrong becuase
            # it will jump to else statement and update dictionary 
            # and we need to continue process till we get subarray of len >= 2
            
            if summation%k in dictionary: 
                if i-dictionary[summation%k] >=2 :
                    return True
            else:
                dictionary[summation%k]= i

        
        return False
    
    # Above Logic but Aesthetic Code
        
    # Runtime: 932 ms, faster than 86.72% of Python3 online submissions for Continuous Subarray Sum.
    # Memory Usage: 33.2 MB, less than 72.05% of Python3 online submissions for Continuous Subarray Sum.

    def checkSubarraySum(self, nums, k) -> bool:
        
        dictionary = {0:-1}
        summation = 0
        for i in range (len(nums)):
            
            summation+=nums[i]
            
            if summation%k not in dictionary: 
                dictionary[summation%k]= i
            elif i-dictionary[summation%k] >=2 :
                return True
        
        return False
    
    
print(Solution().checkSubarraySum([5,0,0,0,0]))
                