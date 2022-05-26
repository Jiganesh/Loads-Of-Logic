# https://leetcode.com/problems/word-break/
# Solution : https://www.youtube.com/watch?v=2NaaM_z_Jig&t


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        
        dp = [0 for i in s]
        
        for j in range (len(s)):
            for i in range (j+1):
                word = s[i:j+1]
                if word in wordDict:
                    dp[j]+=dp[i-1] if i>0 else 1
                    
                    
        return dp[-1]>0
                    
        
            
        