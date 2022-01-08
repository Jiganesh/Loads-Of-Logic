# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            if i==i[::-1]: return i
        return ""

print(Solution().firstPalindrome(["abc","car","ada","racecar","cool"])) #ada