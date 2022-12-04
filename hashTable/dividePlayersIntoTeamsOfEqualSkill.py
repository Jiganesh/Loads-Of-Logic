# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

from typing import List
from collections import Counter


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        n = len(skill)
        t = n//2    # how many pairs will be created
        s = sum(skill) // t  # what will be sum of each pair
        
        c = Counter(skill)  # keep track of how many numbers we have
        lookup =Counter() # keep track of how many pairs generated
        
        for num in skill:
            # If we have number and equal can be generated from that number the make a pair
            if c[num] and s- num in c and c[s-num]>0:
                c[s-num]-=1
                c[num]-=1
                lookup[(s-num, num)]+=1
        
        # If some number is unused then return -1
        for k, v in c.items():
            if v!= 0:
                return -1

        # Calculate result as told
        result = 0
        for k,v in lookup.items():
            a, b = k
            # multiplying by v because that's number of pairs
            result += a*b*v
            
        return result