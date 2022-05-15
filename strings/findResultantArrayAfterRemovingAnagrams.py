# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/submissions/

class Solution:
    
    # Runtime: 87 ms, faster than 85.71% of Python3 online submissions for Find Resultant Array After Removing Anagrams.
    # Memory Usage: 14 MB, less than 42.86% of Python3 online submissions for Find Resultant Array After Removing Anagrams.
    
    def removeAnagrams(self, words) :
        
        
        def anagram (truePointer, runningPointer):
            array = [0]*26
            for i in words[truePointer]:
                array[ord(i)-ord("a")]+=1
                
            for i in words[runningPointer]:
                array[ord(i)-ord("a")]-=1
                
            return not any(array)
                
                
            
        truePointer = 0
        runningPointer = 0
        
        while runningPointer< len(words):
            
            if truePointer!= runningPointer and anagram(truePointer, runningPointer) : 
                words[runningPointer] = None
            else:
                truePointer = runningPointer
            
            runningPointer+=1
            
        return [i for i in words if i]
    
    
    # Runtime: 55 ms, faster than 100.00% of Python3 online submissions for Find Resultant Array After Removing Anagrams.
    # Memory Usage: 14 MB, less than 42.86% of Python3 online submissions for Find Resultant Array After Removing Anagrams.
    
    def removeAnagrams(self, words) :
        
        
        stack = []
        result = []
        for i in words:
            sw = "".join(sorted(i))
            if stack and stack[-1]==sw:
                continue
            else :
                stack.append(sw)
                result.append(i)
        return result
            
            
            