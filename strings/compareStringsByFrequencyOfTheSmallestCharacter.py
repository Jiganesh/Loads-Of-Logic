# https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

class Solution:    
    
    # Runtime: 982 ms, faster than 7.37% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
    # Memory Usage: 14.8 MB, less than 28.53% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def smallestCount(word):
            word = sorted(word)
            smallestChar = word[0]
            count = 0
            for j in word:
                if j== smallestChar: count+=1
                else : break
            return count
        
        queryF=[smallestCount(i) for i in queries]
        wordsF=[smallestCount(i) for i in words]
            
        result = [0]* len(queries)
        
        for indexi, i in enumerate(queryF):
            for indexj , j in enumerate(wordsF):
                if i< j:
                    result[indexi]+=1        
        return result
    
    
    # Few Optimizations
    
    #Runtime: 576 ms, faster than 26.28% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
    # Memory Usage: 14.7 MB, less than 28.53% of Python3 online submissions for Compare Strings by Frequency of the Smallest Character.
    
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def smallestCount(word):
            count = 0
            currentsmall = word[0]
            for i in word:
                if currentsmall>i:
                    count=1
                    currentsmall=i
                elif currentsmall==i:
                    count+=1
            return count
        
        queryF=[smallestCount(i) for i in queries]
        wordsF=[smallestCount(i) for i in words]
            
        result = [0]* len(queries)
        
        for indexi, i in enumerate(queryF):
            for j in wordsF:
                if i< j:
                    result[indexi]+=1        
        return result
        