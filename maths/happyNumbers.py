# https://leetcode.com/problems/happy-number/

class Solution(object):
    
    # Submitted by Jiiganesh
    
    
    # TC: O(N^2)
    # SC: O(1)
    
    # Runtime: 35 ms, faster than 40.60% of Python online submissions for Happy Number.
    # Memory Usage: 13.4 MB, less than 35.81% of Python online submissions for Happy Number.
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashset = set()
        
        while n!=1:
            
            num =0
            while n:
                num+=(n%10)**2
                n=n//10
            n =num
            if n in hashset:
                return False
            else:
                hashset.add(n)
        return True