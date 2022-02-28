# https://leetcode.com/problems/summary-ranges/
class Solution(object):
    
    # Submitted by Jiganesh
    
    # TC :O(N)
    # SC : O(P*M) where P is length of list and M is length of string but O(1) because of return value
    
    # Runtime: 25 ms, faster than 47.01% of Python online submissions for Summary Ranges.
    # Memory Usage: 13.2 MB, less than 99.46% of Python online submissions for Summary Ranges.
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if len(nums )==0:
            return result
        
        
        def makeRange(start,end):
            if start == end:
                return str(start)
            else:
                return str(start)+"->"+str(end)
            
        start = nums[0]
        for i in range (1, len(nums)):
            if nums[i]-nums[i-1]!=1:
                result.append(makeRange(start, nums[i-1]))
                start = nums[i]
                
        result.append(makeRange(start, nums[len(nums)-1]))        
        return result