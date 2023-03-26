# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        
        
        nums.sort()
        n = len(nums)
        prefix_sum = [0] + list(accumulate(nums, operator.add))
        result  = []

        for q in queries:
            ind = bisect.bisect_left(nums, q)
            left = prefix_sum[ind]
            right = prefix_sum[-1] - prefix_sum[ind]

            answer = abs(left-q*ind) + abs((n-ind)*q-right)
            result.append(answer)
        return result
        