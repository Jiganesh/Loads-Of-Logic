# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)


        visited = [0 for i in range(numCourses)]


        stack = []

        def helper(node):
            print
            if visited[node] == 1:
                return True
            if visited[node] == -1:
                return False

            visited[node] = -1
            for child in graph[node]:
                if visited[child]==-1 or (visited[child]==0 and not helper(child)):
                    return False
            visited[node] = 1
            stack.append(node)
            return True

        for i in range (numCourses):
            if not helper(i):
                return []

        return stack