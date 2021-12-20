 # https://leetcode.com/problems/adding-spaces-to-a-string/
class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        array = []
        start = 0
        for i in spaces:
            array.append(s[start:i])
            start = i
        array.append(s[start:])
        return " ".join(array)
    
print(Solution().addSpaces("LeetcodeHelpsMeLearn", [8,13,15]))