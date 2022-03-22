class Solution(object):
    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        
        greedy = ['a']*n
        
        pointer = len(greedy)-1
        k = k-n
        
        c = "abcdefghijklmnopqrstuvwxyz"
        
        
        while k :            
            if k >= 26:
                k-=25
                greedy[pointer]='z'
            else :
                greedy[pointer] = c[k]
                k=0
                
            pointer -=1
            
        return "".join(greedy)