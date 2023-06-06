# https://leetcode.com/problems/delete-characters-to-make-fancy-string/

class Solution:
    def makeFancyString(self, s: str) -> str:
        
        stack = []

        for ch in s:

            while len(stack)>=2 and stack[-1] == stack[-2] == ch:
                stack.pop()
            stack.append(ch)

        return "".join(stack)