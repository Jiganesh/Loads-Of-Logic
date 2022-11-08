# https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []

        for ch in s:
            stack.append(ch)

            while len(stack) >= 2 and stack[-1].islower() and stack[-2].isupper() and stack[-1].lower()==stack[-2].lower():
                stack.pop()
                stack.pop()
            while len(stack) >= 2 and stack[-1].isupper() and stack[-2].islower() and stack[-1].lower()==stack[-2].lower():
                stack.pop()
                stack.pop()

        return "".join(stack)