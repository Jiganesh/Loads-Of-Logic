# https://leetcode.com/problems/word-break-ii/

class Solution:
    
    # Runtime: 39 ms, faster than 59.07% of Python3 online submissions for Word Break II.
    # Memory Usage: 13.8 MB, less than 99.26% of Python3 online submissions for Word Break II.
    def wordBreak(self, s: str, wordDict) :
       
        
        dp = [[] for i in s]
        
        
        for j in range (len(s)):
            for i in range(j+1):
                word = s[i:j+1]
                if word in wordDict:
                    
                    if i>0:
                        for k in dp[i-1]:
                    
                            dp[j].append(k+[word])
                    else:
                        dp[j].append([word])
                        
        print(dp)
                        
        return [" ".join(i) for i in dp[-1]]
                    