# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:  

        stack1 = list(num1)
        stack2 = list(num2)
        carry = 0

        result = deque([])

        while stack1 or stack2 or carry:
            digit1 = int(stack1.pop()) if stack1 else 0
            digit2 = int(stack2.pop()) if stack2 else 0

            val = (digit1+digit2+carry) % 10
            result.appendleft(str(val))
            carry = (digit1 + digit2 + carry)//10

        return "".join(result)
