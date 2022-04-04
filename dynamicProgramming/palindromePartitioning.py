w = [2,1]
v=[12,11]
c = 3

dp=[[-1]*(len(w)+1) for i in range (c+1)]

def knapsack (w, v, c, i):

    if c ==0 or i==0:
        return 0
    
    weight = w[i-1]
    value = v[i-1]
    if weight <= c:
        ans = max(value + knapsack(w, v, c-weight , i-1), knapsack(w,v,c, i-1))
    else:
        ans= knapsack(w,v, c ,i-1) 
    
    return ans

print(knapsack(w,v, c, 2))    

for i in dp:
    print(*i)
        
        
        