# https://leetcode.com/problems/find-the-middle-index-in-array/submissions/

class Solution(object):
    
    # Runtime: 48 ms, faster than 19.31% of Python online submissions for Find the Middle Index in Array.
    # Memory Usage: 13.3 MB, less than 93.10% of Python online submissions for Find the Middle Index in Array.
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = 0
        for index , i in enumerate(nums):
            result +=i 
            nums[index] = result
            
            
        endElement = nums[-1]
        
        for i in range (len(nums)):
            
            left = nums[i-1] if i!=0 else 0
            right = endElement - nums[i]
            
            if left == right : return i
            
        return -1