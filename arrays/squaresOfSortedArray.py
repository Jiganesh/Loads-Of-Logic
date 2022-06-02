# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution(object):
    
    # Runtime: 242 ms, faster than 50.07% of Python online submissions for Squares of a Sorted Array.
    # Memory Usage: 15.5 MB, less than 72.04% of Python online submissions for Squares of a Sorted Array.
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        l, r = 0 , len(nums)-1
        res =[]
        while l<=r:
            if nums[l]**2>nums[r]**2:
                res.append(nums[l]**2)
                l+=1
            else:
                res.append(nums[r]**2)
                r-=1
        return res[::-1]
