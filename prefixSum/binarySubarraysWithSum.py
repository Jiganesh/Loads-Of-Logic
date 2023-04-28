# https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        lookup = defaultdict(int)
        lookup[0] = 1

        prefix_sum = list(accumulate(nums, operator.add))

        result = 0

        for num in prefix_sum :
            if num-goal in lookup:
                result += lookup[num-goal]

            lookup[num]+=1

        return result