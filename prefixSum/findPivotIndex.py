# https://leetcode.com/problems/find-pivot-index/

class Solution:
    
    # TC : O(N)
    # SC : O(1)
    
    # Runtime: 226 ms, faster than 39.17% of Python3 online submissions for Find Pivot Index.
    # Memory Usage: 15.4 MB, less than 11.76% of Python3 online submissions for Find Pivot Index.
    def pivotIndex(self, nums) -> int:
        
        
        for index in range (1,len(nums)):
            nums[index] = nums[index]+ nums[index-1]
        
        endElement = nums[-1]
            
        for pivot in range(len(nums)):
            
            if pivot != 0 and nums[pivot-1] == endElement-nums[pivot] :
                return pivot
            elif pivot ==0 and  endElement == nums[pivot]:
                return 0
            
        return -1