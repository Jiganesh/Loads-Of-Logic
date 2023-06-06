# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

class Solution:
    def minSteps(self, s: str, t: str) -> int:


        s_word_count = Counter(s)
        t_word_count = Counter(t)

        alphabets = "abcdefghijklmnopqrstuvwxyz"
        same_characters = 0
        
        for alph in alphabets:
            same_characters += min(s_word_count[alph], t_word_count[alph])

        return len(t) - same_characters