# https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution:
    
    # Runtime: 285 ms, faster than 87.77% of Python3 online submissions for Delete Operation for Two Strings.
    # Memory Usage: 16 MB, less than 65.72% of Python3 online submissions for Delete Operation for Two Strings.
    
    def minDistance(self, word1: str, word2: str) -> int:
        
        # Hint : Problem Variation of Longest Common Subsequence (Minimum Number Of Insertions and Deletions)
        
        dp = [[0] * (len(word2)+1) for i in range(len(word1)+1)]
        
        for i in range (1, len(word1)+1):
            for j in range (1,len (word2)+1):
                
                if word1[i-1]== word2[j-1] :
                    dp[i][j] = 1+dp[i-1][j-1]
                else :
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
                    
        # for i in dp : print(*i)
                    
        return len(word1)+len(word2) - 2*dp[-1][-1]