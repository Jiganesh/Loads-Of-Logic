# https://leetcode.com/problem
# s/check-if-the-sentence-is-pangram/

class Solution:
    
    def checkIfPangram(self, sentence: str) -> bool:
        
        check_bit = 0
        
        for ch in sentence:
            ind = ord(ch)-ord("a")
            check_bit |= 1 << ind
            
        return check_bit == 0X03FFFFFF