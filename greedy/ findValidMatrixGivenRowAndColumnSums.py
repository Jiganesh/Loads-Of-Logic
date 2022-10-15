class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        R = len(rowSum)
        C = len(colSum)

        matrix = [[0]*C for _ in range(R)]

        for i in range(R):
            for j in range(C):

                value = min(rowSum[i], colSum[j])
                rowSum[i]-=value
                colSum[j]-=value
                matrix[i][j] = value 

        return matrix
