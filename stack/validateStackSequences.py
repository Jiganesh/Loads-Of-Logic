# https://leetcode.com/problems/validate-stack-sequences/

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        pointer_on_popped = 0
        pointer_on_pushed = 0
        stack = []

        while pointer_on_pushed < len(pushed) or (stack and  popped[pointer_on_popped] == stack[-1]):
            if stack and popped[pointer_on_popped] == stack[-1]:
                stack.pop()
                pointer_on_popped+=1
            else:
                stack.append(pushed[pointer_on_pushed])
                pointer_on_pushed+=1


        return pointer_on_popped >= len(popped)