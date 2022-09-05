# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

import math

class Solution:
    
    # Runtime: 7185 ms, faster than 11.37% of Python3 online submissions for Number of Ways to Reach a Position After Exactly k Steps.
    # Memory Usage: 643.8 MB, less than 33.44% of Python3 online submissions for Number of Ways to Reach a Position After Exactly k Steps.
    
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        MOD = (10**9)+7
        
        dp = {}
        def helper(startPos, endPos, currentPos ,k ):
                    
            if k==0:
                if currentPos == startPos:
                    return 1
                else :
                    return 0
            
            if (currentPos, k) in dp:
                return dp[(currentPos,k)]
            
            dp[(currentPos, k)] = (helper(startPos, endPos, currentPos-1, k-1) + helper(startPos, endPos, currentPos+1, k-1))%MOD
            return dp[(currentPos, k)]
        
        return helper(startPos, endPos, endPos, k)
    
    # Math Way
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        # if (startPos + endPos) and k have different parity, then return 0
        # otherwise we can use comb to get k choose (endPos - startPos + k) / 2
        # it can also be k choose k - (endPos - startPos + k) / 2)
        # assuming endPos >= startPos, and we know
        # left + right = k -- (1)
        # right - left = endPos - startPos -- (2)
        # (1) + (2)
        # left + right - left + right = k + endPos - startPos
        # 2 * right = endPos - startPos + k
        # right = (endPos - startPos + k) / 2
        # in other word, left would be k - (endPos - startPos + k) / 2)
        if (startPos + endPos) % 2 != k % 2:
            return 0
        else:
            return math.comb(k, (endPos - startPos + k) // 2) % MOD
