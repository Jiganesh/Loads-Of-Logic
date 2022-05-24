# https://leetcode.com/problems/daily-temperatures/

class Solution:
    # Runtime: 1408 ms, faster than 62.03% of Python3 online submissions for Daily Temperatures.
    # Memory Usage: 24.8 MB, less than 70.19% of Python3 online submissions for Daily Temperatures.
    def dailyTemperatures(self, temperatures) :
        
        
        stack = []
        
        output =[0]*len(temperatures)
        
        for  index , temperature in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]]<temperature :
                output[stack[-1]]= index-stack[-1]
                stack.pop()
                
            stack.append(index)
            
        return output