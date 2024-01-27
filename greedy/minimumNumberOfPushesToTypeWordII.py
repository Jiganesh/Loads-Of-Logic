# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:

        c = sorted(Counter(word).values(), reverse=True)
        result = 0

        for ind, count in enumerate(c):
            result += (ind//8+1) * count

        return result
   
