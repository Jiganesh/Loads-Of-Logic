# https://leetcode.com/problems/non-decreasing-array/


from typing import List

class Solution:
    
    # Runtime: 379 ms, faster than 6.78% of Python3 online submissions for Longest Mountain in Array.
    # Memory Usage: 15.5 MB, less than 19.02% of Python3 online submissions for Longest Mountain in Array.
    def longestMountain(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        left = [0]*n
        right = [0]*n
        
        # Determine elements smaller on left 
        for i in range (1, n):
            if arr[i-1]<arr[i]:
                left[i]= 1 + left[i-1]
                
        # Determine elements smaller on right
        for i in range (n-2, -1, -1):
            if arr[i]>arr[i+1]:
                right[i]= 1+right[i+1]
                
        maximum_length = 0       
        for i in range (n):
            # To insure there is atleast slope to climb and slope to fall
            # It wont be mountain if index has no slope on both sides
            if left[i] and right[i]:
                maximum_length = max(maximum_length, left[i]+right[i]+1)
            
        return maximum_length
    
    # TC : O(N)
    # SC : O(1)
    
    # Runtime: 316 ms, faster than 20.21% of Python3 online submissions for Longest Mountain in Array.
    # Memory Usage: 15.2 MB, less than 50.80% of Python3 online submissions for Longest Mountain in Array.
    def longestMountain(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        maximum_length = 0
        
        for i in range (1,n-1):
            l = r =i
            if arr[i-1]<arr[i]>arr[i+1]:
                
                while l>0 and arr[l-1]<arr[l]: l-=1
                while r<n-1 and arr[r]>arr[r+1] : r+=1

                elements_to_left = i-l
                elements_to_right = r-i

                if elements_to_left and elements_to_right:
                    maximum_length = max(maximum_length, elements_to_left+elements_to_right+1)
                
        return maximum_length