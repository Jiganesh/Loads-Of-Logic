# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

class Solution:

    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:

        xor1 = 0
        for num in arr1:
            xor1 ^= num
        
        xor2 = 0
        for num in arr2:
            xor2 ^= num
        
        return xor1 & xor2
