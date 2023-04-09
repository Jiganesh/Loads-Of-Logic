# https://leetcode.com/problems/prime-in-diagonal/

class Solution:
  
    def diagonalPrime(self, nums: List[List[int]]) -> int:

        def isprime(num):
            if num <= 1:
                return False

            for i in range (2, int(sqrt(num))+1):
                if num%i == 0:
                    return False
            return True

        R = len(nums)
        C = len(nums[0])
        result = 0

        for i in range (R):
            for j in range (C):

                if (abs(i-j) == 0 or abs(i+j) == R-1 ) and isprime(nums[i][j]):

                    result = max(result, nums[i][j])

        return result
