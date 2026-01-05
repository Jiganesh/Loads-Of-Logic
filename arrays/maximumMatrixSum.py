# https://leetcode.com/problems/maximum-matrix-sum/

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:



        R = len(matrix)
        C = len(matrix[0])

        summation = 0
        negatives = 0
        subtract = float("inf")
        for i in range(R):
            for j in range(C):
                num = matrix[i][j]
                summation += abs(num)
                negatives += (num < 0)
                subtract = min(abs(num), subtract)

        if negatives%2==0:
            return summation
        else:
            return summation - 2*subtract