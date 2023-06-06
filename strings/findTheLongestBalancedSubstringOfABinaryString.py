# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:

        c0 = 0
        c1 = 1

        result = 0
        for ch in s:
            if ch == '0':
                if c1:
                    c0 = 0
                    c1 = 0
                c0 += 1
            else:
                c1 += 1

            if c0 and c1:
                result = max(result, min(c0, c1)*2)

        return result
            