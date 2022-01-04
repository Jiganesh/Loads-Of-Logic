def spiralOrder(matrix):
    # m=len(matrix)       #rows
    # n=len(matrix[0])    #column
    # trav= []
    # startm,endm=0,m
    # startn,endn=0,n
    # while startm<endm and startn<endn:
    #     for i in range(startn, endn):       #moving left to right through column
    #         trav.append(matrix[startm][i])  #row will be decided by startm ie top
    #     startm+=1                           #top row will move downward to crop the matrix
    #     for i in range(startm, endm):       #moving top to bottom through m rows
    #         trav.append(matrix[i][endn-1])  #column will be const and is right end endn, and to avoid out of bound index -1
    #     endn-=1                             #matrix be cropped by shifting rightmost end towards left
        
    #     if not (startm<endm and startn<endn):
    #         break

    #     for i in range(endn-1, startn-1, -1):       #moving right to left through column
    #         trav.append(matrix[endm-1][i])          #row will be decided by endm ie bottom
    #     endm-=1                                     #bottom row will move upward to crop the matrix
    #     for i in range(endm-1, startm-1,-1):        #moving bottom to top through m rows
    #         trav.append(matrix[i][startn])          #column will be const and is left end startn
    #     startn+=1                                   #matrix be cropped by shifting leftmost end towards right
    
        
    # return(trav)


    m,n = len(matrix), len(matrix[0])   #rows,columns, adjust these to crop matrix after every complete operation
    x,y=0,-1                            #for Traversal ie accesssing matrix
    dirr= 1                             #for controlling traversal, ie increase/decreasing x, y values
    trav=[]
    
    #first travese to right, after completing operation crop matrix by decreasing m
    #then move downwards again crop matrix as rightmost column is completed ie decrease n 
    #now we have to move right to left and bottom to top, for this change direction ie dirr
    #do this until m and n are valid ie greater than zero
    
    while m>0 and n>0:
        for _ in range(n):
            y+=dirr
            trav.append(matrix[x][y])
        m-=1
        
        for _ in range(m):
            x+=dirr
            trav.append(matrix[x][y])
        n-=1
        
        dirr*=-1
        
    return trav

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
