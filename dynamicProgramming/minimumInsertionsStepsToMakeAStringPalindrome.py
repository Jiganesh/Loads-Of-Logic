# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution:
    
    # Runtime: 1252 ms, faster than 54.18% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.
    # Memory Usage: 15.9 MB, less than 76.05% of Python3 online submissions for Minimum Insertion Steps to Make a String Palindrome.

    # Hint : This problem is variation of lcs(longest Palindromic Subsequence)
    def minInsertions(self, s: str) -> int:
        
        s1= s
        s2 =s[::-1]
        
        dp = [[0]*(len(s)+1) for i in range (len(s)+1)]
        
        for i in range (1,len(s1)+1):
            for j in range (1, len(s2)+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else :
                    dp[i][j]= max(dp[i-1][j], dp[i][j-1])
                    
                    
        return len(s) - dp[-1][-1]