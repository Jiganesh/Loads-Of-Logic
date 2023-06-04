# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        graph = defaultdict(list)

        for ind, row in enumerate(isConnected):
            for j in range (len(row)):
                if row[j] ==1:
                    graph[ind].append(j)

        C = len(isConnected[0])
        visited = [False] * C

        count = 0

        def helper(city):

            for child in graph[city]:
                if visited[child] == False:
                    visited[child] = True
                    helper(child)

        for ind in range (C):

            if visited[ind] == False:
                count +=1
                helper(ind)
        return count
