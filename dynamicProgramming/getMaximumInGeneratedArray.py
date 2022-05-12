# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    # Runtime: 30 ms, faster than 90.50% of Python3 online submissions for Get Maximum in Generated Array.
    # Memory Usage: 13.9 MB, less than 64.69% of Python3 online submissions for Get Maximum in Generated Array.
    def getMaximumGenerated(self, p: int) -> int:
        
        if p < 2 : return p
        
        n= [0]*(p+1)
        
        n[1]=1
        
        for i in range (p+1):
            
            if i%2==0:
                n[i]= n[i//2]
            else:
                n[i] = n[i//2] +n [i//2+1]
                
                
        return max(n)
                
        