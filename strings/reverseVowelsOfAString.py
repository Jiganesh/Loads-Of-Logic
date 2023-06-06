# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        string = list(s)

        left = 0 
        right = len(string)-1

        vowels = "aeiouAEIOU"

        while left < right:
            if string[left] not in vowels:
                left+=1
            elif string[right] not in vowels:
                right-=1
            else:
                string[left], string[right] = string[right], string[left]
                left+=1
                right-=1
        
        return "".join(string)

