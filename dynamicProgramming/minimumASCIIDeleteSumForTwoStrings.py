# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution:
    
    # Runtime: 719 ms, faster than 82.96% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
    # Memory Usage: 15.1 MB, less than 77.58% of Python3 online submissions for Minimum ASCII Delete Sum for Two Strings.
    
    
    # Hint : Problem Variation of Longest Common Subsequence 
    def minimumDeleteSum(self, s1: str, s2: str) -> int: 
        
            
        dp = [[0]* (len(s2)+1) for i in range (len(s1)+1)]
        p=0
        
        for i in range (1,len(s1)+1):
            for j in range (1,len(s2)+1):
                if s1[i-1]==s2[j-1] :
                    dp[i][j] = ord(s1[i-1])+dp[i-1][j-1]
                else : 
                    # we select characters with maximum ascii value to remove so that we are left with lowest ascii characters to delete
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
            # last string is maximum answer possible 
            # hence the subtraction will be minimum possible 
         
        for i in dp : 
            for j in i:
                print(chr(j) if j else "*", end="  ")
            print()
            
        def asciiValue (string):
            value = 0
            for i in string :
                value+=ord(i)
            return value
        
        return asciiValue (s1) + asciiValue (s2)- 2 * (dp[-1][-1])

print (Solution().minimumDeleteSum("ae", "ea"))
