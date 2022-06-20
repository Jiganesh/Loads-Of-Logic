# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution:
    
    
    # Optimized Approach
    
    # TC : O(N + Log N + N)
    # SC : O(N + 26)
    
    # Runtime: 44 ms, faster than 80.00% of Python3 online submissions for Greatest English Letter in Upper and Lower Case.
    # Memory Usage: 13.8 MB, less than 80.00% of Python3 online submissions for Greatest English Letter in Upper and Lower Case.
    def greatestLetter(self, s: str) -> str:
        
        words = set(s)
        result = [0]*26
        
        for i in words:
            upper_ch = i.upper()
            lower_ch = i.lower()
            if upper_ch in words and lower_ch in words:
                result[ord(lower_ch)-ord("a")] = 1
                
        end = 25
        while end >=0:
            if result[end]:
                return chr(end+65)
            end-=1
        return ""
                
                
        