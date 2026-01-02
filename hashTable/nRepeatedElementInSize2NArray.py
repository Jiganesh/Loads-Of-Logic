# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution:

    # TC: O(N)
    # SC: O(N)
    def repeatedNTimes(self, nums: List[int]) -> int:

        unique = set()
        for num in nums:
            if num in unique: return num
            unique.add(num)


            