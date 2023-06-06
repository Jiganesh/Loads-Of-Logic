# https://leetcode.com/problems/single-number-ii/
# https://www.youtube.com/watch?v=IoF-FIQuFT0

from typing import List
from collections import Counter

class Solution:
  
    # Naive Approach
    def singleNumber(self, nums: List[int]) -> int:


        count = Counter(nums)
        for k, v in count.items():
            if v==1:
                return k
            
    # Constant Space Approach
    
    def singleNumber(self, nums: List[int]) -> int:

        result = 0

        for i in range (0, 32):
            set_bit = 1 << i
            count_evens, count_odds = 0, 0
            for num in nums:
                if num & set_bit:
                    count_odds+=1
                else:
                    count_evens+=1
        
            if count_odds%3:
                result |= set_bit

        if (result & 1<<31)  == 0:
            return result
        else:    
            # handle for negative numbers
            return -((result^(0xFFFF_FFFF))+1 )

            
            