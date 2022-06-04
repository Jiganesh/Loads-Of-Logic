# https://leetcode.com/problems/find-common-characters/

from collections import Counter


class Solution:
    # Runtime: 63 ms, faster than 65.96% of Python3 online submissions for Find Common Characters.
    # Memory Usage: 14 MB, less than 29.86% of Python3 online submissions for Find Common Characters.
    def commonChars(self, words) :
        
        array = [float('inf')]*27
        for i in words:
            d = Counter(i)
            for j in range(len(array)):
                letter = chr(j+96)
                array[j] = min(array[j], d[letter])
                
        result = []
        for i in range(len(array)):
            letter = chr(i+96)
            result +=[letter]*array[i]
            
        return result