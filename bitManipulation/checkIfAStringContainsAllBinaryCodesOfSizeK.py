# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
class Solution(object):
    
    # Runtime: 1049 ms, faster than 11.11% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
    # Memory Usage: 54 MB, less than 11.11% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
    
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        bit_array = set([int(s[i:i+k],2) for i in range (len(s)-k+1)])
        
        for i in range (2**k):
            if i not in bit_array:
                return False
            
        return True
    
    # Runtime: 308 ms, faster than 81.48% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
    # Memory Usage: 45.1 MB, less than 29.63% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
    
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        return len(set(s[i:i+k] for i in range (len(s)-k+1))) == 2**k

    

