#https://practice.geeksforgeeks.org/problems/sort-a-stack/1


from collections import deque

#using another stack

# def SortStack(stack):
#     tempstack=deque()
#     while stack:
#         temp=stack.pop()
#         while tempstack and (tempstack[-1]>temp):
#             stack.append(tempstack.pop())
#         tempstack.append(temp)

#     for i in range(len(tempstack)):
#         stack.append(tempstack.pop())




#Using only one stack (RECURSION)

def SortStack(stack):
    if stack:
        temp=stack.pop()
        SortStack(stack)
        insertval(stack,temp)

def insertval(stack,val):
    if not stack or stack[-1]>val:
        stack.append(val)
        return
    else:
        temp=stack.pop()
        insertval(stack, val)
        stack.append(temp)

stack=deque()
stack.append(30)
stack.append(-5)
stack.append(18)
stack.append(14)
stack.append(-3)
print(stack)
SortStack(stack)
print(stack)