# Solution to 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/

###################################################################################################
#
#   This approach uses a variant of Prim's algorithm, where one array stores the minimum cost to
#   connect each point, and another to store all visited points (i.e. the MST).
#
#   For each unvisited point added to the MST, store the minimum cost to connect to all unvisited
#   points. The next point to visit has the least minimum cost in the array.
#
#   Finally, return the total cost of the MST.
#
#   Time complexity:    O(N^2) For each point, the algorithm checks all adjacent points, which
#                       takes O(N) time.
#
#   Space complexity:   O(N) Two arrays of size N.
#
###################################################################################################
def minCostConnectPoints(points):
    out = 0
    # List of visited points
    list_visit = [False] * len(points)
    # List of minimum costs to connect all points
    list_min = [10**7] * len(points)

    # Set the cost to first point to 0
    if len(points) <= 0:
        return out
    else:
        list_min[0] = 0

    i = 0
    while i >= 0:
        min_cost = 10**7
        next_point = -1

        # Visit point
        list_visit[i] = True

        for j in range(0, len(points)):
            if i != j and not(list_visit[j]):
                # Get cost to connect points i and j
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            
                # Add lesser cost to min list
                if cost < list_min[j]:
                    list_min[j] = cost
                
                # Set min cost and next point to visit
                if min_cost > list_min[j]:
                    min_cost = list_min[j]
                    next_point = j
        
        # Go to next point
        i = next_point

    # Add total minimum cost
    for min_cost in list_min:
        out += min_cost

    return out

# Some leetcode test cases
print(minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
print(minCostConnectPoints([[0, 0], [1, 1], [1, 0], [-1, 1]]))
