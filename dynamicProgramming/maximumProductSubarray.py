# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        def helper(array):

            product = 1
            result = min(array)

            for num in array:
                product *= num
                result = max(result, product)
                if product == 0:
                    product = 1

            return result

        maxProd_left = helper(nums)
        maxProd_right = helper(nums[::-1])

        return max(maxProd_left, maxProd_right)