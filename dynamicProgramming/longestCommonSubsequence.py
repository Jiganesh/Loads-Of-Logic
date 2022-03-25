# https://leetcode.com/problems/longest-common-subsequence/


class Solution(object):
    
    # TLE
    
    # Plain Recursion
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """        
        def helper(text1,text2, pointerText1, pointerText2):
            
            if (pointerText1<0 or pointerText2<0):
                return 0
            
            if text1[pointerText1]==text2[pointerText2]:
                return 1+ helper(text1, text2, pointerText1-1, pointerText2-1)
            else :
                return max(helper(text1,text2,pointerText1-1,pointerText2), helper(text1, text2, pointerText1, pointerText2-1))
        
        
        return helper(text1, text2, len(text1)-1, len(text2)-1)
    
    # Memoized Version of Above
    
    # Runtime: 930 ms, faster than 19.39% of Python online submissions for Longest Common Subsequence.
    # Memory Usage: 23.4 MB, less than 16.88% of Python online submissions for Longest Common Subsequence.
    
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = [[-1] * (len(text2)+1) for i in range(len(text1)+1)]

        def helper(text1, text2, pointerText1, pointerText2):

            if (pointerText1 < 0 or pointerText2 < 0):
                return 0

            if dp[pointerText1][pointerText2] != -1:
                return dp[pointerText1][pointerText2]

            res = 0
            if text1[pointerText1] == text2[pointerText2]:
                res = 1 + helper(text1, text2, pointerText1-1, pointerText2-1)
            else:
                res = max(helper(text1, text2, pointerText1-1, pointerText2),
                          helper(text1, text2, pointerText1, pointerText2-1))

            dp[pointerText1][pointerText2] = res
            return res
        
        return helper(text1, text2, len(text1)-1, len(text2)-1)
    
    
    
    # Runtime: 406 ms, faster than 51.49% of Python online submissions for Longest Common Subsequence.
    # Memory Usage: 21.2 MB, less than 91.06% of Python online submissions for Longest Common Subsequence.
    
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """        
        dp = [[0] * (len(text1)+1) for i in range (len(text2)+1)]
        
        for pointerText2 in range (1,len(text2)+1):
            for pointerText1 in range (1,len(text1)+1):
                if text1[pointerText1-1] == text2[pointerText2-1]:
                    dp[pointerText2][pointerText1] = 1 + dp[pointerText2-1][pointerText1-1]
                else:
                    dp[pointerText2][pointerText1] = max(dp[pointerText2-1][pointerText1], dp[pointerText2][pointerText1-1])
                    
        return dp[-1][-1]


print(Solution().longestCommonSubsequence("abcde", "ace")) #3 
print(Solution().longestCommonSubsequence("abc", "def")) #0
print(Solution().longestCommonSubsequence("sfd", "sfdasdgsdf")) #3

