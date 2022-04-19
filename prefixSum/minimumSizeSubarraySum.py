# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    
    # TLE  Brute Force
    def minSubArrayLen(self, target, nums) -> int:
    
        
        summation = 0
        
        array =[]
        
        for i in nums:
            summation+=i
            array.append(summation)
            
        minimum =float('inf')
        
        for i in range (len(array)):
            for j in range (i+1,len(array)):
                
                if array[j]-array[i] >=target:
                    minimum = min(j-i, minimum)
                    
        return  minimum if minimum != float('inf') else 0
    
    
    
    
    def minSubArrayLen(self, target, nums) -> int:
        
        leftPointer = 0
        rightPointer = 0
        
        summation = 0
        minimumSubarray = float('inf')
        
        for i in nums:
            
            summation+=i
            rightPointer+=1
            
            while summation >= target :
                
                minimumSubarray = min(rightPointer - leftPointer, minimumSubarray)
                summation-= nums[leftPointer]
                leftPointer+=1
                
        return minimumSubarray if minimumSubarray != float('inf') else 0
    
    
    
    # Little Efficient that above algorithm as we are using while loop with pointers instead of for loop
    
    # Runtime: 87 ms, faster than 71.41% of Python3 online submissions for Minimum Size Subarray Sum.
    # Memory Usage: 16.8 MB, less than 52.83% of Python3 online submissions for Minimum Size Subarray Sum.
    
    def minSubArrayLen(self, target, nums) -> int:
    
        leftPointer = 0
        rightPointer = 0
        
        summation = 0
        minimumSubarray = float('inf')
        
        while rightPointer< len(nums):
            
            summation+=nums[rightPointer]
            rightPointer+=1
            
            while summation >= target :
                
                minimumSubarray = min(rightPointer - leftPointer, minimumSubarray)
                summation-= nums[leftPointer]
                leftPointer+=1
                
        return minimumSubarray if minimumSubarray != float('inf') else 0