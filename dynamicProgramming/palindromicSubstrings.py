# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    
    # Runtime: 237 ms, faster than 39.93% of Python3 online submissions for Palindromic Substrings.
    # Memory Usage: 210.8 MB, less than 5.06% of Python3 online submissions for Palindromic Substrings.
    
    def countSubstrings(self, s: str) -> int:
        
        
        self.array = [i for i in s]
        
        def palindrome(start, end):
            
            while start>=0 and end < len(s):
                
                if s[start]==s[end]:
                    self.array.append(s[start:end+1])
                    start-=1
                    end+=1
                else:
                    break
                    
        for i in range (len(s)):
            palindrome(i-1, i+1)
            palindrome(i, i+1)
            
        return len(self.array)
            
            
            
        
            
        