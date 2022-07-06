# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

from typing import List
from collections import defaultdict

class Solution:
    
    # BRUTE FORCE
    
    # TC : O(N^2 Log N)
    # SC : O(N)
    
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        def binarySearch (arr, target):
            start = 0
            end = len(arr)-1
            
            while start <= end :
                mid = start + (end-start)//2
                
                if arr[mid] == target:
                    return True
                elif target > arr[mid]:
                    start= mid+1
                else :
                    end = mid-1
                    
            return False
        
                    
                    
        def dfs(a, b , length=0):
            while binarySearch(arr, a+b) :
                return dfs(b,a+b,  length+1)
        
            return length+2
        
        
        maximum = float('-inf')
        for i in range (len(arr)):
            for j in range(i+1, len(arr)):
                maximum =  max(maximum, dfs(arr[i], arr[j]))
                
        return maximum if maximum>2 else 0
    
    
    # OPTIMAL SOLUTION
    # TWO SUM
    
    # TC : O(N^2)
    # SC : O(N^2)
    
    # Runtime: 2486 ms, faster than 56.31% of Python3 online submissions for Length of Longest Fibonacci Subsequence.
    # Memory Usage: 14.9 MB, less than 37.20% of Python3 online submissions for Length of Longest Fibonacci Subsequence.
    
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        
        n = len(arr)
        
        index = { num: ind for ind, num in enumerate(arr)}
        
        dp = [[0]*(n+1) for i in range (n+1)]
        
        
        
        for i in range (1,n+1):
            for j in range (i+1, n+1):
                dp[i][j] = 2
                
            
            
        maximum_length = float("-inf")
        
        for ind_tar , target_num in enumerate(arr):
            
            for ind_sec  in range (ind_tar):
                
                second_num = arr[ind_sec]
                
                first_num = target_num-second_num
                
                if first_num in index and  index[first_num] < ind_sec:
                    
                    
                    ind_fir = index[first_num]
                    dp[ind_sec+1][ind_tar+1] = dp[ind_fir+1][ind_sec+1] + 1 
                    maximum_length = max(maximum_length, dp[ind_sec+1][ind_tar+1])
                    
                                        
        return maximum_length>2 and maximum_length or 0


    # TC : O(N^2)
    # SC : O(N) 
       
    # Runtime: 1724 ms, faster than 80.20% of Python3 online submissions for Length of Longest Fibonacci Subsequence.
    # Memory Usage: 14.9 MB, less than 37.20% of Python3 online submissions for Length of Longest Fibonacci Subsequence.
    
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        
        n = len(arr)
        
        index = { num: ind for ind, num in enumerate(arr)}
        dp = defaultdict(lambda :2) 
        
        for ind_tar , target_num in enumerate(arr):
            
            for ind_sec in range(ind_tar):
            
                second_num = arr[ind_sec]
                first_num = target_num - second_num
                
                
                if first_num in index and index[first_num]< ind_sec:
                    ind_fir = index[first_num]        
                    dp[ind_sec, ind_tar] = dp[ind_fir,ind_sec]+1
                    
        return max(dp.values()) if dp else 0
    
