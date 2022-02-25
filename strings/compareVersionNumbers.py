# https://leetcode.com/problems/compare-version-numbers/
class Solution(object):
    
    # Submitted by @Jiganesh
     
    # TC : O(N)
    # SC : O(N)
    
    # Runtime: 22 ms, faster than 58.55% of Python online submissions for Compare Version Numbers.
    # Memory Usage: 13.6 MB, less than 21.71% of Python online submissions for Compare Version Numbers.
    
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        a = version1.split(".")
        b = version2.split(".")
        
        for i in range(max(len(a), len(b))):
            
            vala = i< len(a) and int(a[i]) or 0
            valb = i< len(b) and int(b[i]) or 0
            
            if vala<valb : return -1
            elif vala>valb : return 1
            
        return 0
    
    # TC : O(N)
    # SC : O(1)
    def compareVersion(self, version1, version2):
        
        
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        i = 0
        j = 0
        
        while i< len(version1) or j< len(version2):
            
            val1 = 0
            while i< len(version1) and version1[i]!=".":
                val1 = val1*10 + int(version1[i])
                i+=1
            
            val2 = 0
            while j< len(version2) and version2[j]!=".":
                val2 = val2*10 + int(version2[j])
                j+=1
            
            if val1<val2 : return -1
            elif val1>val2 : return 1
            
            i+=1
            j+=1