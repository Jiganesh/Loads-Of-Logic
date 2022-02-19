class Solution(object):
    
    # Runtime: 30 ms, faster than 81.82% of Python online submissions for Remove K Digits.    
    # Memory Usage: 13.7 MB, less than 89.67% of Python online submissions for Remove K Digits.

    # APPROACH : STACK 
    # IDEA : 1234, k= 2 => when numbers are in increasing order we need to delete last digits 
    # 4321 , k = 2 ==> when numbers are in decreasing order, we need to delete first digits
    # so, we need to preserve increasing sequence and remove decreasing sequence 
    
    # LOGIC #
    #	1. First think in terms of stack
    #	2. push num into stack IF num it is greater than top of stack
    #	3. ELSE pop all elements less than num

    # TIME COMPLEXICITY : O(N) 
    # SPACE COMPLEXICITY : O(N) 
    
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        
        for i in num :
            while stack and i <stack[-1] and k:
                stack.pop()
                k-=1
                continue
                
            
            # Elimination of leading Zeroes 
            if stack or i!="0": 
                stack.append(i)
            
        
        if k :
            stack= stack[:-k]
            
        return "".join(stack) if stack else "0"