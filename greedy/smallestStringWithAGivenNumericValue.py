# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution(object):
    
    # TC : O(N)
    # SC : O(N)
    
    # Runtime: 312 ms, faster than 76.92% of Python online submissions for Smallest String With A Given Numeric Value.
    # Memory Usage: 15 MB, less than 53.85% of Python online submissions for Smallest String With A Given Numeric Value.
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        greedy = ['a']*n
        
        pointer = len(greedy)-1
        k = k-n
    
        while k :            
            if k >= 26:
                k-=25
                greedy[pointer]='z'
            else :
                greedy[pointer] = chr(96+k)
                k=0
                
            pointer -=1
            
        return "".join(greedy)