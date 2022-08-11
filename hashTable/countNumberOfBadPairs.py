from typing import List
from collections import defaultdict

class Solution:
    
    # TC : O(N)
    # SC : O(N)
    
    # Runtime: 1225 ms, faster than 33.33% of Python3 online submissions for Count Number of Bad Pairs.
    # Memory Usage: 33.4 MB, less than 100.00% of Python3 online submissions for Count Number of Bad Pairs.
    
    '''
    badPairs :
    
    j-i != nums[j] - nums[i]
    can be written as  nums[j] - j != nums[i] -i
    
    hence the good pairs are
    nums[j] -j = nums[i] -i
    
    hence we use hashmap to check how many pairs are there with same difference
    
    '''
    def countBadPairs(self, nums: List[int]) -> int:
        
        lookup = defaultdict(int)
        goodPairs = 0
        
        for ind, num in enumerate(nums):
            goodPairs += lookup[num-ind]
            lookup[num-ind]+=1
            
        n = len(nums)-1
        totalPairs = n * (n+1)//2
        
        return totalPairs-goodPairs
