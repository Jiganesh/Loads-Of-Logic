# https://leetcode.com/problems/palindrome-partitioning-ii/
# https://www.youtube.com/watch?v=9h10fqkI7Nk&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=37&ab_channel=AdityaVerma
# https://www.youtube.com/watch?v=HUeUmrQy9cs&t=305s&ab_channel=CodingDecoded


class Solution:
    
    
    # TLE
    
    def minCutApproach1(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dp = [[-1]*(len(s)+1) for _ in range (len(s)+1)]
        def palindrome(s, i, j):
            if i>=j: return True
            
            while i< j :
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        

        def helper(s, i, j):
            
            if i>=j :
                return 0
            
            if palindrome(s, i, j):
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            mini = float('inf')
            
            for k in range (i, j):
                
                if dp[i][k] != -1:
                    left = dp[i][k]
                else :
                    left = helper(s, i, k)
                    dp[i][k]= left
                    
                if dp[k+1][j] != -1:
                    right = dp[k+1][j]
                else:
                    right = helper(s, k+1, j)
                    dp[k+1][j] = right
                    
            
                temp = 1+ left + right
                mini = min(mini, temp)
                
            dp[i][j]=mini
            return mini
        
        return helper(s,0, len(s)-1)
            
            

    # Runtime: 5559 ms, faster than 5.05% of Python3 online submissions for Palindrome Partitioning II.
    # Memory Usage: 14.2 MB, less than 71.75% of Python3 online submissions for Palindrome Partitioning II.
    
    def minCutApproach2(self, s: str) -> int:
        def isPalindrome (s, i, j):
            return s[i:j+1]==s[i:j+1][::-1]

                    
        totalCuts = [i for i in range (len(s))]
        
        
        for j in range (len(s)):
            cut = j
            for i in range (j+1):
                if i<=j and isPalindrome(s, i, j):
                    cut = min (cut , 0 if i ==0 else totalCuts[i-1]+1)
                    
            totalCuts[j]= cut
        return totalCuts[-1]
    
print(Solution().minCutApproach2("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))