# https://leetcode.com/problems/camelcase-matching/


from typing import List

class Solution:
    
    # Runtime: 38 ms, faster than 77.81% of Python3 online submissions for Camelcase Matching.
    # Memory Usage: 13.9 MB, less than 33.15% of Python3 online submissions for Camelcase Matching.
    
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        
        def check_subsequence (word):
            
            pointer_pattern = 0
            
            for pointer_word in range (len(word)):
                
                if pointer_pattern < len(pattern) and word[pointer_word]==pattern[pointer_pattern]:
                    pointer_pattern+=1
                    pointer_word+=1
                    
                elif word[pointer_word].isupper():
                    return False

            # if pointer_pattern > len(pattern)-1 means all alphabets in pattern are covered and it is subsequence                                
            return pointer_pattern>len(pattern)-1 
                
        return [check_subsequence(word) for word in queries]
                
            

            
