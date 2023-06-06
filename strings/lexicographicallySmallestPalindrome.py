# https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:

        left = 0
        right = len(s)-1

        s = list(s)


        while left < right:
            if s[left] == s[right]:
                left +=1
                right -=1
            else:
                s[left] = s[right] = min(s[left], s[right])

        return "".join(s)
