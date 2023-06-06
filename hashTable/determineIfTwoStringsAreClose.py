# https://leetcode.com/problems/determine-if-two-strings-are-close/

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        word1_ch_count = Counter(word1)
        word2_ch_count = Counter(word2)
        
        freq_word1_count = Counter(word1_ch_count.values())
        freq_word2_count = Counter(word2_ch_count.values())

        word1_set = set(word1)
        word2_set = set(word2)

        return freq_word1_count == freq_word2_count and word1_set == word2_set