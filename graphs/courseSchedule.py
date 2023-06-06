# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # -1 - Parent
        # O - Not visited yet
        # 1 - Visited

        visited = [0 for i in range (numCourses)]

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)


        def helper(node):
            visited[node]= -1
            for child in graph[node]:
              if visited[child] == -1 or (visited[child] == 0 and not helper(child)):
                  return False
            visited[node] = 1
            return True


        for i in range(numCourses):
            if visited[i] == 0 and not helper(i): 
                return False
                
        return True
      