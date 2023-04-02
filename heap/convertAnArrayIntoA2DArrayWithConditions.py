# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        c = Counter(nums)
        most_frequent = max(c.values())
        heap = [[-value, key] for key, value in c.items() ]
        
        heapq.heapify(heap)
        
        result = [[] for i in range (most_frequent)]
        
        
        while heap:
            v, k = heapq.heappop(heap)

            for i in range(-v):

                result[i].append(k)
                
        return result
