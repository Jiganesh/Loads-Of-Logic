# https://leetcode.com/problems/sort-array-by-parity/


class Solution:
    
    # Runtime: 87 ms, faster than 74.12% of Python3 online submissions for Sort Array By Parity.
    # Memory Usage: 14.7 MB, less than 63.70% of Python3 online submissions for Sort Array By Parity.
    def sortArrayByParity(self, nums) :
        
        
        pointer1 =0
        pointer2 =1
        
        while  pointer2 < len(nums):
            while pointer1<pointer2 and nums[pointer1]%2==0:
                pointer1+=1
                
            if nums[pointer2]%2==0:
                nums[pointer1], nums[pointer2] = nums[pointer2], nums[pointer1]
                pointer1+=1
                
            pointer2+=1
            
        return nums
        