class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        array = [1]*numOnes + [0]*numZeros + [-1]*numNegOnes
        return sum(array[:k])

    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        return min(k, numOnes) - max(0, k-numOnes-numZeros)