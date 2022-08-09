class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        dp = [0] * 26
        
        for char in s:
            
            char_position = ord(char)-ord("a")
            
            left = max(0, char_position-k)
            right = min(26, char_position+k+1)
            
            dp[char_position] = max(dp[left: right])+1
            
        return max(dp)