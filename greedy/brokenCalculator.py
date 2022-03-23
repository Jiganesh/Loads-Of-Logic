# https://leetcode.com/problems/broken-calculator/

class Solution(object):

    # Runtime: 20 ms, faster than 87.50% of Python online submissions for Broken Calculator.
    # Memory Usage: 13.2 MB, less than 100.00% of Python online submissions for Broken Calculator.
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        
        count =0
        
        while target > startValue:
            
            if target%2==0 : 
                target = target//2
            else :
                target +=1
                
            count+=1
            
        count += (startValue-target)
        return count
                
                
                
        