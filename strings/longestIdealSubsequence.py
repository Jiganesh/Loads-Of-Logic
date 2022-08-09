# https://leetcode.com/problems/longest-ideal-subsequence/

class Solution:
    # Runtime: 717 ms, faster than 100.00% of Python3 online submissions for Longest Ideal Subsequence.
    # Memory Usage: 14.8 MB, less than 60.00% of Python3 online submissions for Longest Ideal Subsequence.
    def longestIdealString(self, s: str, k: int) -> int:
        
        dp = [0] * 26
        
        for char in s:
            
            char_position = ord(char)-ord("a")
            
            left = max(0, char_position-k)
            right = min(26, char_position+k+1)
            
            dp[char_position] = max(dp[left: right])+1
            
        return max(dp)