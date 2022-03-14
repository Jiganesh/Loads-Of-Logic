# https://leetcode.com/problems/valid-parentheses/

# Runtime: 24 ms, faster than 96.14% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.4 MB, less than 36.61% of Python3 online submissions for Valid Parentheses.

class Solution:
    
    # Submitted by Varun
    
    def isValid(self, s: str) -> bool:
        from collections import deque
        mapp={'}':'{', ')':'(', ']':'['}
        stack=deque()
        for i in s:
            if i in mapp.values():
                stack.append(i)
            elif stack and mapp[i]==stack[-1]:
                stack.pop()
            else:
                return False
        
        return len(stack)==0
    
    # Submitted by Jiganesh
    
    def isValid(self, s: str) -> bool:

        dic = {"}":"{", "]":"[", ")":"("}
        stack = []
        
        for i in s:
            if stack and i in dic and stack[-1] == dic[i]:
                stack.pop()
            else :
                stack.append(i)
                
        return len(stack)==0
    