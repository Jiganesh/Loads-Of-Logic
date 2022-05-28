# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

class Solution:
    
    # Runtime: 54 ms, faster than 75.00% of Python3 online submissions for Check if Number Has Equal Digit Count and Digit Value.
    # Memory Usage: 13.9 MB, less than 75.00% of Python3 online submissions for Check if Number Has Equal Digit Count and Digit Value.
    
    def digitCount(self, num: str) -> bool:
        
        lookup = [0]*len(num)
        
        for i in num:
            if int(i) < len(num) : lookup[int(i)]+=1
        
        return num == "".join(map(str, lookup))