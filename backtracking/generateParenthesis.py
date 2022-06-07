# https://leetcode.com/problems/generate-parentheses/

class Solution:
    
    # Runtime: 66 ms, faster than 19.90% of Python3 online submissions for Generate Parentheses.
    # Memory Usage: 14.2 MB, less than 76.32% of Python3 online submissions for Generate Parentheses.
    def generateParenthesis(self, n: int) :
    
        def helper(n, array = [], open=0, close=0, result=[]):
            
            if len(array)==n*2:
                result.append("".join(array))
                return 
                
            if open<n:
                array.append("(")
                helper(n, array, open+1, close, result)
                array.pop()
            if close<open:
                array.append(")")
                helper(n,array,open, close+1, result)
                array.pop()
            return result
        
        
        return helper(n)
    
    
    # Runtime: 59 ms, faster than 31.07% of Python3 online submissions for Generate Parentheses.
    # Memory Usage: 14.1 MB, less than 76.32% of Python3 online submissions for Generate Parentheses.
    def generateParenthesis(self, n: int) :
        def helper(n, string="", index=0 , open=0, close=0, result=[]):
            
            if index==n*2:
                result.append(string)
            if open<n:
                helper(n, string+"(", index+1, open+1, close, result)
            if close<open:
                helper(n, string+")", index+1, open, close+1, result)
            
            return result
        
        
        return helper(n)