# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    
    # Runtime: 47 ms, faster than 91.23% of Python3 online submissions for Sum of All Odd Length Subarrays.
    # Memory Usage: 13.9 MB, less than 65.09% of Python3 online submissions for Sum of All Odd Length Subarrays.
    
    
    # TC : O(N^2)
    # SC : O(1)

    def sumOddLengthSubarrays(self, arr) -> int:
        
        result = 0       
        for index , i in enumerate(arr):
            
            result+=i
            arr[index] = result
        
        
        slidingWindow = 3
        
        while slidingWindow <= len(arr):
            index =  0
            while index +slidingWindow <= len(arr):
            
                result +=  arr[index+slidingWindow-1] - arr[index-1] if index !=0 else arr[index+slidingWindow-1]
                index+=1
                
            slidingWindow+=2
            
        return result