# Graph Ref : https://www.youtube.com/watch?v=A8ko93TyOns&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=8

from collections import deque

number_of_nodes = 11
graph ={
    
    1: [2],
    2: [1,4],
    3: [5],
    4: [2],
    5: [3, 10, 6],
    6: [5, 7],
    7: [6, 8],
    8: [7, 9, 11],
    9: [10, 8],
    10: [5, 9],
    11: [8]
}

# Cycle Detection Using BFS 

visited = [False] * (number_of_nodes+1)

def cycle_detected(node):
    queue = deque()
    queue.append((node, -1))
    
    while queue:
        print(queue)

        first, prev = queue.popleft()
        for child in graph[first]:
            if visited[child] == False:
                queue.append((child, first))
                visited[child]=True
            elif prev != child:
                print("Cycle detected at Node : ", str(child))
                return True
            else: 
                continue
                # as previous node is parent of child that is why its visited
        
    return False
    

for i in range(1, number_of_nodes):
    if visited[i]==False:
        if cycle_detected(i):
            print("Cycle Detected")