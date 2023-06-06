# https://leetcode.com/problems/print-words-vertically
from typing import List

class Solution:
    def printVertically(self, s: str) -> List[str]:

        words = []
        max_len = 0

        for word in s.split(" "):
            word_length = len(word)
            max_len = max(word_length, max_len)
            words.append((word, word_length))

        result = []

        for col in range (max_len):
            vertical_word = ""
            for word , length in words:
                vertical_word += word[col] if col < length else " "

            result.append(vertical_word.rstrip())

        return result
            
            
