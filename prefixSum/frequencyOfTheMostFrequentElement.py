# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

# Reference
# https://www.youtube.com/watch?v=-jxoqpbxrJc&t=311s
# https://www.youtube.com/watch?v=vgBrQ0NM5vE

class Solution:

    # Runtime: 1508 ms, faster than 89.63% of Python3 online submissions for Frequency of the Most Frequent Element.
    # Memory Usage: 27.7 MB, less than 72.30% of Python3 online submissions for Frequency of the Most Frequent Element.


    # TC : O(N log N)
    # SC : O(N)
    
    def maxFrequency(self, nums, k: int) -> int:

        nums.sort()

        window_sum = k
        index_start = 0

        result  = 0

        for index_end , number in enumerate(nums):
            window_sum += number

            while window_sum < number*(index_end -index_start+1):
                window_sum-=nums[index_start]
                index_start+=1

            result = max( result , index_end-index_start+1)

        return result



