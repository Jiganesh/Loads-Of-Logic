# https://leetcode.com/problems/contains-duplicate/

class Solution:
    
    # Runtime: 497 ms, faster than 72.74% of Python3 online submissions for Contains Duplicate.
    # Memory Usage: 26 MB, less than 72.32% of Python3 online submissions for Contains Duplicate.
    
    # TC : O(N log N)  Iterating through the array and inserting in hashtable
    # SC : O(N)
    def containsDuplicate(self, nums) -> bool:
        lookup = set()
        for i in nums:
            if i in lookup:
                return True
            else:
                lookup.add(i)
        return False
    
    # Sorting 
    # TC : O(N)
    # SC : O(1)
    def containsDuplicate(self, nums) -> bool:
    
        nums.sort()
        for i in range (len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
    