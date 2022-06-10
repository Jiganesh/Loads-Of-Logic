# Graph Ref : https://www.youtube.com/watch?v=Y9NFqI6Pzd4&list=PLgUwDviBIf0rGEWe64KWas0Nryn7SCRWw&index=9

number_of_nodes = 8

graph ={
    
    1: [3],
    2: [5],
    3: [1, 4],
    4: [3],
    5: [2,6,8],
    6: [5, 7],
    7: [6, 8],
    8: [7, 5]
}

def cycle_detected(node, prev):
    
    if visited[node]==False:
        visited[node]=True
        for child in graph[node]:
            if visited[child] == False:
                return cycle_detected(child, node)
            elif (child != prev):
                print("Cycle Detected At ", str(child))
                return True


visited = [False] * (number_of_nodes+1)

for i in range (1, number_of_nodes+1):
    if visited[i] == False:
        if cycle_detected(i, -1):
            print("Cycle Detected")