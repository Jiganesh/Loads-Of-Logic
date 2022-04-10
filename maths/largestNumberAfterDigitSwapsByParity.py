# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

class Solution:
    
    # Brute Force [Accepted]
    def largestInteger(self, num: int) -> int:
        
        s = list(str(num)) # Converting num to list for easy manipulations
        
        # Loops through all numbers and just check the given condition
        for i in range (len(s)):
            for j in range (i+1,len(s)):
                
                # makes sense to swap when the number ahead is smaller than number behind cause we want greater number
                # AND operator helps to check parity
                
                if int(s[i]) < int(s[j]) and int(s[i])&1==int(s[j])&1:
                    s[i],s[j] =s[j],s[i]
                    
        # returning Number
        return "".join(s)
    
    
    # Optimized Approach
    
    # TC : O(N log N)
    # SC : O(N)
    
    # Runtime: 39 ms, faster than 60.00% of Python3 online submissions for Largest Number After Digit Swaps by Parity.
    # Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Largest Number After Digit Swaps by Parity.

    def largestInteger(self, num: int) -> int:
        
        even , odd = [], []
        
        result = list(str(num))
        
        while num:
        
            val = num%10
            if val&1: odd.append(val)
            else: even.append(val)
            num//=10
                
        odd.sort(reverse = True)
        even.sort(reverse = True)
        
        for i in range (len(result)-1, -1, -1):
            if int(result[i])&1:
                result[i]= odd.pop()
            else :
                result[i]= even.pop()
            
        return ''.join(map(str, result))