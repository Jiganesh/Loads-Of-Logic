# https://leetcode.com/problems/count-lattice-points-inside-a-circle/

class Solution:
    
    # Runtime: 2751 ms, faster than 77.43% of Python3 online submissions for Count Lattice Points Inside a Circle.
    # Memory Usage: 18.8 MB, less than 22.94% of Python3 online submissions for Count Lattice Points Inside a Circle.
    
    def countLatticePoints(self, circles) -> int:
        self.set_of_points = set()
        circles = set(tuple(i) for i in circles)
        
        def helper(point):
            x, y , r = point
            for i in range (x-r, x+r+1):
                for j in range (y-r, y+r+1):
                    if ((i-x)**2+ (j-y)**2) <= r**2:
                        self.set_of_points.add((i, j))
                        
                        
        for point in circles: helper(point)

        return len(self.set_of_points)