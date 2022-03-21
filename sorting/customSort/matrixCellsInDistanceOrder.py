# https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution(object):
    
    # TC : O(N^2)
    # SC : O(N^2)
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        
        def distance (point, x2= rCenter, y2= cCenter):
            x1 = point[0]
            y1 = point[1]
            return abs(x1-x2)+ abs(y1-y2)
        
        return sorted([ [i,j] for i in range(rows) for j in range(cols)],key=distance)