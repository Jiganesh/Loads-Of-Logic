# https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        len1 = len(str1)
        len2 = len(str2)

        for i in range (len2, 0, -1):

            probable_answer = str2[:i]

            copies = len1//i
            if (probable_answer*copies) != str1:
                continue

            copies = len2//i
            if (probable_answer*copies) != str2:
                continue

            return probable_answer
        return ""
