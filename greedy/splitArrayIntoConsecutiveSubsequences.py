# https://leetcode.com/problems/split-array-into-consecutive-subsequences/


from typing import List
from collections import Counter, defaultdict



class Solution:
    
    # Runtime: 592 ms, faster than 86.16% of Python3 online submissions for Split Array into Consecutive Subsequences.
    # Memory Usage: 15.5 MB, less than 25.22% of Python3 online submissions for Split Array into Consecutive Subsequences.
    
    def isPossible(self, nums: List[int]) -> bool:
        
        frequencyMap = Counter(nums)
        vaccancyMap = defaultdict(int)
        
        for num in nums:
            
            if frequencyMap[num] <= 0:
                continue
             
            # If the number is available to be used and there is vaccancy for that number
            elif vaccancyMap[num] > 0:
                vaccancyMap[num]-=1
                frequencyMap[num]-=1
                             
                vaccancyMap[num+1]+=1
                
            # If that number is availble and there is no vaccancy for the number
            # That number will create his own sequence
            elif frequencyMap[num+1]>0 and frequencyMap[num+2]>0:
                
                frequencyMap[num]-=1
                frequencyMap[num+1]-=1
                frequencyMap[num+2]-=1
                
                vaccancyMap[num+3] += 1
            
            # If none of the conditions are satisfied then we return false 
            else :
                return False
            
        return True
