# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import defaultdict

class Solution:

    # Runtime: 153 ms, faster than 63.07% of Python3 online submissions for First Unique Character in a String.
    # Memory Usage: 14 MB, less than 99.75% of Python3 online submissions for First Unique Character in a String.

    def firstUniqChar(self, s: str) -> int:
        
        dictionary = defaultdict(int)
        for i in s :
            dictionary[i]+=1
            
        for ind, i in enumerate(s):
            if dictionary[i]==1:
                return ind
        return -1