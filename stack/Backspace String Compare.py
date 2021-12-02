#https://leetcode.com/problems/backspace-string-compare/
#Runtime: 20 ms, faster than 99.27% of Python3 online submissions for Backspace String Compare.
#Memory Usage: 14.1 MB, less than 93.90% of Python3 online submissions for Backspace String Compare.

#(Asked in Amazon SDE1 interview)

class Solution:
    def soln(self, lst: str)-> list:
        op=[]
        for i in lst:
            if i=="#" and op:
               op.pop()
            elif i!="#":
                op.append(i)        
        return op
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.soln(s)==self.soln(t)
