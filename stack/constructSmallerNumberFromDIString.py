# https://leetcode.com/problems/construct-smallest-number-from-di-string/

class Solution:
    
    # Runtime: 33 ms, faster than 100.00% of Python3 online submissions for Construct Smallest Number From DI String.
    # Memory Usage: 13.9 MB, less than 75.00% of Python3 online submissions for Construct Smallest Number From DI String.
    
    def smallestNumber(self, pattern: str) -> str:
        
        pattern+='I'
        digit =1
        
        stack = []
        result = []
        
        for ch in pattern:
            
            stack.append(digit)
            digit+=1
            
            if ch =='I':
                while stack :
                    result.append(stack.pop())
                    
            
        return "".join(map(str, result))
                    