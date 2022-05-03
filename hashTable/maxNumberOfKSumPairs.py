# https://leetcode.com/problems/max-number-of-k-sum-pairs/
class Solution:
    
    # Runtime: 692 ms, faster than 86.83% of Python3 online submissions for Max Number of K-Sum Pairs.
    # Memory Usage: 26.2 MB, less than 91.29% of Python3 online submissions for Max Number of K-Sum Pairs.
    
    def maxOperations(self, nums, k: int) -> int:
        
        count =0
        
        nums.sort()
        
        start = 0
        end = len(nums)-1
        
        while start < end :
            currentSum =  nums[start] + nums[end]
            if currentSum == k:
                start+=1
                end-=1
                count+=1
            elif currentSum< k:
                start+=1
            else:
                end-=1
                
        return count
        
        
        
        
        