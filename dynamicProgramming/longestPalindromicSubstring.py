# https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    
    
    # Submitted  by Jiganesh
    
    # TC : O(N^2)
    # SC : O(N^2)
    
    # Runtime: 904 ms, faster than 75.54% of Python online submissions for Longest Palindromic Substring.
    # Memory Usage: 13.4 MB, less than 87.78% of Python online submissions for Longest Palindromic Substring.
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def palindromeRange (point1, point2):
            
            while point1>=0 and point2 <=len(s)-1:
                if s[point1]!= s[point2]:
                    break
                point1-=1
                point2+=1
                
            return [point1+1, point2]
        
        largest = [0,1]
        
        for i in range(len(s)):
            
            even = palindromeRange(i-1, i)
            odd = palindromeRange (i-1, i+1)
            
            current = max(even ,odd , key = lambda x : x[1]-x[0])
            largest = max(current , largest,  key = lambda x : x[1]-x[0])
            
        return s[largest[0]:largest[1]]
    