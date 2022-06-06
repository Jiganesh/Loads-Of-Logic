# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
class Solution:
    
    # Runtime: 908 ms, faster than 100.00% of Python3 online submissions for Partition Array Such That Maximum Difference Is K.
    # Memory Usage: 28.6 MB, less than 40.00% of Python3 online submissions for Partition Array Such That Maximum Difference Is K.
    def partitionArray(self, nums, k) :
        
        nums.sort()
        
        minimum = nums[0]
        count = 0
        
        for i in range (len(nums)):
            
            if nums[i]-minimum > k:
                minimum = nums[i]
                count+=1
                
        return count+1 # Adding 1 because it will be last subsequence