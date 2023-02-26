# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:

        nums.sort()

        n = len(nums)
        
        left_pointer = mid = (n-1)//2
        right_pointer = n-1

        count = 0
        while left_pointer >= 0 and right_pointer > mid:
            if  nums[left_pointer] * 2 <= nums[right_pointer]:

                right_pointer-=1
                count +=1


            left_pointer-=1

        return count*2