# https://leetcode.com/problems/edit-distance/
# Reference
# https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition
# https://www.youtube.com/watch?v=XYi2-LPrwm4&t=732s # Watch only till Intuition


class Solution:
    
    # TC : O(N*M)
    # SC : O(N*M)
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        dp = [[1]* (len(word1)+1) for i in range (len(word2)+1)]
        
        
        for row_in_dp in range (len(word2)+1):
            dp[row_in_dp][0]=row_in_dp
            
        for col_in_dp in range (len(word1)+1):
            dp[0][col_in_dp]=col_in_dp           
        
        for i in range (1,len(word2)+1):
            for j in range (1,len(word1)+1):
                if word2[i-1]==word1[j-1]:
                    dp[i][j]= dp[i-1][j-1]
                else:
                    dp[i][j]= 1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    
        for i in dp:
            print(*i)
                    
        return dp[-1][-1]