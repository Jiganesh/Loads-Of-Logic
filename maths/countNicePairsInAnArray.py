# https://leetcode.com/problems/count-nice-pairs-in-an-array/

from typing import List
from itertools import Counter

class Solution:
    
    # BruteForce
    
    # TC : O(N^2)
    # SC : O(N)
    
    #1
    """
    condition : num1 + rev(num2) == num2 + rev(num1)
                num1-num2 = rev(num1)-rev(num2)
    """
    def countNicePairs(self, nums: List[int]) -> int:
        
        
        
        str_nums = list(map(str , nums))
        
        rev = { int(i) : int(i[::-1]) for i in str_nums}
        
        
        pair = 0
        
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                
                if nums[i]-nums[j] == rev[nums[i]] - rev[nums[j]]:
                    pair+=1
                    
        return pair
    
    #2
    """
    Expanding #1 condition :
    
    num1-rev(num1) == num2 - rev(num2)
    
    In other words :
    B[i] == B[J]
    
    We just count all the pairs who have B[i]
    """
    # Runtime: 782 ms, faster than 92.91% of Python3 online submissions for Count Nice Pairs in an Array.
    # Memory Usage: 24.4 MB, less than 95.84% of Python3 online submissions for Count Nice Pairs in an Array.

    def countNicePairs(self, nums: List[int]) -> int:
        
        MOD = (10**9) +7
        
        countPairs = Counter()
        pairs = 0
        
        
        for num in nums:
            rev_num = int(str(num)[::-1])
            pairs+= countPairs[num-rev_num]
            countPairs[num-rev_num] +=1
            
            
        return pairs%MOD