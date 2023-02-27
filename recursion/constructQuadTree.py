# https://leetcode.com/problems/construct-quad-tree/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':


        n = len(grid)


        if n == 0 :
            return None


        def allSameNodes(x, y, n):
            nodeVal = grid[x][y]

            for r in range (x, x+n):
                for c in range (y,y+n):
                    if grid[r][c] != nodeVal:
                        return False
            return True



        def solve(x, y, n):


            if allSameNodes(x, y, n):
                return Node (grid[x][y], True)

            else:

                root = Node (1, False)
                root.topLeft = solve(x, y, n//2)
                root.topRight = solve(x, y+n//2 , n//2)
                root.bottomLeft = solve(x+n//2, y, n//2)
                root.bottomRight = solve(x+n//2, y+n//2, n//2)

            return root

        return solve(0, 0, n)

        