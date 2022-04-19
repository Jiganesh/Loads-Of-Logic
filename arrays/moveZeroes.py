# https://leetcode.com/problems/move-zeroes/


class Solution:
    # Runtime: 152 ms, faster than 99.86% of Python3 online submissions for Move Zeroes.
    # Memory Usage: 15.6 MB, less than 19.78% of Python3 online submissions for Move Zeroes.
    
    def moveZeroes(self, nums) -> None:
        index, end = 0, len(nums)
        for i in range(end):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
        while index < end:
            nums[index] = 0
            index += 1
            
    # Runtime: 175 ms, faster than 84.41% of Python3 online submissions for Move Zeroes.
    # Memory Usage: 15.5 MB, less than 69.50% of Python3 online submissions for Move Zeroes.
    
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        
        pointerAtStart = 0
        countOfZeroes  = 0
        
        for i in range(len(nums)):
            if nums[i] !=0:
                nums[pointerAtStart] = nums[i]
                pointerAtStart+=1
            else:
                countOfZeroes += 1
                
        
        while countOfZeroes:
            nums[-countOfZeroes]=0
            countOfZeroes-=1
