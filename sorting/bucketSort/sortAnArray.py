import math
from typing import List
import itertools

class Solution:
    # Runtime: 356 ms, faster than 92.91% of Python3 online submissions for Sort an Array.
    # Memory Usage: 27.6 MB, less than 5.03% of Python3 online submissions for Sort an Array.
    
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def bucketSort(nums) :
            
            if not nums : return []
            
            n = len(nums)

            buckets = [[] for _ in range (n)]

            mx = max(max(nums, default = 1),1)
            mn = max(min(nums, default = 1),1)

            ranged = math.ceil((mx-mn)/n) 

            for num in nums:
                bucket_index = math.floor((n-1)*num/mx)
                buckets[bucket_index].append(num)
            print(buckets)

            sorted_buckets = [sorted(bucket) for bucket in buckets]
        
            return list(itertools.chain.from_iterable(sorted_buckets))
        
        negative = bucketSort([abs(i) for i in nums if i<0])
        positive = bucketSort([i for i in nums if i>=0])
        
        for i in range (len(negative)):
            negative[i] = negative[i]*-1
            
        return  list(reversed(negative)) + positive 
    
    
array = [8,8,-2,-7,-12,-1,-1,-1,7,2,1,1,9,3]
print(Solution().sortArray(array))