# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:


        valid_array = []


        def solve(array) :
            n = len(array)
            count = 0
            minI, maxI = -1, -1

            for i in range (n):
                if array[i]== minK:
                    minI = i
                if array[i]== maxK:
                    maxI = i
                count += min(minI, maxI)+1
            return count
                
        result = 0
        for num in nums:
            if minK <= num <= maxK:
                valid_array.append(num)
            else :
                result += solve(valid_array)
                valid_array = []

        result += solve(valid_array)

        return result
