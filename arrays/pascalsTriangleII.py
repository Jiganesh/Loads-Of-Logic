# https://leetcode.com/problems/pascals-triangle-ii/
# https://www.youtube.com/watch?v=6FLvhQjZqvM

from math import comb

class Solution:
    def getRow(self, rowIndex: int):
        
        array = []
        
        for i in range (rowIndex+1):
            array.append(comb(rowIndex, rowIndex-i))
            
        return array
    
        