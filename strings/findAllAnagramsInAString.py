# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution(object):
    
    
    # Submitted by Jiganesh
    
    # TC : O(LenP * LenS)
    # SC : O(LenP + LenS)
    
    
    # Runtime: 148 ms, faster than 50.90% of Python online submissions for Find All Anagrams in a String.
    # Memory Usage: 14.2 MB, less than 92.80% of Python online submissions for Find All Anagrams in a String.
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        dictP = {i : 0 for i in p}
        dictS = {i : 0 for i in s}
        
        lens, lenp = len(s), len(p)
        
        # storing frequency of all the characters in p in dictP

        for i in p:
            dictP[i]+=1
            
            
        startingPointer = 0 
        result=[]
        
        while startingPointer<lens:
            
            # after every iteration adding the next character
            dictS[s[startingPointer]]+=1
            
            # if the length by adding new character has increased from given length of p
            # deleting the previous character which will be at startingPointer-lenp
            # automatically given the frequency of all the elements in the window
            
            if startingPointer>=lenp :
                dictS[s[startingPointer-lenp]]-=1
                
                
            # checking if the window are valid anagrams by  comparing the frequency of all the elements in the window
            for j in dictP:
                
                # if some element is not present in the window then it is not valid anagram
                # if element is present then the frequecy must be equal
                # if frequency is not equal the also it is not valid anagram
                # hence break the loop
                if j not in dictS or (j in dictS and dictS[j] != dictP[j]):
                    break   
            else:
                
                # if the loop is not broken then it is a valid anagram
                # add the starting index to the result
                result.append(startingPointer-lenp+1)
            
            startingPointer+=1
            
        return result
            
print(Solution().findAnagrams("cbaebabacd", "abc"))
print(Solution().findAnagrams("abab", "ab"))
print(Solution().findAnagrams("aa", "bb"))

