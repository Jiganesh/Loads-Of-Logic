import math

# https://leetcode.com/problems/koko-eating-bananas/
class Solution(object):
    
    # Submitted by @Jiganesh

    # Runtime: 492 ms, faster than 70.74% of Python3 online submissions for Koko Eating Bananas.
    # Memory Usage: 15.4 MB, less than 97.69% of Python3 online submissions for Koko Eating Bananas.
    
    # Python 3
    
    #TC : O(NlogM)
    #SC : O(1)
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        start  , end = 1, max(piles)
        eatingspeed= max(piles);
        while start<=end:
            
            mid = start + (end-start)//2
            hoursTaken = self.kBananas(mid, piles)        
            if hoursTaken <= h:
                eatingspeed = min(eatingspeed, mid)
                end = mid-1
            else :
                start =  mid+1
                
        return eatingspeed
            
    def kBananas(self,mid, piles):
        hoursTaken = 0
        for i in piles:
            hoursTaken += math.ceil(i/mid)
        return hoursTaken            
    
print(Solution().minEatingSpeed([3,6,7,11],8))
print(Solution().minEatingSpeed([30,11,23,4,20],5))
print(Solution().minEatingSpeed([30,11,23,4,20],6))
print(Solution().minEatingSpeed([312884470],968709470))