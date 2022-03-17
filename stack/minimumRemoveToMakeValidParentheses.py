# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution(object):
    
    # Submitted by Jiganesh
    
    # TC : O(N)
    # SC : O(N)
    
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack =[]
        result = []
        
        for j in range(len(s)):
            i = s[j]
            if i == ")" or i =="(" :
                if stack and stack[-1][0]=="(" and i==")":
                    stack.pop()
                else :
                    stack.append([i,j])
                    
        p=0        
        for i in range (len(s)):
            if p< len(stack) and stack[p][1]== i:
                p+=1
                continue
            else :
                result.append(s[i])
        return "".join(result)