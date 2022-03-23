#User function Template for python3

# https://practice.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1/

class Solution:

    def isSubsetSum ( N, arr, sum):
        # code here
            
        dp = [[0 for i in range (sum+1)] for j in range (N+1) ] 
        
        for i in range(N+1):
            for j in range(sum+1):
                if i==0:
                    dp[i][j]=False
                if j ==0:
                    dp[i][j]=True
                    
        for i in range(1,N+1):
            for j in range (1,sum+1):
                
                if arr[i-1]<= j:
                    dp[i][j]= dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j]= dp[i-1][j]
                
        for i in range(N+1):
            for j in range (sum+1):
                print(dp[i][j] ,end ="\t")
            print()
            
    
Solution().isSubsetSum(5, [2,3,7,8,10],12)