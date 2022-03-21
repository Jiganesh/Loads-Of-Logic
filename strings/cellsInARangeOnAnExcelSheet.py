# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution(object):
    
    
    # Submitted by Jiganesh 
    
    # TC : O(N*M)
    # SC : O(N*M)
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        startingLetter, endingLetter = s.split(":")
        startLetter = ord(startingLetter[0])
        endLetter = ord(endingLetter[0])
        startcell = int(startingLetter[-1])
        endcell = int(endingLetter[-1])
        
        result = []
        
        for i in range(startLetter, endLetter+1):
            for j in range(startcell, endcell+1):
                result.append(chr(i)+str(j))
        
        return result
    
    # One liner
    
    # return [ chr(i)+str(k) for i in range(ord(s[0]), ord(s[2])+1) for j in range(int(s[1]), int(s[3])+1) ]
                        