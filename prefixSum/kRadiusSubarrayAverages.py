# https://leetcode.com/problems/k-radius-subarray-averages/

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        prefix_sum = [0]+list(accumulate(nums, operator.add))
        n = len(nums)


        if k == 0:
            return nums

        denominator = 2 * k + 1

        result = [-1]*(n)
        for i in range (2*k, n):
            
            if i >= 2*k-1:
                summation = prefix_sum[i+1] - prefix_sum[i-2*k]
                result[i-k] = summation // denominator


                

        return result
