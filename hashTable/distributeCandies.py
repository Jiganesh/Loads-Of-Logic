
class Solution:
    # Runtime: 1029 ms, faster than 49.28% of Python3 online submissions for Distribute Candies.    
    # Memory Usage: 16.4 MB, less than 8.62% of Python3 online submissions for Distribute Candies.

    def distributeCandies(self, candyType):
        
        candies_advised = len(candyType)//2
        return min(len(set(candyType)), candies_advised)
        