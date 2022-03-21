# https://leetcode.com/problems/simplify-path/

class Solution(object):
    
    # TC : O(N)
    # SC : O(N)
    
    # Runtime: 22 ms, faster than 80.23% of Python online submissions for Simplify Path.
    # Memory Usage: 13.5 MB, less than 60.17% of Python online submissions for Simplify Path.
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathArray = path.split("/")
        stack =[]
        for i in pathArray:
            if i ==".":
                continue
            elif stack and  i== "..":
                stack.pop()
            elif i != ".."  and i :
                stack.append(i)
                
        return "/"+"/".join(stack)