# https://leetcode.com/problems/concatenated-words/ 
# Solution : https://leetcode.com/problems/concatenated-words/discuss/159348/Python-DFS-readable-solution

class Solution:
    
    # Runtime: 1377 ms, faster than 15.65% of Python3 online submissions for Concatenated Words.
    # Memory Usage: 27.6 MB, less than 65.31% of Python3 online submissions for Concatenated Words.
    
    def findAllConcatenatedWordsInADict(self, words) :

        words = set (words)

        def helper_dfs(word):
            
            for i in range(1,len(word)): #prefix must have one word so range (1, len(word))
                prefix = word[:i]
                suffix = word[i:]
                
                if prefix in words and suffix in words: #important
                    return True
                if prefix in words and helper_dfs(suffix):
                    return True
                if suffix in words and helper_dfs(prefix):
                    return True
                
        
        result = []
        for i in words:
            if helper_dfs(i):
                result.append(i)
                
        return result
    
    # memoization 
    
    # Runtime: 1152 ms, faster than 22.04% of Python3 online submissions for Concatenated Words.
    # Memory Usage: 27.6 MB, less than 57.79% of Python3 online submissions for Concatenated Words.
    
    def findAllConcatenatedWordsInADict(self, words):
       
        words = set (words)
        
        def helper_dfs(word):
                
            if word in memoization:
                return memoization[word]
            
            for i in range(1,len(word)): #prefix must have one word so range (1, len(word))
                prefix = word[:i]
                suffix = word[i:]
                
                
                
                if prefix in words and suffix in words: 
                    memoization[prefix]=True
                    memoization[suffix]=True
                    return True
                if prefix in words and helper_dfs(suffix):
                    memoization[prefix]=True
                    return True
               
            return False
 
        
        result = []
        for i in words:
            memoization ={} # don't forget clearing memoization table
            if helper_dfs(i):
                result.append(i)
                
        return result