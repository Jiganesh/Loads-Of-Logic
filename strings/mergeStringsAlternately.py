# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        answer = []
        while i < len(word1) and j < len(word2):
            answer += word1[i]
            answer += word2[j]
            i+=1
            j+=1
        if i == len(word1):
            answer += word2[j:]
        else:
            answer += word1[i:]

        return "".join(answer)
