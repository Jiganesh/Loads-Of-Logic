# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for ch in s:
            
            if ch == "]":

                letters = ""
                while stack and stack[-1] != "[" :
                    letters = stack.pop()+ letters
                stack.pop()

                
                number = ""
                while stack and stack[-1] in "1234567890":
                    print(number)
                    number = stack.pop() + number
                
                last = letters * int(number)
                stack.append(last)

            else:
                
                stack.append(ch)

        return "".join(stack)
    