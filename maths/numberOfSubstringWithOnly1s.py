# https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution:
    def numSub(self, s: str) -> int:
        result =  count = 0
        MOD = 10**9+7

        for i in s :
            if i=='1':
                count +=1
                result += count
            else :
                count=0

        return result % MOD
