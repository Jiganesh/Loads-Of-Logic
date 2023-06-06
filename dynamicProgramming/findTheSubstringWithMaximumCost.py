# https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        
        dictionary = {chr(96+i):i for i in range (1,27)}

        for ind in range (len(chars)):
            dictionary[chars[ind]] = vals[ind]

        current = 0
        maximum = 0

        for ch in s:
            current = max(current+dictionary[ch], dictionary[ch])
            maximum = max(current , maximum)

        return maximum
