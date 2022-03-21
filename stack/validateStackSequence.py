# https://leetcode.com/problems/validate-stack-sequences/

class Solution(object):
    
    # TC : O(N)
    # SC : O(N)
    
    # Runtime: 56 ms, faster than 90.20% of Python online submissions for Validate Stack Sequences.
    # Memory Usage: 13.6 MB, less than 32.88% of Python online submissions for Validate Stack Sequences.
    
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack= []
        pointer = 0
        
        for elementToBePushed in pushed :
            
            while stack and stack[-1]==popped[pointer]:
                stack.pop()
                pointer+=1
                
            stack.append(elementToBePushed)
                
        while stack and stack[-1]==popped[pointer]:
            stack.pop()
            pointer+=1
                
        return not stack
            
            
                
        