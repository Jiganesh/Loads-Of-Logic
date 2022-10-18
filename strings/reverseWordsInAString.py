# https://leetcode.com/problems/reverse-words-in-a-string/
# Author : Jiganesh

class Solution:
    def reverseWords(self, s: str) -> str:

        p = s.split()

        left = 0
        right = len(p)-1

        while left < right:
            p[left], p[right]= p[right], p[left]
            left +=1
            right -=1
        return " ".join(p)
