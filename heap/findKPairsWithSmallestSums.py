import heapq


class Solution(object):
    
    
    # TC : O(KlogK)
    # SC : O(N)
    
    # Runtime: 1299 ms, faster than 50.42% of Python online submissions for Find K Pairs with Smallest Sums.
    # Memory Usage: 30.3 MB, less than 83.76% of Python online submissions for Find K Pairs with Smallest Sums.

    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs
        
        
nums1 =[1,2,4,5,6]
nums2 =[3,5,7,9]
k = 3
print(Solution().kSmallestPairs(nums1, nums2, k))