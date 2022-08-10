# https://leetcode.com/problems/merge-similar-items/


from collections import defaultdict, Counter
from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        dictionary = defaultdict(int)
        for val , weight in items1:
            dictionary[val]+=weight
            
        for val , weight in items2:
            dictionary[val]+=weight
            
        return sorted( [key, value] for key, value in dictionary.items())
    
    
    # One Liner
    
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    
        return sorted((Counter(dict(items1))+Counter(dict(items2))).items())
        
    
