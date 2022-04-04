# https://leetcode.com/problems/next-permutation/

class Solution(object):
    
    # Runtime: 32 ms, faster than 74.78% of Python online submissions for Next Permutation.
    # Memory Usage: 13.6 MB, less than 15.56% of Python online submissions for Next Permutation.
    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        firstPointer = len(nums)-1
        secondPointer = len(nums)-1
        
        while firstPointer>=1 and nums[firstPointer-1] >= nums[firstPointer]:
            firstPointer-=1
        
        if firstPointer == 0:
            nums.sort()
            return
        
        firstPointer-=1
        
        while secondPointer>firstPointer and nums[secondPointer]<=nums[firstPointer]:
            secondPointer-=1
            
        nums[firstPointer], nums[secondPointer] = nums[secondPointer], nums[firstPointer]
        
        
        right = len(nums)-1
        left = firstPointer +1
        
        while left < right :
            nums[left], nums[right]= nums[right], nums[left]
            left+=1
            right-=1
        
        