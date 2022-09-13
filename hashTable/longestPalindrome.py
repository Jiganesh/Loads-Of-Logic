# https://leetcode.com/problems/longest-palindrome/


from collections import Counter

class Solution:
    
    # Runtime: 76 ms, faster than 6.25% of Python3 online submissions for Longest Palindrome.
    # Memory Usage: 14 MB, less than 22.32% of Python3 online submissions for Longest Palindrome.
    
    def longestPalindrome(self, s: str) -> int:
        
        even_length_of_palindrome = 0
        lookup = Counter(s)
        odd_ch = 0
        
        for ch, count in lookup.items():
            
            even_length_of_palindrome += count//2
            if count%2:
                odd_ch = 1
                
        return (even_length_of_palindrome*2) + odd_ch