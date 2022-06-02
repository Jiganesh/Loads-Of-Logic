# https://leetcode.com/problems/transpose-matrix/

class Solution(object):
    
    # Runtime: 78 ms, faster than 42.44% of Python online submissions for Transpose Matrix.
    # Memory Usage: 14.2 MB, less than 86.05% of Python online submissions for Transpose Matrix.
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
        result = [[0]*len(matrix) for i in range (len(matrix[0]))]
        
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                result[j][i] = matrix[i][j]
                
        return result
    
    # Runtime: 52 ms, faster than 91.86% of Python online submissions for Transpose Matrix.
    # Memory Usage: 14.4 MB, less than 40.12% of Python online submissions for Transpose Matrix.
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*matrix))