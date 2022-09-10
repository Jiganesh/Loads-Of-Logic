# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:

    # Runtime: 57 ms, faster than 20.82% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
    # Memory Usage: 13.8 MB, less than 60.15% of Python3 online submissions for Check If a Word Occurs As a Prefix of Any Word in a Sentence.
    
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
    
        for ind, word in enumerate(sentence.split(" ")):
            if word.startswith(searchWord): return ind+1
            
        return -1
