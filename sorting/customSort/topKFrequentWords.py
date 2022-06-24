# https://leetcode.com/problems/top-k-frequent-words/

from typing import List
from collections import Counter



class Solution:
    
    # TC: O(N + NlogN)
    # SC : O(N+N)
    
    # Runtime: 102 ms, faster than 23.97% of Python3 online submissions for Top K Frequent Words.
    # Memory Usage: 14 MB, less than 27.43% of Python3 online submissions for Top K Frequent Words.
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        
        dictionary = Counter(words)
        
        def custom_sort(word):
            return -dictionary[word], word
        
        return sorted(dictionary.keys(), key= custom_sort)[:k]
    
    
