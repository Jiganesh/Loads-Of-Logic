from typing import List
import heapq

# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

class Solution:
    
    # TC : O(N log N)
    # SC : O(K)
    
    # Runtime: 130 ms, faster than 28.22% of Python3 online submissions for Kth Largest Element in an Array.
    # Memory Usage: 14.8 MB, less than 40.87% of Python3 online submissions for Kth Largest Element in an Array.
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        
        for i in nums:
            heapq.heappush(heap, i)
            
            if len(heap)>k:
                heapq.heappop(heap)
                            
        return heap[0]
        