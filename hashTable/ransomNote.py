# https://leetcode.com/problems/ransom-note/

from collections import Counter

class Solution:
    # Runtime: 92 ms, faster than 50.51% of Python3 online submissions for Ransom Note.
    # Memory Usage: 14.1 MB, less than 94.49% of Python3 online submissions for Ransom Note.
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        
        for key, value in ransomNote.items():
            if magazine[key] < value:
                return False
            
        return True