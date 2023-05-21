# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution:
    def minLength(self, s: str) -> int:
        
        stack = []
        
        def check (stack):
            return  (stack[-2] == "A" and stack[-1] =="B") or (stack[-2] == "C" and stack[-1] =="D")
        
        for i in s:
            stack.append(i)
            while len(stack) > 1 and check(stack):
                stack.pop()
                stack.pop()
                
        return len(stack)
        