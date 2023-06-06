# https://leetcode.com/problems/basic-calculator-ii/

class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        curr_num = 0
        op = ""
        n = len(s)

        for i in range (n):
            ch = s[i]

            if ch in "1234567890":
                curr_num  = curr_num * 10 + int(ch)

            if (ch != " " and ch in "+-/*") or (i == n-1) :
                if op == "+":
                    stack.append(curr_num)
                elif op == "-":
                    stack.append(-curr_num)
                elif op == "/":
                    num = stack.pop() // curr_num
                    stack.append(num)
                elif op == "*":
                    num = stack.pop() * curr_num
                    stack.append(num)
                else:
                    stack.append(curr_num)

                op = ch
                curr_num = 0


        result = 0
        while stack:
            result += stack.pop()

        return result
 