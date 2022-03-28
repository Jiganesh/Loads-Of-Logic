class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):

        def longestCommonSubsequence (str1, str2):
            dp= [[0]*(len(str2)+1) for i in range (len(str1)+1)]
            
            for i in range (1,len(str1)+1):
                for j in range (1, len(str2)+1):
                    if str1[i-1]==str2[j-1]:
                        dp[i][j] = 1+dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                        
            for i in dp : print(*i)
            
            res = dp[-1][-1]
            print(printSCS (dp, str1, str2))
            return  res
        
        def printSCS(dp, str1, str2):
            
            pstr1 = len(str1)
            pstr2 = len(str2)
            
            string = ""
            
            while pstr1*pstr2 !=0:
                dp[pstr1][pstr2]="*"
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
                
            for i in dp : print(*i)
                
            return string[::-1]
                                        
            
        commonInBothStrings = longestCommonSubsequence(str1, str2)
        letterDifferentInBothStrings = len(str1)-commonInBothStrings + len(str2)-commonInBothStrings
        subsequence= commonInBothStrings+letterDifferentInBothStrings
        return subsequence
        
        
print(Solution().shortestCommonSupersequence("abac", "cab"))
print(Solution().shortestCommonSupersequence("AGGTAB","GXTXAYB"))