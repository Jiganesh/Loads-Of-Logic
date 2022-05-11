# https://www.youtube.com/watch?v=6FLvhQjZqvM
from math import comb


class Solution:
    
    # Runtime: 41 ms, faster than 54.55% of Python3 online submissions for Pascal's Triangle II.
    # Memory Usage: 13.8 MB, less than 97.58% of Python3 online submissions for Pascal's Triangle II.
    
    def getRow(self, rowIndex: int):
        
        array = [1]
        for i in range (rowIndex):
            a = [1]
            for j in range (len(array)-1):
                a.append(array[j]+array[j+1])
            a.append(1)
            array=a
        return array
    
    # OP SOLUTION
    
    def getRow(self, rowIndex: int):

        array = [1]
        
        for i in range (1,rowIndex+1):
            array.append(comb(rowIndex, rowIndex-i))
            
        return array
        