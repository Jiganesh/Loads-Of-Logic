# https://leetcode.com/problems/bag-of-tokens/

from typing import List


class Solution:
    
    # Runtime: 56 ms, faster than 94.81% of Python3 online submissions for Bag of Tokens.
    # Memory Usage: 14 MB, less than 77.36% of Python3 online submissions for Bag of Tokens.

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        max_score = 0
        
        left = 0
        right = len(tokens)-1
        
        tokens.sort()
        
        score = 0
        while left <= right :
            
            if power >= tokens[left]:
                power-=tokens[left]
                left+=1
                score+=1
                
                max_score = max(max_score, score)
                
            elif score>=1 :
                
                power+=tokens[right]
                score-=1
                right-=1
                
            else:
                
                break
            
        return max_score
    