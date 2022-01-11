# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution(object):
    
    # TC : O(N)
    # SC : O(N)
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in s:
            if stack and stack[-1]== "(" and i== ")" :
                stack.pop()
            else:
                stack.append(i)

        return len(stack);
    
    # TC : O(N)
    # SC: O(1)
    
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        leftBrackets=rightBrackets=0
        for i in s:
            if i=="(": leftBrackets+=1
            elif i==")" and leftBrackets<=0 :rightBrackets+=1
            elif i==")" :leftBrackets-=1
        return leftBrackets+rightBrackets
    
print(Solution().minAddToMakeValid("())"))