class Solution(object):
    
    # Runtime: 23 ms, faster than 68.57% of Python online submissions for String to Integer (atoi).00
    # Memory Usage: 13.5 MB, less than 79.83% of Python online submissions for String to Integer (atoi).
    
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,n=0,len(s)
        sign=1
        
        while i<n  and s[i]==" ": i+=1;
        
        if i< n and s[i] in "+-":
            sign = -1 if s[i]=="-" else 1
            i+=1
        
        res =0
        while i<n and s[i] in set ("0123456789"):
            res= res*10+int(s[i])
            i+=1
            
        if sign==-1:
            return max(-res,-2**31)
        else :
            return min(res, 2**31-1)