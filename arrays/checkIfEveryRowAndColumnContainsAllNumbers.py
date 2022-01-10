class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n =len(matrix)
        columneach=[]
        for i in range(n):
            for j in range(n):
                columneach.append(matrix[j][i])
            
            for p in range(1, n+1):
                if p not in columneach or p not in matrix[i]:
                    return False
            columneach=[]
                
        return True
            
    
            
              
                
                
print(Solution().checkValid([[1,2,3],[3,1,2],[2,3,1]]))
print(Solution().checkValid([[1,1,1],[1,2,3],[1,2,3]]))

        
        