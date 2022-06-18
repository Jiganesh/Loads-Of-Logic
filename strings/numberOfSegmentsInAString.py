# https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution:
    
    # Runtime: 47 ms, faster than 39.49% of Python3 online submissions for Number of Segments in a String.
    # Memory Usage: 13.9 MB, less than 49.08% of Python3 online submissions for Number of Segments in a String.
    
    def countSegments(self, s: str) -> int:
        return  len([i for i in s.split(" ") if i])
        