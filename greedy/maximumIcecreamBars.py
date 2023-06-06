# https://leetcode.com/problems/maximum-ice-cream-bars/
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()

        result = 0
        
        for cost in costs:
            if coins-cost >= 0 :
                result +=1
                coins-=cost
        return result