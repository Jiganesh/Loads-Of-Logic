# https://leetcode.com/problems/minimize-string-length/

class Solution(object):
    def minimizedStringLength(self, s):
        """
        :type s: str
        :rtype: int
        """

        return len(set(s))