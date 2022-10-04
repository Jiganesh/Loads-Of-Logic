def bubble_sort(A): #First approach 
    iteration = 0
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            iteration += 1
            if(A[j]>A[j+1]):
                A[j],A[j+i]=A[j+1],A[j]
    return A, iteration

def bubble_sort_2(A): #Second approach
    iteration = 0
    for i in A:
        for j in range(len(A)-1): 
            iteration +=1
            if(A[j]>A[j+1]):
                swap(A,j,j+1)
    return A, iteration

def swap(A,i,j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

A = [1,2,8,6]
print(bubble_sort_2(A))

# steps find in bubble sort Number elements * (number of elements-1)