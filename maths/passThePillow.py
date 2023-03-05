# https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        time = time % ((n-1)*2 +1) +1
        return min(time, n*2 - time)