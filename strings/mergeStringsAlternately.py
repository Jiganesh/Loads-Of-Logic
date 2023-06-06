# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        p1 = 0
        p2 = 0

        n1 = len(word1)
        n2 = len(word2)

        while p1 < n1 or p2 < n2:
            if p1 < n1:
                result += word1[p1]
                p1+=1
            if p2 < n2:
                result += word2[p2]
                p2+=1
        return result
            
