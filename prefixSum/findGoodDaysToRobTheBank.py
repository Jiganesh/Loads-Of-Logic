# https://leetcode.com/problems/find-good-days-to-rob-the-bank/

from typing import List
class Solution:
    
    # Runtime: 1695 ms, faster than 20.58% of Python3 online submissions for Find Good Days to Rob the Bank.
    # Memory Usage: 33.3 MB, less than 33.79% of Python3 online submissions for Find Good Days to Rob the Bank.
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        
        n = len(security)
        
        
        element_smaller_to_left = [0]*n
        element_greater_to_right = [0]*n
        
        # Determining elements smaller to left
        for i in range (1, n):    
            if security[i-1]>=security[i] :
                element_smaller_to_left[i] = 1+element_smaller_to_left[i-1]   
            else :
                element_smaller_to_left[i] = 0
                
        # Determining elements greater to right:
        for i in range (n-2, -1, -1):
            if security[i]>security[i+1]:
                element_greater_to_right[i] = 0
            else:
                element_greater_to_right[i] = 1 + element_greater_to_right[i+1]
                
        
        # print(element_smaller_to_left, element_greater_to_right)
        
        result = []
        for i in range (n):
            if element_smaller_to_left[i]>=time and  element_greater_to_right[i]>=time:
                result.append(i)
        
        return result 