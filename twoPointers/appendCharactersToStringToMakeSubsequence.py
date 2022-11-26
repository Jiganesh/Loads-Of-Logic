# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_pointer = 0
        t_pointer = 0
        
        matched_letters = 0
        
        s_length =len(s)
        t_length =len(t)
        
        while t_pointer < t_length and s_pointer < s_length:
            
            if s[s_pointer]==t[t_pointer]:
                matched_letters+=1
                
                s_pointer+=1
                t_pointer+=1
            else:
                s_pointer += 1
        
        return t_length-matched_letters