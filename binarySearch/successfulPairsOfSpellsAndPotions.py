# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

import bisect

class Solution:
    # Runtime: 1351 ms, faster than 57.14% of Python3 online submissions for Successful Pairs of Spells and Potions.
    # Memory Usage: 37.5 MB, less than 57.14% of Python3 online submissions for Successful Pairs of Spells and Potions.
    
    # TC : O(n*log(m))
    # SC : O(N)
    def successfulPairs(self, spells , potions , success: int) :
        
        result = []
        
        portions_length = len(potions)
        potions.sort() # we can find point from where the potions start being sucessful and no need to count
        
        for spell in spells:
            
            point = bisect.bisect_left(potions, success/spell)
            # success/spell pin points in between because of floating point
            # math.ceil(success/spell) works too
            #  7/3 = 2.3333    1,2,3,4,5  ==> 3,4,5
            #  ceil 7/3 = 3    1,2,3,4,5  ==> 3,4,5
            result.append(portions_length - point)
            
        return result
 