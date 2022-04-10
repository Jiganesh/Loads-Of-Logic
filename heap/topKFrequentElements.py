# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq

class Solution:
    # Runtime: 160 ms, faster than 35.80% of Python3 online submissions for Top K Frequent Elements.
    # Memory Usage: 18.7 MB, less than 40.43% of Python3 online submissions for Top K Frequent Elements.
    
    def topKFrequent(self, nums, k):
        
        dictionary = Counter(nums)
        
        heap = []
        for key , count in dictionary.items() :
            
            heapq.heappush(heap, (count, key))
            
            if len(heap)> k:
                heapq.heappop(heap)
            
        return [i[1] for i in heap]
    
    
   
        
        
        
        
    