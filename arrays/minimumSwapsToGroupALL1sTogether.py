# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/


class Solution(object):
    def minSwaps(self , nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Brute Force - Time Limit Exceeded
        n= len(nums)
        lenSlidingWindow = nums.count(1)
        nums= nums+nums
        count = n
        for i in  range(n):
            count = min(nums[i: i+lenSlidingWindow].count(0), count)
        return count
                
    
print(Solution().minSwaps([1,0,1,0,1]))
print(Solution().minSwaps([0,1,0,1,1,0,0]))
print(Solution().minSwaps([0,1,1,1,0,0,1,1,0]))
print(Solution().minSwaps([1,1,0,0,1]))
print(Solution().minSwaps([0,0,0,0,0]))
print(Solution().minSwaps([1,1,1,1,1]))


    
    
    
    