# https://leetcode.com/problems/triangle/

class Solution:
    
    # BELOW TWO APPROACHES ARE TOP DOWN APPROACH
    
    # Recursive Approach
    def minimumTotal(self, triangle):
        
        R = len(triangle)
        C = len(triangle[-1])
        dp = [[float("inf")]*C for  i in range (R)]
        
        def dfs_helper(row, col):
            

            if 0<=row<R and 0<=col<C:
                dp[row][col] = triangle[row][col]+ min(dfs_helper(row+1,col), dfs_helper(row+1, col+1))
                return dp[row][col]
            else:
                return 0
        
                        
        return dfs_helper(0,0)
        # for row in dp :
        #     print(*row)
    
    # Memoized Approach
    
    # Runtime: 69 ms, faster than 90.46% of Python3 online submissions for Triangle.
    # Memory Usage: 15.5 MB, less than 17.42% of Python3 online submissions for Triangle.
    
    # TC: O(N^2)
    # SC: O(N^2)
    def minimumTotal(self, triangle):

        
        R = len(triangle)
        C = len(triangle[-1])
        dp = [[float("inf")]*C for  i in range (R)]
        
        def dfs_helper(row, col):
        
            if 0<=row<R and 0<=col<C:
                
                # Memoization #TLE if this line not present
                if dp[row][col] != float("inf"): return dp[row][col]
                
                dp[row][col] = triangle[row][col]+ min(dfs_helper(row+1,col), dfs_helper(row+1, col+1))
                return dp[row][col]
            else:
                return 0
                        
        return dfs_helper(0,0)

    # BELOW APPROACH IS BOTTOM UP APPROACH
    
    # TC : O(N^2)
    # SC : O(N)
    
    # Runtime: 125 ms, faster than 19.81% of Python3 online submissions for Triangle.
    # Memory Usage: 14.9 MB, less than 92.55% of Python3 online submissions for Triangle.
    
    def minimumTotal(self, triangle):
        
        dp = [0]*(len(triangle)+1)
        
        for row in range (len(triangle)-1,-1,-1):
            for col in range (len(triangle[row])):
                dp[col] = min(dp[col], dp[col+1])+ triangle[row][col]
                
        # print(dp)
                
        return dp[0]        
        
