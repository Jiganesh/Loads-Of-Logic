# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    
    # Runtime: 59 ms, faster than 88.52% of Python3 online submissions for Zigzag Conversion.
    # Memory Usage: 14.1 MB, less than 51.47% of Python3 online submissions for Zigzag Conversion.
    def convert(self, s: str, numRows: int) -> str:
        
        
        if numRows == 1 : return s 
        
        result = ""
        incrementer = 2 * (numRows-1)
        
        for rows in range (numRows):
            
            for index in range (rows, len(s), incrementer):
                
                result += s[index]
                
                if (rows>0 and rows< numRows-1 and index + (incrementer-2*rows) < len(s)):

                    result += s[index + incrementer-2*rows]
                    
        return result