# https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

class Solution:
    
    # Runtime: 37 ms, faster than 84.07% of Python3 online submissions for Smallest Value of the Rearranged Number.
    # Memory Usage: 13.9 MB, less than 24.12% of Python3 online submissions for Smallest Value of the Rearranged Number.
    def smallestNumber(self, num: int) -> int:
    
        negative = -1 if num<0 else 1
        
        num = negative * num
        nums_str = list(str(num))
        
        array = [negative * int(i) for i in nums_str]
        array.sort()
        
        # [0 1 3] below block will return [1 0 3]
        # [0 -3 -1] below block will return [-3 0 -1]
        
        # Its not a bug It's a feature XD
        
        for i in range(len(array)):
            if array[0]==0 and array[i]:
                array[0],array[i]= array[i], array[0]
                break
                
                
                
        number = "".join(map(str,[negative*i for i in array]))
        number = negative * int(number)
        
        return number
                
                
    def smallestNumber(self, a):
        s = sorted(str(abs(a)))
        if a <= 0:
            return -int(''.join(s[::-1]))
        i = next(i for i,a in enumerate(s) if a > '0')
        s[i], s[0] = s[0], s[i]
        return int(''.join(s))
                
        