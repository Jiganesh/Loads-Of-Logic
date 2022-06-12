# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

class Solution:
    # Runtime: 1240 ms, faster than 100.00% of Python3 online submissions for Count Subarrays With Score Less Than K.
    # Memory Usage: 28.6 MB, less than 60.00% of Python3 online submissions for Count Subarrays With Score Less Than K.
    def countSubarrays(self, nums, k) :
        
        
        current = start = result = 0
        for end in range (len(nums)):
            current += nums[end]
            while current * (end -start+1)>=k:
                current-=nums[start]
                start +=1            
            result += end-start+1            
            
        return result 