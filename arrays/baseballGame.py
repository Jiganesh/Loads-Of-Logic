# https://leetcode.com/problems/baseball-game/

class Solution:
    
    # Runtime: 52 ms, faster than 63.73% of Python3 online submissions for Baseball Game.
    # Memory Usage: 14.2 MB, less than 34.49% of Python3 online submissions for Baseball Game.
    
    def calPoints(self, ops):
        
        
        result = []
        
        for i in ops:
            
            if i == "C":
                result.pop()
            elif i == "D":
                result.append(result[-1]*2)
            elif i == "+":
                result.append(result[-2]+result[-1])
            else:
                result.append(int(i))
                
        return sum (result)