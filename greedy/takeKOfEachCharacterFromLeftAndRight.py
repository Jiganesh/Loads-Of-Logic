# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/

from collections import Counter, defaultdict

class Solution:
    def takeCharacters(self, s: str, k: int) -> int: 

        lookup = Counter(s)
        maximum_allowed = {}
        for ch in "abc":
            if lookup[ch]-k >= 0:
                maximum_allowed[ch] =  lookup[ch]-k 
            else:
                return -1

        
        longest_substring_within_limits = 0
        left = 0
        curr_count = defaultdict(int)

        for ind, ch in enumerate(s):
            curr_count[ch] +=1
            while curr_count[ch] > maximum_allowed[ch]:
                
                ch_left = s[left]
                curr_count[ch_left]-=1
                left+=1

            current_substring = ind+1 - left
            longest_substring_within_limits = max(current_substring, longest_substring_within_limits)
        minimum_number = len(s) - longest_substring_within_limits
        return minimum_number
