# https://leetcode.com/problems/longest-harmonious-subsequence/

import bisect
from collections import Counter

class Solution:
    
    # Solved with HashTable
    
    # TC : O(NlogN)
    # SC : O(N)
    
    def findLHS(self, nums) :
        
        dictionary = Counter(nums)
        maxans = 0
        for i in dictionary:
            if i+1 in dictionary : maxans = max(maxans, dictionary[i]+dictionary[i+1])
        return maxans
    
    # Solved with Binary Search
    
    # TC: O(NlogN)
    # SC : O(N)
    
    def findLHS(self, nums) -> int:
        
        nums.sort()
        maxans = 0
        for i in nums:
            right = bisect.bisect_right(nums,i+1) 
            left = bisect.bisect_left(nums,i)
            
            if  nums[right-1]-nums[left]==1:
                ans = right-left
                maxans = max(maxans, ans)
            
        return maxans