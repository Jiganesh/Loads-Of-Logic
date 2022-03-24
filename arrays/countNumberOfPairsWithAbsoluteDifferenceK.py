# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

from collections import Counter

class Solution(object):
    
    # Brute Force Approach
    
    # TC : O(N
    # SC : O(N)
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count =0
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i]-nums[j])==k: 
                    count +=1
        return count
                
                
                
    
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dictionary =Counter()
        count=0
        for i in nums:
            dictionary[i]+=1
            count += dictionary[i-k] + dictionary[i+k]
            
        return count 