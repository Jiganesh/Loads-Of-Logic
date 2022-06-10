# https://leetcode.com/problems/flood-fill/

class Solution:
    # Runtime: 86 ms, faster than 72.01% of Python3 online submissions for Flood Fill.
    # Memory Usage: 14.1 MB, less than 37.52% of Python3 online submissions for Flood Fill.

    def floodFill(self, image, sr: int, sc: int, newColor: int) :
        
        R = len(image)
        C = len(image[0])
        
        def helper(i, j):
            
            
            if valid(i,j):
                if image[i][j]==newColor: return

                image[i][j]=newColor
                
                helper(i, j+1)
                helper(i+1, j)
                helper(i-1, j)
                helper(i, j-1)
            
        def valid(i,j):
            return 0<=i<R and 0<=j<C  and image[i][j] == currentColor
            
            
        currentColor = image[sr][sc]
        helper(sr, sc)
        
        return image
