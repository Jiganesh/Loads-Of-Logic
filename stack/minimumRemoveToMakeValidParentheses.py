# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# Solution : https://www.youtube.com/watch?v=thL70BR3yMA&ab_channel=NickWhite
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
    
    
    # Optimised Solution (Nick White)
    
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, result = [],[]
        openbrace =0
        for i in range(len(s)):
            character = s[i]
            if character =="(": 
                openbrace +=1
            
            if character ==")" : 
                if openbrace ==0  :
                    continue
                else: 
                    openbrace-=1
            
            stack.append(character)
            
        
        while stack:
            
            character = stack.pop()
            if character =="(" and openbrace:
                openbrace-=1
                continue
            
            result.append(character)
            
        return "".join(result[::-1])            
        
        
    
    
