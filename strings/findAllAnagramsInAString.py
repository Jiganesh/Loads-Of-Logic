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
        
        for i in p:
            if i in dictP : dictP[i]+=1
            else :dictP[i]=1
            
        i = 0 
        
        result=[]
        
        while i<lens:
            dictS[s[i]]+=1
            if i>=lenp :
                dictS[s[i-lenp]]-=1
                
            for j in dictP:
                if j not in dictS or (j in dictS and dictS[j] != dictP[j]):
                    break   
            else:
                result.append(i-lenp+1)
            
            i+=1
        return result
            
print(Solution().findAnagrams("cbaebabacd", "abc"))
print(Solution().findAnagrams("abab", "ab"))
print(Solution().findAnagrams("aa", "bb"))

