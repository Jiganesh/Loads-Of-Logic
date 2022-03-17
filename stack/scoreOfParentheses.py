# https://leetcode.com/problems/score-of-parentheses/
# Solution : https://www.youtube.com/watch?v=jfmJusJ0qKM&ab_channel=NickWhite
class Solution(object):
    
    # TC : O(N)
    # SC : O(N)
    
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = []
        score = 0
        
        for i in s :
            if i =="(":
                stack.append(score)
                score = 0
            else :
                score = stack.pop()+ max(score*2, 1)
        return score
    
                