# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    # TC : O(N)
    # SC : O(1)
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:

        arr.sort()
        previous_num = 0

        for num in arr:
            new_num = min(previous_num+1, num)
            previous_num = new_num

        return previous_num