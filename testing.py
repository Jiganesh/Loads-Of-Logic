n, case = map(int, input().split(" "))
marks = list(map(int, input().split(" ")))
while case:
    ind, mark = map(int, input().split(" "))
    marks[ind-1]=mark
    case-=1
    
stack = []
for i in marks:
    if stack and stack[-1]==i:
        stack.pop()
    stack.append(i)

print(len(stack)) 

"""
5 2
1 1 2 5 2
1 3
4 2
"""