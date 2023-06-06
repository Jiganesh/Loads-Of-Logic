# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def helper(expression):
            result = []
            N = len(expression)

            for ind in range (N):
                operator = expression[ind]
                if operator in "+-*":

                    left = helper(expression[:ind])
                    right = helper(expression[ind+1:])

                    for num1 in left:
                        for num2 in right:

                            if operator == "+":
                                result.append(num1 + num2)

                            if operator == "-":
                                result.append(num1 - num2)
                            
                            if operator == "*":
                                result.append(num1 * num2)

            if not result:
                result.append(int(expression))

            return result

        return helper(expression)
            



