#https://leetcode.com/problems/maximal-rectangle/

def mah(lst):
    sta,finalL=[],[]
    it=0
    for i in lst:               #code for next smallest left
        it+=1
        if sta:
            while(sta and i<=sta[-1][1]):
                sta.pop()
            
            if not sta:
                finalL.append(-1)
            
            elif (i>sta[-1][1]):
                finalL.append(sta[-1][0]-1)

        else:
            finalL.append(-1)

        sta.append([it,i])

    it,sta,finalR=len(lst),[],[]   #code of Next smallest right
    for i in lst[::-1]:     #change is it=7, it-=1 for counting index
        it-=1               #as it process in reverse    
        if sta:
            while(sta and i<=sta[-1][1]):
                sta.pop()
                
            if not sta:
                #if array empty 1 index ahead of last index ie here 7
                finalR.append(len(lst))
            
            elif (i>sta[-1][1]):
                finalR.append(sta[-1][0])

        else:
            finalR.append(len(lst))

        sta.append([it,i])
        
    finalR=finalR[::-1]   

    final=[]        #calculate width=NSR-NSL-1 and area=width*height[k] ie arr[k]
                        
    for k in range(len(lst)):
        final.append( (finalR[k] - finalL[k] -1) *lst[k])

    return max(final)

def maxrect():
    #inputs n*m and arr[][]
    rows,column=int(input()),int(input())
    mat= [[int(input()) for x in range(column)] for y in range(rows)]

    if rows==0 and column==0:
        return 0
    
    #for printing matrix
    for i in range(rows):
        for j in range(column):
            print(mat[i][j], end=" ")
        print()

    i,j=0,0
    vector=[]
    #for 1st row
    for j in range(column):
        vector.append(mat[0][j])

    #calculate max MAH of this 1d array
    mx=mah(vector)
    print("mx",mx)

    #for 2nd row to last
    for i in range(1, rows):
        for j in range(column):
            if mat[i][j]==0:
                vector[j]=0

            else:
                vector[j]=vector[j]+mat[i][j]

        mx1=mah(vector)     #current mah of vector
        print("mx1",mx1)
        mx=max(mx, mx1)

    return mx
