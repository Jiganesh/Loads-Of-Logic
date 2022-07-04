# https://leetcode.com/problems/wiggle-subsequence/


from typing import List
class Solution:
    
    
    # TC : O(N)
    # SC : O(N)
    
    # Runtime: 45 ms, faster than 73.32% of Python3 online submissions for Wiggle Subsequence.
    # Memory Usage: 13.9 MB, less than 36.01% of Python3 online submissions for Wiggle Subsequence.
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if len(nums)<2 : return len(nums)
        
        
        sequence = []
        
        for i in range (1, len(nums)):
            if nums[i]-nums[i-1] > 0:
                sequence.append(1)
            elif nums[i]-nums[i-1] < 0:
                sequence.append(0)
                
        # print(sequence)
        
        
        if not sequence : return 1
        
        toggle = sequence[0]
        length = 1
        
        for i in range (1, len(sequence)):
            if sequence[i] == toggle ^ 1:
                toggle ^=1
                length +=1
                
        return length+1
            
    # TC : O(N)
    # SC : O(1)        
    
    # Runtime: 60 ms, faster than 45.65% of Python3 online submissions for Wiggle Subsequence.
    # Memory Usage: 13.9 MB, less than 36.01% of Python3 online submissions for Wiggle Subsequence.
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        toggle = None
        length = 1
        
        
        for i in range (1, len(nums)):
            if nums[i]>nums[i-1] and toggle != True:
                length+=1
                toggle=True
            if nums[i]<nums[i-1] and toggle != False:
                length+=1
                toggle=False
                
            
        return length              
        
    