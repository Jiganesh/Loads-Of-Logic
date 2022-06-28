
from typing import  List

class Solution:
    # Runtime: 44 ms, faster than 71.28% of Python3 online submissions for Unique Morse Code Words.
    # Memory Usage: 13.8 MB, less than 72.71% of Python3 online submissions for Unique Morse Code Words.
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse_code  = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabets = list("abcdefghijklmnopqrstuvwxyz")
        
        dictionary = dict(zip(alphabets, morse_code))
        
        result = set()
        for word in words:
            code = "".join([dictionary[j] for j in word])
            result.add(code)
            
        return len(result)