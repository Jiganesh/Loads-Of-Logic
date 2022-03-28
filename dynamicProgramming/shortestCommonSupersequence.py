# https://leetcode.com/problems/shortest-common-supersequence/

# Reference
# https://www.geeksforgeeks.org/print-shortest-common-supersequence/
# https://www.youtube.com/watch?v=823Grn4_dCQ&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=25&ab_channel=AdityaVerma
class Solution(object):
    
    # Runtime: 368 ms, faster than 81.48% of Python online submissions for Shortest Common Supersequence .
    # Memory Usage: 21.6 MB, less than 87.04% of Python online submissions for Shortest Common Supersequence .
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        
        
        def longestCommonSubsequence (str1, str2):
            dp= [[0]*(len(str2)+1) for i in range (len(str1)+1)]
            
            for i in range (1,len(str1)+1):
                for j in range (1, len(str2)+1):
                    if str1[i-1]==str2[j-1]:
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                        
            return printSCS (dp, str1, str2)
            
        
        def printSCS(dp, str1, str2):
            
            pstr1 = len(str1)
            pstr2 = len(str2)
            
            string = ""
            
            while pstr1*pstr2 !=0:
                if str1[pstr1-1] == str2[pstr2-1]:
                    string += str1[pstr1-1]
                    pstr1-=1
                    pstr2-=1
                elif dp[pstr1][pstr2-1] > dp[pstr1-1][pstr2]:
                    string+= str2[pstr2-1]
                    pstr2-=1
                else:
                    string +=str1[pstr1-1]
                    pstr1-=1
                    
            while pstr1:
                string+=str1[pstr1-1]
                pstr1-=1
            while pstr2:
                string+=str2[pstr2-1]
                pstr2-=1
                
            return string[::-1]
        
        return longestCommonSubsequence(str1, str2)
        
        
print(Solution().shortestCommonSupersequence("abac", "cab"))
print(Solution().shortestCommonSupersequence("AGGTAB","GXTXAYB"))