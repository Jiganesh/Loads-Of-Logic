# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/
# Solution : https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/discuss/2454262/DP-vs.-Brute-Force

class Solution:
    
    # BruteForce Solution 
    # Constraint 1<= s.length <= 1000
    
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count =0
        while "01" in s:
            s = s.replace("01", "10")
            count+=1
        return count

    # Runtime: 72 ms, faster than 80.00% of Python3 online submissions for Time Needed to Rearrange a Binary String.
    # Memory Usage: 13.9 MB, less than 40.00% of Python3 online submissions for Time Needed to Rearrange a Binary String.
    
    def secondsToRemoveOccurrences(self, s: str) -> int:
        
        seconds = 0
        zeroes = 0
        
        for ch in s :
            zeroes += ch == "0"
            if ch == "1" and zeroes  > 0:
                seconds = max(seconds+1, zeroes)
                
        return seconds
                