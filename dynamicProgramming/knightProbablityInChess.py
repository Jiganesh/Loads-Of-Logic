# https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    
    # Runtime: 503 ms, faster than 36.49% of Python3 online submissions for Knight Probability in Chessboard.
    # Memory Usage: 23.5 MB, less than 27.90% of Python3 online submissions for Knight Probability in Chessboard.
    
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        dx = [-2, -2, 2, 2, -1, -1, 1, 1]
        dy = [-1, 1, -1, 1, -2,  2, -2, 2]
        
        dp = {}
        
        def valid(i, j):
            return 0<=i<n and 0<=j<n
        
        def helper(i, j , moves):
            
            if not valid(i, j):
                return 0
            
            if moves==0:
                return 1
            
            if (i, j, moves) in dp:
                return dp[(i, j, moves)]
            
            ans=0
            for ind in range(8):
                x = i+dx[ind]
                y = j+dy[ind]
                
                ans += helper(x,y,moves-1)
            ans = ans/8
            
            
            dp[(i, j, moves)]=ans
            return ans
        
        return helper(row, column ,k)