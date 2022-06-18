# https://leetcode.com/problems/longest-word-in-dictionary/

class Solution:
    
    # Runtime: 239 ms, faster than 28.22% of Python3 online submissions for Longest Word in Dictionary.
    # Memory Usage: 14.4 MB, less than 71.32% of Python3 online submissions for Longest Word in Dictionary.
    
    # TC : O(N*S)
    # SC : O(N)
    def longestWord(self, words):
        
        
        max_word = ""
        words = set(words)
        
        for i in words:
            
            for pointer in range (len(i)):
                if i[:pointer+1] not in words:
                    break
            else:
                
                
                if len(max_word) < len(i):
                    max_word = i
                elif len(max_word)==len(i):
                    max_word = min (i, max_word)
                    
                    
                # ABOVE FOUR LINES CAN ALSO BE WRITTEN AS 
                # if len(max_word) > len(i) or  i < max_word: max_word = word
                    
        return max_word
        
        