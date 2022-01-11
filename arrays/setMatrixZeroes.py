# def change_values(i,j, matrix):
#     for col in range(len(matrix[0])):
#         if matrix[i][col]!=0:
#             matrix[i][col]=None

#     for rows in range(len(matrix)):
#         if matrix[rows][j]!=0:
#             matrix[rows][j]=None

#     return matrix

def setZeroes(matrix):
    
    #brute force method: : 
    #time complexity (m*n*(m+n)) space (m*n)
    #check every element if its zero, if yes change that row and column with value NONE
    #as early change to zero is dangerous 
    #then again with traversal change that NONE to 0

#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]==0:
#                     change_values(i,j, matrix)

#         for r in range(len(matrix)):
#             for c in range(len(matrix[0])):
#                 if matrix[r][c]==None:
#                     matrix[r][c]=0

#-------------------------------------------------------------

    #instead of changeing every element just store the index of current zeros in list [i,j]
    #and then change whole rows and column values to zero while iterating with indexes
    #time: (m*n) space ()
    
    
#         ind=[]
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]==0:
#                     ind.append([i,j])

#         for i in range(len(ind)):
#             matrix[ind[i][0]]=[0]*len(matrix[0])

#         for cnt in range(len(ind)):
#             for j in range(len(matrix)):
#                 matrix[j][ind[cnt][1]]=0

#----------------------------------------------------------------------------------------

    #A more efficient solution will be to store these index in set saperately for easy access

#         indi, indj=set(),set()
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]==0:
#                     indi.add(i)
#                     indj.add(j)

#         for i in indi:
#             for j in range(len(matrix[0])):
#                 matrix[i][j]=0
        
    
#         for i in range(len(matrix)):
#             for j in indj:
#                 matrix[i][j]=0


#-----------------------------------------------------------------------------------------------
           
    #But if we can use a flag like method to check the first or last row/column has zero,
    #it will be easy to just iterate through matrix checking if row / column contains zero value
    #if yes then mark that element to be zero
    #Time: m*n Space: O(1) 
    
    zero_inrow=False
    zero_incol=False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:   
                if i==0:     #first row
                    zero_inrow=True
                if j==0:    #first column
                    zero_incol=True
                matrix[i][0]=matrix[0][j]=0
                

    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
                
    #but remember, update first row and col t0 zero after updating remaining matrix            
    if zero_inrow:
        for col in range(len(matrix[0])):
            matrix[0][col]=0
    
    if zero_incol:
        for row in range(len(matrix)):
            matrix[row][0]=0   

    return matrix  

print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))