# https://leetcode.com/problems/elimination-game/

class Solution:
    
    # Runtime: 80 ms, faster than 33.80% of Python3 online submissions for Elimination Game.
    # Memory Usage: 14 MB, less than 25.17% of Python3 online submissions for Elimination Game.
    
    def lastRemaining(self, n: int) -> int:
        
        def helper(n, is_left):
            
            # Base Condition
            # Only One element is left
            if n==1:
                return 1
                
            if is_left :
                # All the odd number will be removed
                # If n is 5 i.e [1,2,3,4,5] --> [2,4] --> 2 * [1, 2]
                # If n is 4 i.e [1,2,3,4] --> [2, 4] --> 2 * [1, 2]
                
                return 2 * helper(n//2,  False)
            
            # If the run is from right there can be two cases
            # n is odd that is [1, 2, 3, 4, 5] --> [2, 4] --> 2*[1, 2]
            
            if n%2:
                return 2 * helper(n//2, True) 
            
            # n is even that is [1, 2, 3, 4] --> [1, 3] --> 2*[1, 2] - 1
            else :
                return 2 * helper(n//2, True) - 1
                
        return helper(n, True)