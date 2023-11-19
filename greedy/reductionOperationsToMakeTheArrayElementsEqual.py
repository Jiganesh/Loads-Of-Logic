# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/editorial/

class Solution:

    # TC : O(K * log K)
    # SC : O(K)

    # K is number of unique elements in nums array

    def reductionOperations(self, nums: List[int]) -> int:

        counter = Counter(nums)
        heap = [(-k,v) for k, v in counter.items()]
        heapq.heapify(heap)


        result = 0

        while len(heap) >=2 :
            largest, largest_count = heapq.heappop(heap)
            second_largest, second_largest_count = heapq.heappop(heap) 


            result += largest_count
            heapq.heappush(heap, (second_largest, largest_count+second_largest_count))

        return result
        

    def reductionOperations(self, nums: List[int]) -> int:

        key_count = Counter(nums)
        nums = [[k, v] for k , v in key_count.items()]
        nums.sort()

        n, result  = len(nums), 0

        for i in range (n-1, 0 , -1):
            result += nums[i][-1]
            nums[i-1][-1] += nums[i][-1]

        return result
        

        