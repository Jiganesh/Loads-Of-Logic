# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

from typing import List

class Solution:
    
    # Runtime: 662 ms, faster than 63.08% of Python3 online submissions for Capacity To Ship Packages Within D Days.
    # Memory Usage: 17 MB, less than 81.11% of Python3 online submissions for Capacity To Ship Packages Within D Days.
    
    # TC: O(NlogK)
    # SC : O(N)
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def days_needed(weights, weight):
            
            temp = weight
            result = 1
            
            for index, i in enumerate(weights):
                
                if temp>= i:
                    temp-=i
                else:
                    temp = weight
                    temp-=i
                    result +=1
                    
            return result
        
        
        l = max(weights) # VERY IMPORTANT
        r = sum(weights)
        
        while l<r:
            mid = (l+r)//2
            days_with_n_weight = days_needed(weights, mid) 

            
            if  days_with_n_weight > days:
                l = mid+1
            else :
                r = mid
        return l
    
    # Aesthetic Solution and smart way to write
    
    # TC : O(NLogK)
    # SC : O(1)            
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)
        while left < right:
            mid, need, cur = (left + right) / 2, 1, 0
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0
                cur += w
            if need > D: left = mid + 1
            else: right = mid
        return left
                