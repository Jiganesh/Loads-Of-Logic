# https://leetcode.com/problems/assign-cookies/

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        i = 0
        count = 0
        for cookie in s:
            if i < len(g) and cookie >= g[i]:
                i+=1
                count+=1
        return count