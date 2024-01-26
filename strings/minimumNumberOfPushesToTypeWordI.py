https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/

class Solution:
    def minimumPushes(self, word: str) -> int:

        m = defaultdict(int)
        
        for ind, i in enumerate(word):
            m[i] = ind//8 +1
            
        return sum(m.values())
            
            
            