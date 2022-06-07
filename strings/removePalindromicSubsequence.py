# https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    # Runtime: 51 ms, faster than 19.89% of Python3 online submissions for Remove Palindromic Subsequences.
    # Memory Usage: 13.8 MB, less than 53.87% of Python3 online submissions for Remove Palindromic Subsequences.
    def removePalindromeSub(self, s: str) -> int:
        
        # If string is empyty we dont need to delete anything 
        # If whole string is palindrome we can delete it in one go
        # As we need to delete subsequence we can delete all "a"s and "b"s as it will be palindromic subsequence
        
        return 2 - (s==s[::-1]) - (s=="") # Inspired by lee's solution as True statement will be turning into One's
    