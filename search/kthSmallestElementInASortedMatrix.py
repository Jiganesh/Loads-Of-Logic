# https://www.youtube.com/watch?v=0d6WF79hQME&t=235s
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

import bisect
import heapq

class Solution:
    # Runtime: 182 ms, faster than 92.74% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # Memory Usage: 18.9 MB, less than 16.73% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.    

    # TC : O(m*n log (m*n))
    # SC : O(N)
    def kthSmallest(self, matrix, k):    
        low=[]
        for i in matrix:
            low.extend(i)
        low.sort()
        return low[k-1]
    
    # Runtime: 367 ms, faster than 19.31% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # Memory Usage: 18.8 MB, less than 37.81% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    
    # TC : O(m*n log k)
    # SC : O(k)
    def kthSmallest(self, matrix, k):    

        nums = []
        
        for i in matrix:
            for j in i:
                
                heapq.heappush(nums, -j)
                if len(nums)>k:
                    heapq.heappop(nums)
                    
        return heapq.heappop(nums)*-1
    
    
    # Runtime: 330 ms, faster than 27.98% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    # Memory Usage: 18.8 MB, less than 38.25% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
    
    # TC : O(m+n)
    # SC :O(1)
    def kthSmallest(self, matrix, k) :
        
        def count_elements_less_than_given(mid):
            count =0
            for i in matrix:
                count+= bisect.bisect_right(i, mid)
            return count
            
        
        low = matrix[0][0]
        high = matrix[-1][-1]
        
        while low<high:
            
            mid = low+ (high - low)//2
            if count_elements_less_than_given(mid) < k:
                low = mid+1
            else:
                high=mid
                
        return low
            
print (Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))
