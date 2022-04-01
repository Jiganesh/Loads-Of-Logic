def matrixMultiplication(arr, n):
    
    dp = [[-1]* (len(arr)+1) for i in range (len(arr)+1)]
    
    def helper(arr, i, j):
        if i == j : return 0
        
        if dp[i][j] != -1 : return dp[i][j]
        
        ans = float('inf')
        
        for  k in range (i , j):
            tempAns = helper(arr, i, k) + helper(arr, k+1, j) + arr[i-1]*arr[k]*arr[j]
            ans = min(tempAns, ans) 
            
        dp[i][j]= ans
        return ans
    
    return helper(arr, 1, len(arr)-1)
    
arr = [4, 5, 3, 2]
print(matrixMultiplication(arr, len(arr))) #70


arr = [10, 15, 20 ,25]
print(matrixMultiplication(arr, len(arr))) #8000


            
        