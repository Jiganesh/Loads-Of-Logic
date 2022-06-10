number_of_nodes = 5
number_of_edges = 7
list_of_edges = [(1,2),(1,3),(1,5),(2,4),(2,3),(3,4),(3,5)]
list_of_edges_with_weights = [(1,2,4),(1,3,5),(1,5,8),(2,4,2),(2,3,3),(3,4,4),(3,5,1)]




# Adjacency Matrix Undirected
# 1-based Indexing
print("Adjacency Matrix Undirected Graph without weights")
adjacency_matrix = [[0]*(number_of_nodes+1) for i in range(number_of_nodes+1)]

for u, v in list_of_edges:
    adjacency_matrix[u][v]=1
    adjacency_matrix[v][u]=1


for i in adjacency_matrix:
    print(*i)
    
   
# Adjacency List Undireceted
# 1-based Indexing
print("Adjacency List Undirected Graph without weights")
adjacency_list = {}

def add(nodea, nodeb):
    if nodea in adjacency_list:
        adjacency_list[nodea].append(nodeb)
    else:
        adjacency_list[nodea]=[nodeb]
        
for u, v in list_of_edges:
    add(u,v)
    add(v,u)
    
print(adjacency_list)

'''Note : When graphs are directed you can just do one way update'''

# Weighted Graphs

# Adjacency Matrix Undirected
# 1-based Indexing
print("Adjacency Matrix Undirected Graph with weights")
adjacency_matrix = [[0]*(number_of_nodes+1) for i in range(number_of_nodes+1)]

for u, v, weights in list_of_edges_with_weights:
    adjacency_matrix[u][v]=weights
    adjacency_matrix[v][u]=weights


for i in adjacency_matrix:
    print(*i)
    
   
# Adjacency List Undireceted
# 1-based Indexing
print("Adjacency List Undirected Graph with weights")
adjacency_list = {}

def add(nodea, nodeb, weights):
    if nodea in adjacency_list:
        adjacency_list[nodea].append((nodeb,weights))
    else:
        adjacency_list[nodea]=[(nodeb,weights)]
        
for u, v ,weights in list_of_edges_with_weights:
    add(u,v, weights)
    add(v,u, weights)
    
print(adjacency_list)