# https://leetcode.com/problems/valid-anagram/

class Solution:
    # Runtime: 120 ms, faster than 8.01% of Python3 online submissions for Valid Anagram.
    # Memory Usage: 14.4 MB, less than 96.92% of Python3 online submissions for Valid Anagram.
    
    def isAnagram(self, s: str, t: str) -> bool:
        
        character = [0]*26
        
        for ch in s:
            index = ord(ch)-ord("a")
            character[index]+=1
            
        for ch in t:
            index = ord(ch)-ord("a")
            character[index]-=1
        
        
        for i in character:
            if i!=0:
                return False
            
        return True
        